#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.channelnewbuilt_page import New
from pages.Business_management.Business_Processing.relocate_page import Relocate
from pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class relocate(unittest.TestCase):
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_channelrelocate()
        self.dd=Relocate(a)


    def test_relocate(self):
        '''迁址,根据选取到的渠道编号来 判断第四位是否为0 0则为省渠道，不为0责任市渠道'''
        tt=self.dd.channel_no()
        kk=tt[3:4]
        if kk==0:
            self.dd.channeladdress()
        else:
            self.dd.channeladdress(2)
        # self.dd.title()
        # self.dd.channeladdress()
        self.dd.reason()
        self.dd.appendix()#附件
        self.dd.Submission()

    def test_relocate1(self):
        '''迁址到市'''
        self.dd.channel_no()
        # self.dd.title()
        self.dd.channeladdress(2)
        self.dd.reason()
        self.dd.appendix()#附件
        self.dd.Submission()


    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()