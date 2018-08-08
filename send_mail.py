# coding:utf-8
import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        '主题',
        '邮件内容',
        'sender@qq.com',    #发送方
        ['receive@qq.com'],#接收方
    )