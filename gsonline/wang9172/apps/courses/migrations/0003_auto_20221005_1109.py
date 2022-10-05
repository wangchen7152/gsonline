# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2022-10-05 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_auto_20221004_1526'),
        ('courses', '0002_course_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.CharField(blank=True, choices=[('qd', '\u524d\u7aef\u5f00\u53d1'), ('hd', '\u540e\u7aef\u5f00\u53d1'), ('xnh', '\u865a\u62df\u5316')], default='qd', max_length=12, null=True, verbose_name='\u96be\u5ea6'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u673a\u6784\u8bb2\u5e08'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u8bfe\u7a0b\u673a\u6784'),
        ),
    ]
