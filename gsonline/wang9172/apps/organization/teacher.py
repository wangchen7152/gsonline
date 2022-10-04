# _*_ encoding:utf_8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Teacher
from courses.models import Course as Course_teacher

__author__ = 'wang'


class TeacherList(View):
    def get(self, request):
        teachers = Teacher.objects.all()

        # 点击人气排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == u"hot":
                teachers = teachers.order_by("-click_nums")

        sort_teachers = Teacher.objects.all().order_by("-click_nums")[:3]

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(teachers, 5, request=request)
        teachers = p.page(page)

        # 判断页面按钮
        active = 'teacher'
        return render(request, "teachers-list.html", {
            "teachers": teachers,
            "sort_teachers": sort_teachers,
            "active": active
        })


class TeacherDetail(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        # Course_org = Teacher.objects.get(org=teacher.org)
        all_course = Course_teacher.objects.filter(teacher=teacher)

        # 讲师排行
        sort_teachers = Teacher.objects.all().order_by("-click_nums")[:3]
        return render(request, "teacher-detail.html", {
            "teacher": teacher,
            "all_Course": all_course,
            "sort_teachers": sort_teachers
        })
