from django.contrib import admin
from django.conf.urls import url
from.import views

urlpatterns = [
    #url(r'^signup/add_user/', views.add_user),
    url(r'^signup/$',views.signup),
]
