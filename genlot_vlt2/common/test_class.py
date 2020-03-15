#coding:utf-8

import time
import datetime
from login_b import Login_B
import unittest
from selenium import webdriver
from pages.home1_page import Home_Page
from selenium.webdriver.support.select import Select



#
# log_info(u"校验流程是否执行成功")
#
# db = Mysql()
# sql='''select is_finished from xj_station_starlevel_subsidy  '''
# result = db.run_sql(sql)
#
#
# #计算昨天和明天的日期
#
# today = datetime.date.today()
# yestoday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)
#
#
# def count_time(self,count):
#     today = datetime.date.today()
#     new_day = today + datetime.timedelta(days=count)
#     return new_day
class a(unittest.TestCase):
    def test(self):
        a=Login_B()
        tt=Home_Page(a)
        # tt.jumpBusinessmanagement()
        tt.get_element_by_xpath('''//*[@id="app"]//dl/dd[text()='业务运营']''').click()
        # self.a.find_element_by_xpath('''//*[@id="app"]//dl/dd[text()='业务运营']''').click()
        time.sleep(1)
        tt.get_element_by_xpath('''//*[@id="app"]//span[text()='角色管理']''').click()
        time.sleep(1)
        tt.get_element_by_xpath('''//*[@id="app"]//span[text()='角色列表']''').click()
        time.sleep(1)
        kk=tt.get_element_by_xpath('''//*[@id="app"]//input[@placeholder='请选择用户角色']''')
        Select(kk).select_by_index(4)










