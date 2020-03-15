#!/usr/bin/env python
#coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import datetime
import setting,base64
from email.mime.image import MIMEImage

def SendEmail(Path,TestResultHTML,receiver,Title):
    sender = setting.sender
    username = setting.username
    password = base64.decodestring(setting.password)

    msgRoot = MIMEMultipart('alternative')

    text='This is an automated report,Please see the attachment for specific information!'
    EmailText = MIMEText(text, 'plain')

    msgRoot['Subject'] = Title
    msgRoot['from']='liangzhang.lin@genlot.com'
    msgRoot.attach(EmailText)
    #构造附件
    att = MIMEText(open(Path, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="'+TestResultHTML+'"'
    msgRoot.attach(att)


    smtp = smtplib.SMTP()
    smtp.connect('10.27.0.214')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

if __name__ =='__main__':
    pass



