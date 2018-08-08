# coding:utf-8
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    subject, from_email, to = '测试邮件', 'sender@qq.com', ['receive@qq.com']
    text_content = '欢迎使用 django'
    html_content = '<p> 欢迎访问<a href="http://www.baidu.com">www.baidu.com</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()