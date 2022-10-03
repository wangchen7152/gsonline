# _*_ encoding:utf:8 _*_


__author__ = 'wang'

import xadmin

from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'add_time', 'des']
    search_fields = ['name', 'add_time', 'des']
    list_filter = ['name', 'add_time', 'des']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                    'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image',
                     'address',
                     'city', 'add_time']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address',
                   'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year', 'work_company', 'work_positon',
                    'add_time', 'click_nums', 'fav_nums']
    search_fields = ['org', 'name', 'work_year', 'work_company', 'work_positon',
                     'add_time', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_year', 'work_company', 'work_positon',
                   'add_time', 'click_nums', 'fav_nums']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
