# _*_ encoding:utf-8 _*_

__author__ = 'wang'
# _*_ encoding:utf:8 _*_


from django.conf.urls import url
from .views import CourseList, CourseDetail

urlpatterns = [
    url(r'^list/$', CourseList.as_view(), name="course_list"),
    url(r'^course/(?P<course_id>\d+)$', CourseDetail.as_view(), name="detail")
]
