from django.core.serializers import serialize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import now
import datetime
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.db.models import Q
from .forms import ChatGroupForm
from .models import ChatBox, Message, ChatGroup, GroupRequest, GroupMessage, Notification
from webpush import send_user_notification
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def chat_friend(request):
    action = request.GET.get('action')
    pk = request.GET.get('pk')
    if action == 'friend':
        print('THIS IS A FRIEND')
        friend = get_object_or_404(User, pk=pk)
        chat_box = ChatBox.objects.filter(user_1=request.user, user_2=friend).first()
        if not chat_box:
            chat_box = ChatBox.objects.filter(
                user_1=friend, user_2=request.user).first()
        if not chat_box:
            chat_box = ChatBox(user_1=request.user, user_2=friend)
            chat_box.save()
        chat_messages_list = Message.objects.filter(
            chat_box=chat_box).order_by('sent_date')
        paginator = Paginator(chat_messages_list, 7)
        if not request.GET.get('page'):
            page = 0
        else:
            page = int(request.GET.get('page'))
        page = paginator.num_pages - page
        try:
            chat_messages = paginator.page(page)
        except EmptyPage:
            chat_messages = []
        except PageNotAnInteger:
            chat_messages = paginator.page(paginator.num_pages)
        json_admin = {
            'id': friend.id,
            'username': friend.username,
            #'avatar': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png',
        }
        return JsonResponse({'friend': json_admin, 'chat_messages': serialize('json', chat_messages)})
    else:
        return redirect('/chat/')

@login_required(login_url="/login/")
def chat(request):
    return render(request, 'social/main.html')

@login_required(login_url="/login/")
def send_message(request):
    pk = request.GET.get('pk')
    action = request.GET.get('action')
    if action == 'friend':
        friend = User.objects.get(id=pk)
        chat_box = ChatBox.objects.filter(
            user_1=request.user, user_2=friend).first()
        if not chat_box:
            chat_box = ChatBox.objects.filter(
                user_1=friend, user_2=request.user).first()
        message = Message(
            chat_box=chat_box, message_sender=request.user, message=request.GET.get('message'))
        # !ABSOLUTE PATH
        notification = Notification.objects.create(sender=request.user, url='/chat/', content=message.message[:100])
        notification.save()
        notification.receiver.add(friend)
        for receiver in notification.receiver.all():
            sender_avatar = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
            payload = {"head": f"Message from {notification.sender}",
            "body": notification.content,
            "url": notification.url,
            "icon": sender_avatar,
            }
            send_user_notification(user = receiver, payload = payload,ttl = 1000)
    message.save()
    return JsonResponse({})

@login_required(login_url="/login/")
def chat_career(request):
    if request.method == 'GET':
        if request.user.is_staff:
            admins = User.objects.all()
        else:
            admins = User.objects.filter(groups__name='Dreams')
        if request.user.is_authenticated:
            groups = ChatGroup.objects.filter(members=request.user)
        else:
            groups = []
        return render(request, 'social/chat.html', {'admins': admins, 'groups': groups,})

@login_required(login_url="/login/")
def chat_lifestyle(request):
    if request.method == 'GET':
        if request.user.is_staff:
            admins = User.objects.all()
        else:
            admins = User.objects.filter(groups__name='Lifestyle')
        if request.user.is_authenticated:
            groups = ChatGroup.objects.filter(members=request.user)
        else:
            groups = []
        return render(request, 'social/chat.html', {'admins': admins, 'groups': groups,})

@login_required(login_url="/login/")
def chat_health(request):
    if request.method == 'GET':
        if request.user.is_staff:
            admins = User.objects.all()
        else:
            admins = User.objects.filter(groups__name='HealthEmo')
        if request.user.is_authenticated:
            groups = ChatGroup.objects.filter(members=request.user)
        else:
            groups = []
        return render(request, 'social/chat.html', {'admins': admins, 'groups': groups,})