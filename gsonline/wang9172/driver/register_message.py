# _*_ encoding:utf-8 _*_

__author__ = 'wang'

from apps.operation.models import UserMessage


def get_log_name(rigister_name):
    def get_message(name):
        def set_message(*args, **kwargs):
            user_message = UserMessage()
            name(*args, **kwargs)


        return set_message

    return get_message
