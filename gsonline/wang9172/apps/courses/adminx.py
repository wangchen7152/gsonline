# _*_ encoding:utf:8 _*_

__author__ = 'wang'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from courses.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseAdmin(object):
    # 列表展示
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time',
                    'student_num', 'fav_num', 'image', 'get_lesson_nums',
                    'go_to']
    # 可搜索内容
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time',
                     'student_num', 'fav_num', 'image']

    # 列表过滤
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time',
                   'student_num', 'fav_num', 'image']
    # 默认排序
    ordering = ['-click_num']
    # 设置只读字段
    readonly_fields = ['click_num']
    # 设置编辑页面不展示编辑列
    exclude = ['fav_num']
    # 一个model两个模型
    inlines = [LessonInline]
    # 设置列表页直接编辑内容
    list_editable = ['degree', 'desc']
    # 设置页面刷新,秒为单位
    refresh_times = [3, 10]
    # 富文本编辑器
    style_fields = {"detail": "ueditor"}

    def queryset(self):
        ba = super(CourseAdmin, self).queryset()
        ba = ba.filter(is_banner=False)
        return ba

    def save_model(self):
        # 保存课程统计机构课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.couse_org
            course_org.course_nums = CourseOrg.objects.filter(
                course_org=course_org).count()
            course_org.save()


class BannerAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time',
                    'student_num', 'fav_num', 'image']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time',
                     'student_num', 'fav_num', 'image']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time',
                   'student_num', 'fav_num', 'image']
    ordering = ['-click_num']
    readonly_fields = ['click_num']
    inlines = [LessonInline]
    list_editable = ['degree', 'name']

    def queryset(self):
        ba = super(BannerAdmin, self).queryset()
        ba = ba.filter(is_banner=True)
        return ba


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
xadmin.site.register(BannerCourse, BannerAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
