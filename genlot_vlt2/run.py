#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
from setting import *
import unittest
import time,os
from selenium import  webdriver

#======新增加========
import smtplib
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def create__browser_driver(b='gc'):
    try:
        if b == 'gc':
            dv = webdriver.Chrome()
        elif b == 'ff':
            dv = webdriver.Firefox()
        elif b == 'ie':
            dv = webdriver.Ie()
        else:
            pass
        return dv
    except BaseException:
        pass
#=================================================新增加=======================================================

#====================定义发送邮件====================
def send_mail(file_new):
    host = 'genlot.com'
    port ='25'
    from_user = 'xiaolin.zou@genlot.com'  # 发送这邮箱
    passwd = '666888zxl'     # 密码--SMTP授权码
    to_user = [u'568505593@qq.com',u'baoming.zheng@genlot.com',
               u'lin.duan@genlot.com',u'henglin.wu@genlot.com',
               u'ranfeng.gong@genlot.com',u'zhengxin.huang@genlot.com',
               u'xiaoming.chen@genlot.com',u'yansong.li@genlot.com',
               u'weipeng.gao@genlot.com',u'jie.liu@genlot.com',
               u'2489039801@qq.com',u'657365253@qq.com',
               u'yonghong.zhou@genlot.com',u'nanshan.chen@genlot.com'
               ] # 接收邮箱
    #to_user = u'568505593@qq.com'  # 接收邮箱

    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    #msg = MIMEText(mail_body,'html','utf-8')
    #创建一个带附件的实例
    msg=MIMEMultipart()
    msg['Subject'] = Header('自动化测试报告','utf-8')
    msg['From']=formataddr(["小林",from_user])  # 发件人邮箱昵称、发件人邮箱账号
    message = MIMEMultipart()
    #构造附件
    attach_file=MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    attach_file["Content-Type"] = 'application/octet-stream'
    attach_file["Content-Disposition"] = 'attachment; filename="report.html"'#filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(attach_file)
    msg.attach(MIMEText(mail_body,'html','utf-8'))#邮件正文内容
    try:
        #smtp = smtplib.SMTP_SSL(host,port)
        smtp = smtplib.SMTP(host,port)
        smtp.login(from_user,passwd)
        smtp.sendmail(from_user,to_user,msg.as_string())
        smtp.quit()
        print(u'邮件发送成功！')
    except  smtplib.SMTPException as e:
        print(u'邮件发送失败！')
        print(e)

def new_report(testReport):
    '''读取最新的报告'''
    lists = os.listdir(testReport)
    lists.sort(key = lambda fn:os.path.getmtime(testReport + fn))
    file_new = os.path.join(testReport,lists[-1])
    return file_new

#=================================================新增加=======================================================


if __name__ == '__main__':
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename =html_report + u"test_result_" + now + u".html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(fp, title=u"测试报告", description = u"Chrome测试结果")
    discover = unittest.defaultTestLoader.discover(case_path,pattern=u"*test.py",top_level_dir=case_path)
    runner.run(discover)
    #新增加
    fp.close()
    file_path = new_report(html_report)
    send_mail(file_path)
