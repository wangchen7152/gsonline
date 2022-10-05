# _*_ encoding:utf-8 _*_

__author__ = 'wang'


from django.conf.urls import url
from .views import CourseList, CourseDetail, CourseInfo, CourseComments, \
    AddComments

urlpatterns = [
    url(r'^list/$', CourseList.as_view(), name="course_list"),
    url(r'^course/(?P<course_id>\d+)$', CourseDetail.as_view(), name="detail"),
    url(r'^info/(?P<course_id>\d+)$', CourseInfo.as_view(), name="info"),
    url(r'^comments/(?P<course_id>\d+)$', CourseComments.as_view(),
        name="comments"),
    url(r'^add_comments/$', AddComments.as_view(), name="add_comments")
]
