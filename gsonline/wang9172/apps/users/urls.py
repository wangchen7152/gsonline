# _*_ encoding:utf-8 _*_

__author__ = 'wang'

from django.conf.urls import url
from .views import UserCenter, UploadUserImage, ChangePwdView, \
    UserCenterSendEmail, CheckCode

urlpatterns = [
    url(r'^user_center/(?P<user_id>\d+)$', UserCenter.as_view(),
        name='user_center'),
    # 用户头像上传
    url(r'^image/upload/$', UploadUserImage.as_view(), name='image_upload'),
    # 用户个人中心修改密码
    url(r'^update/pwd/$', ChangePwdView.as_view(), name='update_pwd'),
    # 用户个人中心修改密码
    url(r'^send/email/$', UserCenterSendEmail.as_view(), name='send_email'),
    # 用户个人往邮箱发送验证码
    url(r'^check/code/$', CheckCode.as_view(), name='check_code'),
]
