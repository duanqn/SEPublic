from django.conf.urls import *
import teacher_py.userinfo as userinfo

urlpatterns = [
    url(r'^$', userinfo.index),
    ]