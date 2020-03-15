#-*- coding:utf-8 -*-
__author__ = 'lin'

from interface_common import commonfunc
from interface_common.commonfunc import *
from interface_common import request
import MySQLdb

# import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class mysql_db():
    def setUp(self):
        print_info(u'连接数据库。。。')
        self.Config_info =   config_info("数据库信息",0,1)
        host    =   self.Config_info[u'web_db_ip']
        user    =   self.Config_info[u'db_username']
        passwd  =   self.Config_info[u'db_password']
        db      =   self.Config_info[u'db_table']
        print_info('host:%s'%host)
        print_info('user:%s'%user)
        print_info('passwd:%s'%passwd)
        print_info('db:%s'%db)
        self.conn=MySQLdb.connect(host,user,passwd,db,charset='utf8')
        print_info(u'数据库连接完毕')

    #执行sql语句
    def run_sql(self,sql):
        try:
            a = []
            print_info(u'执行sql语句:%s'%sql)
            #cursor方法获取操作游标
            self.Cursor=self.conn.cursor()
            #execute方法执行SQL语句
            self.Cursor.execute(sql)
            #fetchall方法获取所有数据
            data=self.Cursor.fetchall()
            print_info(u'执行结果：%s'%data)
            for row in data:
                for data1 in row:
                    a.append(data1)
            print_info(a)
            return a

        except Exception,e:
            #回滚
            self.conn.rollback()
            print_info(e)

    def tearDown(self):
        wait_one_second()
        self.conn.close()
