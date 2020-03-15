# -*- coding: utf-8 -*-
# author: lin


# import win32com.client
import time,traceback
import random
import logging
import xml.dom.minidom
import os,re,sys,json
import xlrd
import cx_Oracle
import re
import unittest

reload(sys)
sys.setdefaultencoding('utf-8')


class Commonfunc(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass




#定义日志函数
def initlog():
    logger = None
    logger = logging.getLogger()
    datefmt = "%Y-%m-%d %H:%M:%S"
    format_str = "[%(asctime)s]: %(levelname)s - %(message)s"
    formatter = logging.Formatter(format_str,datefmt)
    stream_handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return [logger,stream_handler]
#日记记录
def print_info(err_msg,level=logging.INFO):
    logger,stream_handler = initlog()
    logger.info(err_msg)
    stream_handler.flush()#确保所有的日志输出已经被刷新
    logger.removeHandler( stream_handler )#去掉log继承

def print_error(err_msg,level=logging.INFO):
    logger,stream_handler = initlog()
    logger.error(err_msg)
    stream_handler.flush()#确保所有的日志输出已经被刷新
    logger.removeHandler( stream_handler )#去掉log继承
#断言文本
def Equal_TEXT_Step(input_):
    b=input_+'成功跳转到指定步骤！'
    print_info(u'期望的断点为：%s'%b)
    return b
def Equal_TEXT_Apply(input_):

    b='[新增'+input_+']成功！'
    print_info(u'期望的断点为：%s'%b)
    return b

def Equal_Value(input_):
    b   =   input_
    print_info(u'期望的断点为：%s'%b)
    return b

def now_time():
    now_time=str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])+'_'+\
             str(time.localtime()[3]) + str(time.localtime()[4]) + str(time.localtime()[5])
    return now_time





#写站点编号
def write_station_to_txt(path,d):
    write_object=open(path,'w')
    write_object.write(d)
    write_object.close()
#读站点编号
def read_station_from_txt(path):
    read_object=open(path,'r')
    b=read_object.readlines()
    value=int(b[0])
    read_object.close()
    print_info(u'读取期号为：%s'%value)
    return value


def the_sum_of_error_and_fail(result_):
    # a='<HTMLTestRunner._TestResult run=1 errors=1236 failures=3>'
    a=str(result_)
    errors_value    =   re.compile(r'errors=\d*')
    failures_value    =  re.compile(r'failures=\d*')
    value =  re.compile(r'\d*\d')
    b   =   errors_value.findall(a)[0]
    c   =   failures_value.findall(a)[0]
    d   =   int(value.findall(b)[0])    +   int(value.findall(c)[0])
    return d


#获取当前工作目录
def current_path():
    file_catalog    =   str(os.getcwd())
    a=re.compile(r'\S*interface')
    current_path=str(a.findall(file_catalog)[0])

    return current_path

def check_and_kill_process(process_name):

    WMI = win32com.client.GetObject('winmgmts:')

    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)

    if len(processCodeCov) > 0:#判断操作
        print_info( '%s is exists' % process_name)
        os.system('taskkill /f /im %s'%process_name)
    else:
        print_info( '%s is not exists' % process_name)

def is_num(num):
        try:
            int(num)
            return True
        except ValueError:
            return False
    #读取excel行数据
def read_excel_row(value1,value2):
    # _path    =   current_path()
    _path =os.path.abspath(r'..\..')
    path=os.path.join(_path,'static\\interface_data\\test_data.xlsx')
    data=xlrd.open_workbook(path)#打开Excel文件读取数据
    table=data.sheet_by_name(value1)#通过索引顺序获取
    value=table.row_values(value2)#获取第N行的数据
    return value

    # 读取excel列数据
def read_excel_column(str1, str2):
    _path = current_path()
    path = os.path.join(_path, 'static\\data\\test_data.xlsx')
    data = xlrd.open_workbook(path)  # 打开Excel文件读取数据
    table = data.sheet_by_name(str1)  # 通过索引顺序获取
    value = table.col_values(str2)
    print value# 获取第N列的数据
    return value


    #读取excel生成字典
def config_info(value1,value2,value3):
    dict_config =   {}
    a=read_excel_column(value1,value2)
    b=read_excel_column(value1,value3)
    for i in range(1,len(a)):
        if is_num(a[i]):
            a[i]=int(a[i])
        if is_num(b[i]):
            b[i]=int(b[i])
        dict_config.update({'%s'%a[i]:'%s'%b[i]})
    dict_config_str =   json.dumps(dict_config,ensure_ascii=False)
    print_info('读取excel数据转字典：%s'%dict_config_str)
    return dict_config

#等待1秒
def wait_one_second():
    time.sleep(1)
#等待2秒
def wait_two_second():
    time.sleep(2)
#等待3秒
def wait_three_second():
    time.sleep(3)
#等待4秒
def wait_four_second():
    time.sleep(4)
#等待5秒
def wait_five_second():
    time.sleep(5)

def orcal_query(sql):
    user=(read_excel_row("数据库信息",3))[1]
    password=(read_excel_row("数据库信息",4))[1]
    ip=(read_excel_row("数据库信息",1))[1]
    dbname=(read_excel_row("数据库信息",5))[1]
    port=int((read_excel_row("数据库信息",2))[1])
    # print "user=%s"%user
    print '%s/%s@%s/%s'%(user,password,ip,dbname)
    conn = cx_Oracle.connect('%s/%s@%s/%s'%(user,password,ip,dbname))  # 这里的顺序是用户名/密码@oracleserver的ip地址/数据库名字
    # conn = cx_Oracle.connect('%s,%s,%s/%s' % (user, password,ip,dbname))
    # conn = cx_Oracle.connect('%s,%s,%s' % (user, password, ip))
    # print 11111111
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    # for re in rows:
    #     print re
    # cur.commit()
    cur.close()
    conn.close()
    return rows

def create_id():
    return int(time.time())

def create_email_id():
    a= str(int(time.time()))
    email=a+"@qq.com"
    return email
def create_phone_number():
    a= str(int(time.time()))
    phonenumber=a+random.choice("0123456789")
    return phonenumber

def phoneNORandomGenerator():
    # 随机生成手机号码
    prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

def refind(str,patton):
    aa=re.findall(patton,str)
    return  aa
if __name__ == '__main__':
    pass
