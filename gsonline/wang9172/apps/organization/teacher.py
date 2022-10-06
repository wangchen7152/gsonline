# _*_ encoding:utf-8 _*_
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UserFavorite
from .models import Teacher
from courses.models import Course as Course_teacher

__author__ = 'wang'


class TeacherList(View):
    def get(self, request):
        teachers = Teacher.objects.all()

        # 是否存在搜索功能
        search_request = request.GET.get('keywords', '')
        if search_request:
            teachers = teachers.filter(
                Q(name__icontains=search_request) |
                Q(work_company__icontains=search_request) |
                Q(points__icontains=search_request) |
                Q(need_know__icontains=search_request) |
                Q(work_positon__icontains=search_request)
            )

        # 点击人气排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == u"hot":
                teachers = teachers.order_by("-click_num")
            else:
                teachers = teachers.order_by("-student_num")

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

        # 进入页面首页查询是否收藏教师
        has_teacher_fav = False
        user = UserFavorite.objects.filter(user=request.user, fav_type=3,
                                           fav_id=teacher_id)
        if user:
            has_teacher_fav = True

        # 进入页面首页查询是否收藏机构
        has_fav_org = False

        user = UserFavorite.objects.filter(user=request.user, fav_type=2,
                                           fav_id=teacher.org.id)
        if user:
            has_fav_org = True

        # 讲师排行
        sort_teachers = Teacher.objects.all().order_by("-click_nums")[:3]
        return render(request, "teacher-detail.html", {
            "teacher": teacher,
            "all_Course": all_course,
            "sort_teachers": sort_teachers,
            "has_teacher_fav": has_teacher_fav,
            "has_fav_org": has_fav_org
        })
