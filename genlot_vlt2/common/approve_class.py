# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common.function import log_info
import time


class Approve(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        log_info(u"开始登录")
        self.p = self.driver.get("http://10.13.0.63:9191")
        username = 'chenxiaoming'
        password = '111111'

        un = self.driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input[1]')
        pw = self.driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input[2]')
        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/button')

        un.send_keys(username)
        pw.send_keys(password)
        login_btn.send_keys(Keys.ENTER)
        #点击站点管理系统，进入站点管理系统页面
        time.sleep(1)
        self.driver.find_element_by_xpath(u'//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]').click()

    def tearDown(self):
        pass
        #time.sleep(2)
        #self.driver.quit()