# _*_ encoding:utf-8 _*_

__author__ = 'wang'

from django.conf.urls import url
from .views import UserCenter


urlpatterns = [
    url(r'^user_center/(?P<user_id>\d+)$', UserCenter.as_view(),
        name='user_center'),
]
