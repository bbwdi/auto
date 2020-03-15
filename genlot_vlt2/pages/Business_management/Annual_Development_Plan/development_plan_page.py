#coding=utf-8
from pages.base_page import BasePage
import time
from common.function import regex,log_info
from db.oracle_db import Oracle
import os


aa='''渠道业务管理'''#进入渠道业务管理
bb='''年度发展计划'''
cc='''//*[@id="tab-3"]'''#计划汇总（地市）

class page(BasePage):
    def jump_planlist(self):
        '''跳转到计划列表'''
        self.get_element_by_xpath(aa).click()
        self.get_element_by_xpath(bb).click()
        time.sleep(1)

    def jump_plangather(self):
        '''跳转到计划汇总'''
        self.get_element_by_xpath(aa).click()
        self.get_element_by_xpath(bb).click()
        self.get_element_by_xpath(cc).click()
        time.sleep(1)

    def tt(self):
        pass