#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.channelAddmachine_page import Add
from pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class add(unittest.TestCase):
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_channelAddmachine()
        self.dd=Add(a)


    def test_addmachine(self):
        '''新增机器'''
        tt=self.dd.channel_no()
        self.dd.title(tt)
        self.dd.Resources()
        self.dd.reason()
        self.dd.appendix()
        self.dd.Submission()

    def test_addmachine1(self):
        '''新增机器输入完后点取消'''
        tt=self.dd.channel_no()
        self.dd.title(tt)
        self.dd.Resources()
        self.dd.reason()
        self.dd.appendix()
        self.dd.cancel()

    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()