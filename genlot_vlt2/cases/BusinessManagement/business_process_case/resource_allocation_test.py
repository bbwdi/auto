#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.Allocation_page import Allocation
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class Allocation_machine(unittest.TestCase):
    '''资源发放'''
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_ResourceAllocation()
        self.dd=Allocation(a)


    def test_allocation_machine(self):
        '''资源调拨,提交终端机'''
        title=self.dd.title()
        Ex_warehouse=self.dd.Ex_warehouse()
        In_warehouse = self.dd.In_warehouse()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money=self.dd.Money()
        self.dd.appendix()
        self.dd.Submission()
        time.sleep(2)
        # data=self.dd.data()
        # cc=data['warehouseGoodsInfoList'][0]
        # print 'cc=%s'%cc
        # '''型号只有id 通过sql单独查'''
        # sql1='''SELECT device_model FROM T_GOODS_MODEL WHERE goods_id = %d AND id = %d'''%(cc['goodId'],cc['modelId'])
        # hh=(self.dd.sql_result(sql1))[0]
        # self.assertEqual(title,data['resourceApplyTitle'])
        # self.assertEqual(name,data['purchaseUserName'])
        # self.assertEqual(time1, data['preReceivDate'])
        # self.assertEqual(shebei, cc['goodsName'])
        # self.assertEqual(modle, hh)
        # self.assertEqual(serial,cc['goodsSerialNumber'])
        # self.assertEqual(reason, data['remark'])
        # self.assertEqual(remake,cc['remark'])
        # self.assertEqual(money, data['totalMoney'])

    def test_allocation_machine1(self):
        '''资源调拨,暂存终端机'''
        title=self.dd.title()
        Ex_warehouse=self.dd.Ex_warehouse()
        In_warehouse = self.dd.In_warehouse()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money=self.dd.Money()
        self.dd.appendix()
        self.dd.zancun()
        time.sleep(2)

    def test_allocation_machine2(self):
        '''资源调拨,取消终端机'''
        title=self.dd.title()
        Ex_warehouse=self.dd.Ex_warehouse()
        In_warehouse = self.dd.In_warehouse()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money=self.dd.Money()
        self.dd.appendix()
        self.dd.cancel()
        time.sleep(2)

    def test_allocation_machine3(self):
        '''资源调拨,提交柜员机'''
        title = self.dd.title()
        Ex_warehouse = self.dd.Ex_warehouse()
        In_warehouse = self.dd.In_warehouse()
        shebei = self.dd.goodsname_zhongduanji()
        modle = self.dd.modle()
        remake = self.dd.Remarks()
        reason = self.dd.reason()
        money = self.dd.Money()
        self.dd.appendix()
        self.dd.Submission()
        time.sleep(2)

    def test_allocation_machine4(self):
        '''资源调拨,暂存柜员机'''
        title = self.dd.title()
        Ex_warehouse = self.dd.Ex_warehouse()
        In_warehouse = self.dd.In_warehouse()
        shebei = self.dd.goodsname_zhongduanji()
        modle = self.dd.modle()
        remake = self.dd.Remarks()
        reason = self.dd.reason()
        money = self.dd.Money()
        self.dd.appendix()
        self.dd.zancun()
        time.sleep(2)

    def test_allocation_machine5(self):
        '''资源调拨,取消柜员机'''
        title = self.dd.title()
        Ex_warehouse = self.dd.Ex_warehouse()
        In_warehouse = self.dd.In_warehouse()
        shebei = self.dd.goodsname_zhongduanji()
        modle = self.dd.modle()
        remake = self.dd.Remarks()
        reason = self.dd.reason()
        money = self.dd.Money()
        self.dd.appendix()
        self.dd.cancel()
        time.sleep(2)

    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()
