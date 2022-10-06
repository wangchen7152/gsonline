# _*_ encoding:utf8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称")
    birthday = models.DateField(max_length=32, null=True, verbose_name="生日")
    gender = models.CharField(max_length=6,
                              choices=(("male", u"男"), ("female", "女")),
                              default="female", verbose_name=u"性别")
    phone = models.CharField(max_length=11, null=True, verbose_name="手机号")
    image = models.ImageField(upload_to="image/%Y/%m",
                              default=u"image/default.png", max_length=100)
    address = models.CharField(max_length=64, verbose_name=u'地址', default='',
                               blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(verbose_name=u"邮箱")
    send_type = models.CharField(max_length=126, choices=(
        ("register", "注册"), ("forget", "找回密码")),
                                 verbose_name=u"验证码类型")
    send_time = models.DateField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code


class Banner(models.Model):
    title = models.CharField(max_length=124, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name="超链接地址")
    index = models.IntegerField(default=1000, verbose_name="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
