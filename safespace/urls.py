from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from social import views as social_views
from django.conf.urls.static import static #todo delete
from django.urls import path
from Practices import views as practices_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Users.urls')),
    url(r'^login/$',views.login_view),
    url(r'^home/$',views.home),
    url(r'^$', views.startingpage),
    url(r'^changepassword/', views.change_password),
    url(r'^logout/$', views.logout_view),
    url(r'^library/$',views.library),
    url(r'^about_us/$',views.aboutus),
    url(r'^', include('Practices.urls')),
    url(r'^faqs/$', views.FAQS),


    path('get_user_by_id/', views.get_user_by_id, name='get_user_by_id'),
    # Chat
    path('chat/', social_views.chat, name='chat'),
    path('chat_career/', social_views.chat_career, name='chat_career'),
    path('chat_lifestyle/', social_views.chat_lifestyle, name='chat_lifestyle'),
    path('chat_health/', social_views.chat_health, name='chat_health'),
    path('social/', include('social.urls'), name='scoal'),
    # Web-Push
    path('webpush/', include('webpush.urls')),

    # Reset-Password

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "passwordreset.html"),
    name="reset_password"),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "passwordreset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "passwordreset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "passwordreset_done.html"), 
    name="password_reset_complete"),

    # Reset Complete
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #todo delete