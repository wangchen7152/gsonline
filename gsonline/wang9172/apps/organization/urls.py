# _*_ encoding:utf:8 _*_

__author__ = 'wang'

from django.conf.urls import url
from .views import AskUser, OrgList, OrgHome, CourseHome, TeacherHome, DesHome

urlpatterns = [
    url(r'^user_ask/$', AskUser.as_view(), name="user_ask"),
    url(r'^list/$', OrgList.as_view(), name='list'),
    url(r'^home/(?P<org_id>\d+)$', OrgHome.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)$', CourseHome.as_view(), name='org_course'),
    url(r'^teacher/(?P<org_id>\d+)$', TeacherHome.as_view(),
        name='org_teacher'),
    url(r'^des/(?P<org_id>\d+)$', DesHome.as_view(), name='des'),
]
