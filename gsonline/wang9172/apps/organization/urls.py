# _*_ encoding:utf:8 _*_

__author__ = 'wang'

from django.conf.urls import url, include
from .views import AskUser, OrgList

urlpatterns = [
    url(r'^user_ask/$', AskUser.as_view(), name="user_ask"),
    url(r'^list/$', OrgList.as_view(), name='list'),
]
