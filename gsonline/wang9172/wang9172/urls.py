# _*_ encoding:utf-8 _*_
"""wang9172 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from users.views import LoginView, RegisterView, ActiveView, ForgetPassword, \
    ResetPassword, ModifyPwdView
from organization.views import OrgList
from wang9172.settings import MEDIA_ROOT

import xadmin

urlpatterns = [
    # xadmin url
    url(r'^xadmin/', xadmin.site.urls),
    # 首页
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    # 登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 注册页面
    url(r'^register/$', RegisterView.as_view(), name='register'),
    # 忘记密码
    url(r'^forget_pwd/$', ForgetPassword.as_view(), name='forget_pwd'),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),
    # 激活连接
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name='active'),
    # 重置连接
    url(r'^reset/(?P<active_code>.*)/$', ResetPassword.as_view(),
        name='reset'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 配置上传文件访问处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 批量配置课程机构
    url(r'^org/', include('organization.urls', namespace="org")),

    # 配置讲师
    url(r'^teacher/', include('organization.urls', namespace="teacher")),


    # 配置讲师
    url(r'^course/', include('courses.urls', namespace="course")),


    # 用户个人中心
    url(r'^user/', include('users.urls', namespace="user")),
]
