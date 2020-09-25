from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('chat_friend/', views.chat_friend, name='chat_friend'),
    path('send_message/', views.send_message, name='send_message'),
]
