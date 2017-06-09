from django.conf.urls import include, url
from .views import *
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^dashboard/$',index,name='dashboard'),
    url(r'^update/$',update_complaint,name='update'),
]