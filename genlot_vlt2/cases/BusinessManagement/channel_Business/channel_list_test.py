#coding=utf-8
import unittest
from time import sleep
from pages.home1_page import Home_Page
from  pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
from db.oracle_db import Oracle
from common.login_b import Login_B
from common.function import regex
import time
from common.function import log_info



class channel_list_test(unittest.TestCase):
    def setUp(self):
        '''初始化登陆'''
        a=Login_B()#登陆
        self.obh = Home_Page(a)#将登陆用的drvier赋给self.obh
        self.obh.jumpBusinessmanagement()#跳转到业务管理
        self.cc=jump_channel_list_page(a)#
        self.cc.jump()



    def test_query1(self):
        '''测试渠道列表全部查询，只校验总数是不是一样'''

        aa = self.cc.queryresult()
        aa1=str(aa[0])
        tt1=self.cc.page_num()
        print  aa1
        print tt1
        self.assertEqual(aa1,tt1)

    def test_query2(self):
        '''测试渠道列表第一行数据，并且校验,'''
        tt=self.cc.pageresult1()
        yy=self.cc.sql_page_result()
        tt1=tt[0].split('\n')
        print tt1
        print yy
        for i in range(5):
            self.assertEqual(tt1[i],yy[i])

    def test_resetting(self):
        '''测试重置按钮，输入框中前后对比'''
        channer_no = '123'
        channel_type = u'自营厅'
        channel_level = u'一级'
        person = u'张三'
        phone = '13570816554'
        startdate = '2019-12-17'
        enddate = '2019-12-17'
        self.cc.resetting(channer_no='123',channel_type=u'自营厅',channel_level=u'一级',person=u'张三',phone='13570816554',startdate='2019-12-17',enddate='2019-12-17')
        page_channel_no=self.cc.channel_no_isnull()
        page_channel_type=self.cc.channel_type_isnull()
        page_channel_level=self.cc.channel_level_isnull()
        page_person=self.cc.person_isnull()
        page_phone=self.cc.phone_isnull()
        page_startdate=self.cc.start_date_isnull()
        page_enddate = self.cc.end_date_isnull()
        self.assertNotIn(channer_no,page_channel_no)

    def test_export_now(self):
        '''测试导出当前'''
        t=self.cc.export_check()
        self.cc.export()
        time.sleep(5)
        t = self.cc.export_check()
        print type(t)
        self.assertEqual(t,'True')

    def test_export_all(self):
        '''测试导出所有'''
        t=self.cc.export_check()
        self.cc.export_all()
        time.sleep(5)
        t = self.cc.export_check()
        print type(t)
        self.assertEqual(t,'True')

    def test_view(self):
        '''查看，并对比数据'''
        tt1 = self.cc.querydetail()#二进制
        tt=self.cc.view_channel()#Unicode
        aa=tt1[0]
        for i in range(13):
            '''数据库拿出来的有float型，页面都是Unicode型，需要转化成str比较'''
            c=aa[i]
            c=str(c)
            self.assertEqual(c,tt[i])

    def tearDown(self):
        self.cc.close_browser()



if __name__ == '__main__':
    unittest.main()