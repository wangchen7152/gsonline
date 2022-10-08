# _*_ encoding:utf-8 _*_
import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend

from utils.mixin_utils import LoginRequiredMixin
from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetPwd, ResetPwd, \
    UploadImageForm, ResetEmail
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email


# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            raise e


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(
            request.POST
        )
        if login_form.is_valid():
            user_name = request.POST.get("username")
            pass_word = request.POST.get("password")
            user = authenticate(username=user_name, password=pass_word)
            is_active = UserProfile.objects.get(username=user.username).is_active
            if user is not None:
                if is_active == True:
                    login(request, user)
                    return render(request, "index.html", {'user': user})
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html",
                              {"msg": "用户名密码错误", "login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html",
                      {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if not UserProfile.objects.filter(email=request.POST.get("email")):
            if register_form.is_valid():
                user_email = request.POST.get("email")
                pass_word = request.POST.get("password")
                user_profile = UserProfile()
                user_profile.email = user_email
                user_profile.password = make_password(pass_word)
                send_register_email(user_email)
                try:
                    user_profile.save()
                except:
                    pass
                return render(request, "login.html", {"msg": "用户注册成功，请去邮箱确认激活"})
            else:
                return render(request, "register.html",
                              {"register_form": register_form})
        else:
            return render(request, "register.html", {"msg": "用户已经注册"})


class ActiveView(View):

    @classmethod
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.get(code=active_code)
        if all_record:
            email = all_record.email
            user = UserProfile.objects.get(email=email)
            user.is_active = True
            user.save()
        else:
            return render(request, "active_file.html")
        return render(request, "login.html")


class ForgetPassword(View):
    def get(self, request):
        return render(request, "forgetpwd.html", {})

    def post(self, request):
        forget_form = ForgetPwd(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email")
            user = UserProfile.objects.get(email=email)
            if user:
                send_register_email(email, "forget")
                return render(request, "send_success.html")
            else:
                return render(request, "forgetpwd.html",
                              {"msg": "当前用户未注册，请重新注册"})
        else:
            return render(request, "forgetpwd.html",
                          {"forget_form": forget_form})


class ResetPassword(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.get(code=active_code)
        if all_record:
            email = all_record.email
            return render(request, "password_reset.html", {"email": email})

        else:
            return render(request, "active_file.html")


class ModifyPwdView(View):
    def post(self, request):
        reset_pwd = ResetPwd(request.POST)
        email = request.POST.get("email")
        if reset_pwd.is_valid():
            password1 = request.POST.get("password")
            password2 = request.POST.get("password2")
            if password1 != password2:
                return render(request, "password_reset.html",
                              {"msg": "两次输入的密码不能相同"})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(password1)
                user.save()
                return render(request, "login.html", {"msg": "用户密码修改成功,请重新登录"})

        else:
            return render(request, "password_reset.html",
                          {"email": email, "reset_form": reset_pwd})


class UserCenter(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        return render(request, 'usercenter-info.html', {
            "user": user
        })


class UploadUserImage(LoginRequiredMixin, View):
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES,
                                     instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse('{"status":"success","msg":"头像修改成功"}',
                                content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"头像修改失败"}',
                                content_type='application/json')


class ChangePwdView(LoginRequiredMixin, View):
    """
    个人中心修改用户密码
    """

    def post(self, request):
        reset_pwd = ResetPwd(request.POST)
        if reset_pwd.is_valid():
            password_old = request.POST.get("password_old")
            if authenticate(username=request.user.username,
                            password=password_old):
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password_old != password1 or password_old != password2:
                    if password1 != password2:
                        return HttpResponse('{"status":"fail","msg":"两次密码不同"}',
                                            content_type='application/json')
                    else:
                        user = request.user
                        user.password = make_password(password1)
                        user.save()
                        return HttpResponse(
                            '{"status":"success","msg":"修改成功，请重新登录"}',
                            content_type='application/json')
                else:
                    return HttpResponse(
                        '{"status":"success","msg":"修改的密码不能同原密码一致"}',
                        content_type='application/json')

            else:
                return HttpResponse('{"status":"fail","msg":"原密码错误"}',
                                    content_type='application/json')

        else:
            return HttpResponse(json.dumps(reset_pwd.errors),
                                content_type='application/json')


class LogOutView(View):
    def get(self, request):
        logout(request=request)
        return render(request, 'index.html', {

        })


class UserCenterSendEmail(LoginRequiredMixin, View):
    def post(self, request):
        email = request.POST.get('email', '')
        if not UserProfile.objects.filter(email=email):
            email_form = ResetEmail(request.POST)
            if email_form.is_valid():
                status_check = send_register_email(email, "change_email")
                if status_check == True:
                    return HttpResponse(
                        '{"status":"success","msg":"邮箱验证码发送成功"}',
                        content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail","msg":"邮箱发送失败"}',
                                        content_type='application/json')

            else:
                return HttpResponse('{"status":"fail","msg":"邮箱不符合规格"}',
                                    content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"邮箱已存在"}',
                                content_type='application/json')


class CheckCode(LoginRequiredMixin, View):
    def post(self, request):
        new_email = request.POST.get('email', '')
        new_code = request.POST.get("code", "")
        email_code = EmailVerifyRecord.objects.get(email=new_email,
                                                   code=new_code,
                                                   send_type=u'change_email').code
        if email_code:
            user = UserProfile.objects.get(id=request.user.id)
            user.email = new_email
            user.save()
            return HttpResponse(
                '{"status":"success","msg":"邮箱验证成功，新邮箱地址已修改"}',
                content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"验证码验证错误"}',
                                content_type='application/json')
