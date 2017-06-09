from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^signin/$',user_login,name="login"),
    url(r'^signup/$',user_signup,name="signup"),
    url(r'^logout/$',user_logout,name="logout"),
]
