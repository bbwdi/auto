# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common.function import log_info
import setting
import time


class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # log_info(u"开始登录")
        # self.p = self.driver.get("http://10.6.0.203:8888/#/login")
        # username = u'zxl_test'
        # password = u'123456'
        #
        # time.sleep(5)
        # un = self.driver.find_element_by_xpath('''//input[starts-with(@placeholder,'请输入用户账号')]''')
        # pw = self.driver.find_element_by_xpath('''//input[starts-with(@placeholder,'请输入用户密码')]''')
        #
        # login_btn = self.driver.find_element_by_xpath('''//span[contains(text(),'登录')]''')
        #
        # # un.clear()
        # # pw.clear()
        # un.send_keys(username)
        # pw.send_keys(password)
        # login_btn.click()
        # time.sleep(5)

    def tearDown(self):
        #pass
        #防止过快关掉浏览器
        #time.sleep(2)
        self.driver.quit()

