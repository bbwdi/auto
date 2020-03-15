#!/usr/bin/env python
#coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import datetime
from email.mime.image import MIMEImage


def send_mail(Path, TestResultHTML, receiver, Title):
    sender = 'xiaolin.zou@genlot.com'
    username = 'xiaolin.zou@genlot.com'
    password = '666888zxl'
    # #
    # sender = 'llzllx1988@126.com'
    # username = 'llzllx1988@126.com'
    # password = 'Aaron1988'


    msgRoot = MIMEMultipart('alternative')

    text='This is an automated report,Please see the attachment for specific information!'
    EmailText = MIMEText(text, 'plain')

    msgRoot['Subject'] = Title
    msgRoot['from']='xiaolin.zou@genlot.com'
    # msgRoot['to']='319507751@qq.com'
    # msgRoot['from']='llzllx1988@126.com'

    # text = "Hi,all\nThis is the automation report"
    # EmailText = MIMEText(text, 'plain')
    msgRoot.attach(EmailText)
    #构造附件
    att = MIMEText(open(Path, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="'+TestResultHTML+'"'
    msgRoot.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect('mail.genlot.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()
        print(u'邮件发送成功！')
    except  smtplib.SMTPException as e:
        print(u'邮件发送失败！')
        print(e)

if __name__ =='__main__':
    Path=r'F:\Henan_Xinxi_Web_Auto\scripts\run_report\SuiCai_Error_Report.txt'
    TestResultHTML='TestResultHTML'+'.html'
    receiver='624129005@qq.com'
    Title='TestResultHTML'
    send_mail(Path,TestResultHTML,receiver,Title)



