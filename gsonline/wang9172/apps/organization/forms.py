# _*_ encoding:utf-8 _*_

__author__ = 'wang'

from django import forms
from operation.models import UserAsk

import re


class TestUserAskForm(forms):
    name = forms.CharField(required=True, max_length=64, min_length=2)
    phone = forms.CharField(required=True, max_length=11, min_length=11)
    course_name = forms.CharField(required=True, max_length=64, min_length=1)


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        正则验证手机号码
        """
        mobile = self.cleaned_data['mobile']
        re_mobile = "^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$"
        p = re.compile(re_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code="mobile_invalid")
