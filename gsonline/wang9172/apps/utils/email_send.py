# _*_ encoding:utf:8 _*_

__author__ = 'wang'

from users.models import EmailVerifyRecord
import random
from django.core.mail import send_mail
from wang9172.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_cord(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_tile = ""
    email_body = ""
    if send_type == "register":
        email_tile = "工商在线注册链接激活链接"
        email_body = "请点击下列链接激活你的账号:http://127.0.0.1:8000/active/%s" % (
            email_record)

        send_status = send_mail(email_tile, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    if send_type == "forget":
        email_tile = "工商在线密码重置连接"
        email_body = "请点击下列链接重置你的密码:http://127.0.0.1:8000/reset/%s" % (
            email_record)
        send_status = send_mail(email_tile, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_cord(randomlength=8):
    str = ''
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars)
    for i in range(randomlength):
        str += chars[random.randint(0, length - 1)]
    return str
