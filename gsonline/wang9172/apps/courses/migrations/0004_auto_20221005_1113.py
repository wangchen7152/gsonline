# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2022-10-05 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20221005_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_category',
            field=models.CharField(blank=True, choices=[('qd', '\u524d\u7aef\u5f00\u53d1'), ('hd', '\u540e\u7aef\u5f00\u53d1'), ('xnh', '\u865a\u62df\u5316')], default='qd', max_length=12, null=True, verbose_name='\u8bfe\u7a0b\u7c7b\u522b'),
        ),
    ]
