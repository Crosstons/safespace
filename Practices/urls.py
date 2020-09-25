from django.conf.urls import url,include
from django.conf.urls import url
from.import views


urlpatterns = [

  url(r'^practices/$',views.practices, name="list"),
  url(r'^practices/(?P<slug>[\w-]+)/$', views.practices_details, name="detail"),
] 



 