# _*_ encoding:utf-8 _*_

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UserFavorite
from .models import Course


class CourseList(View):
    def get(self, request):
        all_course = Course.objects.all().order_by("-add_time")

        # 热门课程
        hot_courses = Course.objects.all().order_by("-click_num")[:3]

        # 排序
        sort = request.GET.get('sort', "")
        if sort == 'hot':
            all_course = all_course.order_by('-click_num')
        else:
            all_course = all_course.order_by('-student_num')

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 5, request=request)
        all_course = p.page(page)
        return render(request, 'course-list.html', {
            "all_course": all_course,
            "sort": sort,
            "hot_courses": hot_courses,
        })


class CourseDetail(View):
    def get(self, request, course_id):
        course_detail = Course.objects.get(id=course_id)
        course_detail.click_num += 1
        course_detail.save()

        tag = course_detail.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:2]
        else:
            relate_courses = []
        return render(request, "course-detail.html", {
            "course_detail": course_detail,
            "relate_courses": relate_courses,
        })
