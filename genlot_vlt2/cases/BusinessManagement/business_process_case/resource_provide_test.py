#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.ResourceProvide_page import Provide
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class provide_machine(unittest.TestCase):
    '''资源发放'''
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_ResourceProvide()
        self.dd=Provide(a)


    def test_provide_machine(self):
        '''资源发放,提交终端机'''
        title=self.dd.title()
        warehouse=self.dd.warehouse()
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

    def test_provide_machine1(self):
        '''资源发放,暂存终端机'''
        title=self.dd.title()
        warehouse=self.dd.warehouse()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money=self.dd.Money()
        self.dd.appendix()
        self.dd.zancun()
        time.sleep(2)

    def test_provide_machine2(self):
        '''资源发放,取消提交终端机'''
        title=self.dd.title()
        warehouse=self.dd.warehouse()
        shebei=self.dd.goodsname_zhongduanji()
        modle=self.dd.modle()
        remake = self.dd.Remarks()
        reason=self.dd.reason()
        money=self.dd.Money()
        self.dd.appendix()
        self.dd.cancel()
        time.sleep(2)

    def test_provide_machine3(self):
        '''资源发放,提交柜员机'''
        title = self.dd.title()
        warehouse = self.dd.warehouse()
        shebei = self.dd.goodsname_zhongduanji()
        modle = self.dd.modle()
        remake = self.dd.Remarks()
        reason = self.dd.reason()
        money = self.dd.Money()
        self.dd.appendix()
        self.dd.Submission()
        time.sleep(2)

    def test_provide_machine4(self):
        '''资源发放,暂存柜员机'''
        title = self.dd.title()
        warehouse = self.dd.warehouse()
        shebei = self.dd.goodsname_zhongduanji()
        modle = self.dd.modle()
        remake = self.dd.Remarks()
        reason = self.dd.reason()
        money = self.dd.Money()
        self.dd.appendix()
        self.dd.zancun()
        time.sleep(2)

    def test_provide_machine5(self):
        '''资源发放,取消柜员机'''
        title = self.dd.title()
        warehouse = self.dd.warehouse()
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
