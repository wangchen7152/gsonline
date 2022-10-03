# _*_ encoding:utf:8 _*_

__author__ = 'wang'

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time',
                    'student_num', 'fav_num', 'image']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time',
                     'student_num', 'fav_num', 'image']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time',
                   'student_num', 'fav_num', 'image']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name', 'add_time']
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name', 'add_time']
    list_filter = ['course', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', "add_time"]
    search_fields = ['course', 'name', 'download', "add_time"]
    list_filter = ['course', 'name', 'download', "add_time"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
