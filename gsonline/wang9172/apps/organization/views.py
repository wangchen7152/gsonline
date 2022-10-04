# _*_encoding:utf-8 _*_
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from .models import City, CourseOrg, Teacher
from .forms import UserAskForm
from courses.models import Course


# Create your views here.


class OrgList(View):
    def get(self, request):
        all_org = CourseOrg.objects.all()
        all_city = City.objects.all()
        all_teacher = Teacher.objects.all()
        # 机构排名
        hot_orgs = all_org.order_by("-click_nums")[:3]

        # 去除筛选机构
        ct = request.GET.get("ct", "")
        city_id = request.GET.get('city', "")

        if ct:
            all_org = all_org.filter(catgory=ct)
            # 取出筛选城市
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        sort = request.GET.get("sort", "")
        if sort:
            if sort == u"students":
                all_org = all_org.order_by("-study_nums")
            else:
                all_org = all_org.order_by("-course_nums")

        # 排序
        org_nums = all_org.count()

        # 测试分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        objects = all_org
        p = Paginator(objects, 5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html",
                      {"all_org": orgs,
                       "all_city": all_city,
                       "all_teacher": all_teacher,
                       "org_nums": org_nums,
                       "city_id": city_id,
                       "catgory": str(ct),
                       "hot_orgs": hot_orgs,
                       "sort": sort,
                       })


class AskUser(View):
    """
    咨询相关操作
    """

    def post(self, request):
        ask_form = UserAskForm(request.POST)
        if ask_form.is_valid():
            ask_form.save(commit=True)
            return HttpResponse("{'status':'success'}",
                                content_type='application/json')
        else:
            return HttpResponse("{'status': 'failed', 'msg': '添加出错'}",
                                content_type='application/json')


class OrgHome(View):
    """
    机构s首页
    """

    def get(self, request, org_id):
        current = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:2]
        return render(request, "org-detail-homepage.html", {
            "all_courses": all_courses,
            "all_teacher": all_teacher,
            "course_org": course_org,
            "current": current
        })


class CourseHome(View):
    """
    机构课程页面
    """

    def get(self, request, org_id):
        current = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        return render(request, "org-detail-course.html", {
            "all_courses": all_courses,
            "current": current,
            "course_org": course_org,
        })


class TeacherHome(View):
    """
    机构教师页面
    """

    def get(self, request, org_id):
        current = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teacher = course_org.teacher_set.all()[:2]

        return render(request, "org-detail-teachers.html", {
            "all_teacher": all_teacher,
            "current": current,
            "course_org": course_org
        })


class DesHome(View):
    """
    机构课程页面
    """

    def get(self, request, org_id):
        current = "des"
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, "org-detail-desc.html", {
            "current": current,
            "course_org": course_org
        })
