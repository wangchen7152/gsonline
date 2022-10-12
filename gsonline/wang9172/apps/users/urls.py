# _*_ encoding:utf-8 _*_

__author__ = 'wang'

from django.conf.urls import url
from .views import UserCenter, UploadUserImage, ChangePwdView, \
    UserCenterSendEmail, CheckCode, UpdateUserInfo, UserCourseDetail, \
    UserFavOrg, UserFavCourse, UserFavTeacher, MyMessage

urlpatterns = [
    url(r'^center/(?P<user_id>\d+)$', UserCenter.as_view(),
        name='user_center'),
    # 用户头像上传
    url(r'^image/upload/$', UploadUserImage.as_view(), name='image_upload'),
    # 用户个人中心修改密码
    url(r'^update/pwd/$', ChangePwdView.as_view(), name='update_pwd'),
    # 用户个人中心修改密码
    url(r'^send/email/$', UserCenterSendEmail.as_view(), name='send_email'),
    # 用户个人往邮箱发送验证码
    url(r'^check/code/$', CheckCode.as_view(), name='check_code'),
    # 个人中心修改用户信息
    url(r'^change/info/$', UpdateUserInfo.as_view(), name='change_info'),
    # 个人中心修改用户信息
    url(r'^course/$', UserCourseDetail.as_view(), name='course'),
    # 用户收藏机构
    url(r'^fav/org/$', UserFavOrg.as_view(), name='fav_org'),
    # 用户收藏的课程
    url(r'^fav/course/$', UserFavCourse.as_view(), name='fav_course'),
    # 用户收藏的老师
    url(r'^fav/teacher/$', UserFavTeacher.as_view(), name='fav_teacher'),
    # 个人中心-我的信息
    url(r'^my/message/$', MyMessage.as_view(), name='my_message'),
]
