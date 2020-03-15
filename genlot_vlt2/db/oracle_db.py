#coding=utf-8
import cx_Oracle
from common.function import log_info
import sys
import setting
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

class Oracle():
    def __init__(self):
        log_info(u'连接数据库。。。')
        self.conn=cx_Oracle.connect(setting.connetion_info, encoding = "UTF-8")
        log_info(u'数据库连接完毕')

    #执行sql语句
    def run_sql(self, sql):
        try:
            a = []
            log_info(u'执行sql语句:%s'%sql)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            #print data
            for row in data:
                for data1 in row:
                    a.append(data1)
            log_info(a)
            return a

        except Exception,e:
            #回滚
            self.conn.rollback()
            log_info(e)

    def get_data(self,sql):
        try:
            log_info(u'执行sql语句:%s'%sql)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception,e:
            #回滚
            self.conn.rollback()
            log_info(e)


    def sql_delete(self,sql):
            log_info(u'执行sql语句:%s'%sql)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            self.cursor.close()
            self.conn.commit()

    def disconnect(self):
        self.conn.close()

#执行sql语句
    def run_sql_list(self, sql):
        try:
            a = []
            log_info(u'执行sql语句:%s'%sql)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print "data=%s"%data
            for row in data:
                for data1 in row:
                    a.append(data1)
            log_info(a)
            # self.cursor.close()
            return a

        except Exception,e:
            #回滚
            self.conn.rollback()
            log_info(e)
            # self.cursor.close()

    def run_sql_dir(self, sql):
        try:
            a = []
            log_info(u'执行sql语句:%s'%sql)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print "data=%s"%data
            # self.cursor.close()
            return data
        except Exception,e:
            #回滚
            self.conn.rollback()
            log_info(e)
            # self.cursor.close()
    def run_sql_LOB(self, sql):
        try:
            a = []
            log_info(u'执行sql语句:%s'%sql)
            self.cursor = self.conn.cursor()
            tt=self.cursor.execute(sql)
            for row in tt:
                ss=row[0].read()
                print "ss=%s"%ss
                print type(ss)
                a.append(ss)
            return a
        except Exception,e:
            #回滚
            self.conn.rollback()
            log_info(e)
            # self.cursor.close()



if __name__=="__main__":
    pass
    # sql = 'select * from tms_inspector limit 1'
    # t = Oracle().run_sql(sql)
    # print t
