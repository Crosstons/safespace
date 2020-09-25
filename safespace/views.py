from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse, JsonResponse
from Users import views
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User as AdminUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#def signup(request):
#    return render(request,'signupage.html')

def login_view(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/home/')

    else:
      form = AuthenticationForm()
    return render(request,'loginpage.html', {'form':form}) 

def logout_view(request):
    # if request.method == 'POST':
    logout(request)
    return redirect('/')

@login_required(login_url="/login/")
def home(request):
      return render(request, 'home_menu.html')   

def startingpage(request):
      return render(request, 'startingpage.html')

@login_required(login_url="/login/")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/login/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })

@login_required(login_url="/login/")
def get_user_by_id(request):
    pk = request.GET.get('pk')
    user = get_object_or_404(AdminUser, pk=pk)
    json_user = {
        'id': user.id,
        'username': user.username,
        'avatar': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png',
    }
    if not user:
        user = request.user
    return JsonResponse({'user': json_user})

@login_required(login_url="/login/")
def library(request):
    return render(request, 'library.html')   

@login_required(login_url="/login/")
def practices(request):
    return render(request, 'practices.html')   

def aboutus(request):
    return render(request, 'about_us.html')

def FAQS(request):
    return render(request, 'FAQS.html')
