# _*_encoding:utf8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"城市名称")
    add_time = models.DateField(datetime.now)
    des = models.CharField(max_length=200, verbose_name="u描述")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    catgory = models.CharField(default="pxjg", max_length=24, choices=(
        ("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")), verbose_name=u"机构类型")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"机构封面图",
                              max_length=256)
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    city = models.ForeignKey(City, verbose_name=u"所在城市")
    add_time = models.DateField(datetime.now)
    study_nums = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")

    class Meta:
        verbose_name = u"机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_year = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=64, verbose_name=u"工作公司")
    work_positon = models.CharField(max_length=64, verbose_name=u"工作职位")
    add_time = models.DateField(datetime.now)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"头像",
                              max_length=256, default='')
    year = models.IntegerField(verbose_name="年龄", default=66)
    points = models.CharField(max_length=128, verbose_name="教学特点", blank=True)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
