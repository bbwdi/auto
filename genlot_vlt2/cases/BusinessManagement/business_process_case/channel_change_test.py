#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.ChannelChange_page import Change
from pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class change(unittest.TestCase):
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_channelchange()
        self.dd=Change(a)


    def test_change(self):
        '''渠道变更'''
        zz=self.dd.channel_no()
        self.dd.switch(1)#基本信息开启编辑
        palce=self.dd.place1()
        area=self.dd.areainput()
        zhanshi=self.dd.zhanshi()
        kailimit=self.dd.kailimit()
        shiwanlimit=self.dd.shiwanlimit()
        Recharge=self.dd.Recharge()
        peoplelimit=self.dd.people_limit()
        # latitude=self.dd.latitude()
        # longitude=self.dd.longitude()
        self.dd.switch(2)  # 个人信息开启编辑
        name=self.dd.name()
        sex=self.dd.sex()
        phone=self.dd.phone()
        cardid=self.dd.cardid()
        self.dd.Photo()
        self.dd.switch(3)  # 开启编辑
        cardnum=self.dd.cardnum()
        self.dd.cardnaccount()
        self.dd.deposit()
        self.dd.Submission()
        time.sleep(1)
        tt=self.dd.querydetail(zz)
        tt1 = tt[0]
        bb = len(tt1)
        a = list(tt1)
        for i in range(bb):#数据库查询出来的 各种类型都有  统一转成str对比
            a[i] = str(a[i])
        self.assertEqual(palce, a[0])
        self.assertEqual(area, a[1])
        self.assertEqual(zhanshi, a[2])
        self.assertEqual(kailimit, a[3])
        self.assertEqual(shiwanlimit, a[4])
        self.assertEqual(Recharge, a[5])
        self.assertEqual(peoplelimit, a[6])
        # self.assertEqual(latitude, a[7])
        # self.assertEqual(longitude, a[8])
        self.assertEqual(name, a[9])
        self.assertEqual(sex, a[10])
        self.assertEqual(phone, a[11])
        self.assertEqual(cardid, a[12])

    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()