# _*_ encoding:utf8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


# Create your models here.


class Course(models.Model):
    id = models.IntegerField(primary_key=True,
                             verbose_name=u"课程表")
    name = models.CharField(max_length=64, verbose_name=u"课程名称")
    desc = models.CharField(max_length=256, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程描述")
    degree = models.CharField(max_length=12, choices=(
        ("cj", "初级"), ("zj", "中级"), ("gj", "高级")), verbose_name="难度")
    learn_time = models.IntegerField(default=0,
                                     verbose_name=u"学生时长，分钟数")
    student_num = models.IntegerField(verbose_name=u"学习人数")
    fav_num = models.IntegerField(verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"轮播图",
                              max_length=256)
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=64, verbose_name=u"章节名")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    course = models.ForeignKey(Lesson, verbose_name=u"课程")
    name = models.CharField(max_length=64, verbose_name=u"视频")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=64, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",
                                verbose_name=u"资源文件", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
