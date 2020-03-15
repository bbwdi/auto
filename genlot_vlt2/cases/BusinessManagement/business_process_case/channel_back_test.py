#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.channel_back_page import Back
from pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class back(unittest.TestCase):
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_channelback()
        self.dd=Back(a)


    def test_backmachine(self):
        '''退机'''
        tt=self.dd.channel_no()
        self.dd.Resources()
        self.dd.reason()
        self.dd.appendix()
        self.dd.Submission()

    def test_backmachine1(self):
        '''退机输入后取消'''
        tt=self.dd.channel_no()
        self.dd.Resources()
        self.dd.reason()
        self.dd.appendix()
        self.dd.cancel()


    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()