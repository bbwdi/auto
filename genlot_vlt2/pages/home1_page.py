#coding=utf-8
from selenium import webdriver
# from common.base_class import Test
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from db.oracle_db import Oracle
from common.function import log_info
import os


user = "admin"
password = "123456"
userinput="//input[@placeholder='请输入用户账号']"
passwordinput="//input[@placeholder='请输入用户密码']"
button='''//*[@id="app"]//span[text()='登录']'''
jumpBusinessmanagement1='''//*[@id="app"]//dd[text()='业务管理']'''#进入业务管理
jumpBusinessoperation1='''//*[@id="app"]//dd[text()='业务运营']'''#进入业务运营
jumpBusinessmonitoring1='''//*[@id="app"]//dd[text()='业务监控']'''#进入业务监控
jumpsystemmanagement1='''//*[@id="app"]//dd[text()='系统管理']'''#进入系统管理
jumpCustomersystem1='''//*[@id="app"]//dd[text()='客服系统']'''#进入客服系统
user_name='''//*[@id="app"]//div//span/span[@class='user-name']'''
page_nums='''//*[@id="main"]//span[1][contains(text(),'共 ')]'''

class Home_Page(BasePage):
    def jumpBusinessmanagement(self):
        '''进入业务管理'''
        self.get_element_by_xpath(jumpBusinessmanagement1).click()
        time.sleep(1)


    def jumpBusinessoperation(self):
        '''进入业务运营'''
        self.get_element_by_xpath(jumpBusinessoperation1).click()
        time.sleep(1)

    def jumpBusinessmonitoring(self):
        '''进入业务监控'''
        self.get_element_by_xpath(jumpBusinessmonitoring1).click()
        time.sleep(1)


    def jumpsystemmanagement(self):
        '''进入系统管理'''
        self.get_element_by_xpath(jumpsystemmanagement1).click()
        time.sleep(1)


    def jumpCustomersystem(self):
        '''进入客服系统'''
        self.get_element_by_xpath(jumpCustomersystem1).click()
        time.sleep(1)

    def ins(self):
        '''根据登陆用户拿相应的组织机构'''
        time.sleep(3)
        name=self.get_element_by_xpath(user_name).text
        user_ins_sql = ''' SELECT t.ins_id  from T_USER_INS t left join T_USER_INFO  k on t.user_id=k.user_id where  k.account='%s' '''%name
        kk=Oracle().run_sql_list(user_ins_sql)
        log_info(kk)
        print "kk=%s"%kk
        kk1=kk[0]
        log_info(kk1)
        return kk1

    def page_num(self):
        kk=self.get_element_by_xpath(page_nums).text
        log_info(kk)
        tt=regex("\d+",kk)
        log_info(tt)
        return  tt


if __name__=='__main__':
    pass
