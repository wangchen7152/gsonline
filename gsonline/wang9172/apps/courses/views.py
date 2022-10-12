# _*_ encoding:utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course, CourseResource
from operation.models import CourseComments as Comments
from operation.models import UserCourse
from utils.mixin_utils import LoginRequiredMixin


class CourseList(View):
    def get(self, request):
        all_course = Course.objects.all().order_by("-add_time")

        # 热门课程
        hot_courses = Course.objects.all().order_by("-click_num")[:3]

        # 是否存在搜索功能
        search_request = request.GET.get('keywords', '')
        if search_request:
            all_course = all_course.filter(
                Q(desc__icontains=search_request) |
                Q(name__icontains=search_request) |
                Q(detail__icontains=search_request)
            )

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


class CourseInfo(LoginRequiredMixin, View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        course_detail = Course.objects.get(id=course_id)
        course_detail.click_num += 1
        course_detail.save()
        # 查询是否用户已关联该课程
        user_course = UserCourse.objects.filter(user=request.user,
                                                course=course_detail)
        if not user_course:
            user_course = UserCourse(user=request.user, course=course_detail)
            user_course.save()

        # 根据课程ID获取所有学习该课程的用户
        all_UserCourses = UserCourse.objects.filter(course=course_detail)
        # 获取所有用户ID
        user_id = [course.user.id for course in all_UserCourses]
        # 根据用户ID将关联的课程均查出
        all_user_courses = UserCourse.objects.filter(user_id__in=user_id)
        # 获取所有课程的ID
        course_ids = [course.course.id for course in all_user_courses]
        # 根据id获取所有课程
        fav_course_list = Course.objects.filter(id__in=course_ids).order_by(
            "-click_num")[:5]
        all_resources = CourseResource.objects.filter(course=course_detail)
        return render(request, "course-video.html", {
            "course_detail": course_detail,
            "all_resources": all_resources,
            "fav_course_list": fav_course_list
        })


class CourseComments(LoginRequiredMixin, View):
    """
    课程评论信息
    """

    def get(self, request, course_id):
        course_detail = Course.objects.get(id=course_id)
        all_resources = CourseResource.objects.filter(course=course_detail)
        all_comments = Comments.objects.filter(course=course_id)
        return render(request, "course-comment.html", {
            "course_detail": course_detail,
            "all_resources": all_resources,
            "all_comments": all_comments
        })


class AddComments(View):
    """
    用户添加评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',
                                content_type='application/json')

        course_id = request.POST.get('course_id', 0)
        comment = request.POST.get('comments', '')
        if course_id > 0 and comment:
            com = Comments()
            course = Course.objects.get(id=course_id)
            com.course = course
            com.comments = comment
            com.user = request.user
            com.save()
            return HttpResponse("{'status': 'success', 'msg': '添加成功!'}",
                                content_type='application/json')
        else:
            HttpResponse("{'status':'fail','msg':'添加失败!'}",
                         content_type='application/json')
