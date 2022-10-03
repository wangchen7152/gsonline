# _*_ encoding:utf:8 _*_

__author__ = 'wang'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=3)
    password = forms.CharField(required=True, max_length=16, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=32)
    password = forms.CharField(required=True, max_length=32)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误或已失效"})


class ForgetPwd(forms.Form):
    email = forms.EmailField(required=True, max_length=32)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误或已失效"})


class ResetPwd(forms.Form):
    password = forms.CharField(required=True, min_length=3)
    password2 = forms.CharField(required=True, min_length=3)
