# _*_ encoding:utf8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher


# Create your models here.


class Course(models.Model):
    id = models.IntegerField(primary_key=True,
                             verbose_name=u"课程表")
    name = models.CharField(max_length=64, verbose_name=u"课程名称")
    desc = models.CharField(max_length=256, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程描述")
    teacher = models.ForeignKey(Teacher, verbose_name='机构讲师')
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
    course = models.ForeignKey(CourseOrg, verbose_name=u"课程机构")
    course_category = models.CharField(max_length=12, choices=(
        ("qd", "前端开发"), ("hd", "后端开发"), ("xnh", "虚拟化")), verbose_name="课程类别",
                                       default='qd', blank=True, null=True)
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)


    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_nums(self):
        return self.lesson_set.all().count()

    def learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def get_comments(self):
        return self.coursecomments_set.all()[:6]


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=64, verbose_name=u"章节名")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        # 获取课程下的所有章节视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"课程")
    name = models.CharField(max_length=64, verbose_name=u"视频")
    url = models.CharField(max_length=64, verbose_name=u"访问地址", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    video_time = models.CharField(default=0, verbose_name=u"视频时长",
                                  max_length=24)

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=64, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",
                                verbose_name=u"资源文件", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
