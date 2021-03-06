#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.ResourceProcurement_page import Procure
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class purcure(unittest.TestCase):
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_ResourceProcurement()
        self.dd=Procure(a)


    def test_purcure_machine(self):
        '''资源采购,采购终端机，需要有终端机类型 没有的话就随机加一个类型'''
        title=self.dd.title()
        name=self.dd.name()
        time1=self.dd.deliverdate()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        serial=self.dd.Serial()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money1=self.dd.Money()
        money=money1*100
        self.dd.appendix()
        self.dd.Submission()
        time.sleep(2)
        data=self.dd.data()
        cc=data['warehouseGoodsInfoList'][0]
        print 'cc=%s'%cc
        '''型号只有id 通过sql单独查'''
        sql1='''SELECT device_model FROM T_GOODS_MODEL WHERE goods_id = %d AND id = %d'''%(cc['goodId'],cc['modelId'])
        hh=(self.dd.sql_result(sql1))[0]
        self.assertEqual(title,data['resourceApplyTitle'])
        self.assertEqual(name,data['purchaseUserName'])
        self.assertEqual(time1, data['preReceivDate'])
        self.assertEqual(shebei, cc['goodsName'])
        self.assertEqual(modle, hh)
        self.assertEqual(serial,cc['goodsSerialNumber'])
        self.assertEqual(reason, data['remark'])
        self.assertEqual(remake,cc['remark'])
        print "money=%s"%money
        self.assertEqual(money, data['totalMoney'])

    def test_purcure_machine1(self):
        '''资源采购,采购终端机，需要有终端机类型 没有的话就随机加一个类型'''
        title=self.dd.title()
        name=self.dd.name()
        time1=self.dd.deliverdate()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        serial=self.dd.Serial()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money1=self.dd.Money()
        money=money1*100
        self.dd.appendix()
        self.dd.cancel()


    def test_purcure_machine2(self):
        '''资源采购,采购柜员机,需要有柜员机类型 没有的话就随机加一个类型'''
        tt = self.dd.title()
        self.dd.name()
        self.dd.deliverdate()
        self.dd.goodsname_guiyuanji()
        self.dd.modle()
        self.dd.reason()
        self.dd.appendix()
        self.dd.Submission()
        time.sleep(3)

    def test_purcure_machine3(self):
        '''资源采购,取消采购柜员机'''
        tt = self.dd.title()
        self.dd.name()
        self.dd.deliverdate()
        self.dd.goodsname_guiyuanji()
        self.dd.modle()
        self.dd.reason()
        self.dd.appendix()
        self.dd.cancel()
        time.sleep(3)

    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()
