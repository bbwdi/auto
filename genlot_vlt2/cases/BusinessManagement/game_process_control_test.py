# -*- coding=utf-8 -*-

from time import sleep
from setting import *
import time
import datetime
from common.base_class_province import Test
from pages.Business_management.game_public_mange_page.game_public_plan_page import GamePublicPlanPage
from pages.Business_management.channel_resource_manage_page.out_put_manage_page import WarehouseManagePage
from pages.Business_management.card_balance_page.card_generation_page import CardGenerationPage
from pages.Business_management.Business_Processing.channelnewbuilt_page import New
from common.login_b import Login_B
from pages.home1_page import Home_Page
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
class ProcessControl(Test,GamePublicPlanPage,CardGenerationPage,WarehouseManagePage,New):
    '''流程控制'''


    def channel_add_approval_process(self,title):
        '''渠道建站-申请审批'''
        approval_list=[u'业务管理',u'我的待办',u'展开']
        self.user_login()
        self.click_more_button_for_one(approval_list)
        self.search_information({u'请输入业务标题':title},{},{})
        self.click_table_cell_operation_button(1,7,3,3)
        self.input_text_message_for_inside_text(u'请输入审批意见',u'同意')
        self.click_button_for_one(u'确 定')
        print(u'审批完成')

    def open_channel_add(self):
        '''打开渠道新建'''
        open_list=[u'业务管理',u'渠道业务管理',u'业务办理',u'渠道新建']
        self.user_login(u'gavin-aa',u'123456')
        self.click_button_for_one(open_list[0])
        sleep(3)
        self.click_more_button_for_one(open_list[1:])
        sleep(3)

    def login_and_add(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_channelnewbuilt()
        self.dd=New(a)

    def channel_new_shi(self):
        '''新建市级渠道'''
        # 判断是否走流程 1代表走  需要从流程表中取数据对比 0代表不走流程 对比数据从channel info
        jj = self.dd.isprocess()
        self.dd.choose_group(2)
        channel_no = self.dd.channelno()
        print channel_no
        type = self.dd.channeltype()
        level = self.dd.channellevel()
        changsuo = self.dd.place1()
        mianji = self.dd.areainput()
        limit = self.dd.kailimit()
        limit1 = self.dd.shiwanlimit()
        chongzhi = self.dd.Recharge()
        limit2 = self.dd.people_limit()
        # latitude=self.dd.latitude()
        # longitude=self.dd.longitude()
        zhanshinum = self.dd.zhanshi()
        address = self.dd.channeladdress()
        name = self.dd.name()
        sex = self.dd.sex()
        phone = self.dd.phone()
        cardid = self.dd.cardid()
        tt = datetime.datetime.now()
        kk = tt.year
        age = str(int(kk) - int(cardid[6:10]))
        address1 = self.dd.Contact_address()
        self.dd.Photo()
        cardnum = self.dd.cardnum()
        cardnaccount = self.dd.cardnaccount()
        self.dd.deposit()
        self.dd.gameJurisdiction()
        self.dd.gametime()
        self.dd.Resources()
        self.dd.appendix()
        '''通过判断jj的值 看是否存在流程，启用流程需要输入标题'''
        if jj == 1:
            time.sleep(2)
            title = self.dd.title(channel_no)
            time.sleep(2)
            self.dd.Submission()
        else:
            time.sleep(2)
            self.dd.Submission()
            '''调用渠道列表  对比数据 暂时不用'''


    def test_game_package_public(self):
        '''游戏包发布'''
        self.login_and_add()
        self.channel_new_shi()

        # self.channel_add_approval_process(u'宁夏-建站-5400010002')
        # self.game_add()
        # game_name=u'%s' %self.reader_csv(game_name_file)[0]
        # self.game_public_plan_add(game_name)
        # self.goods_warehouse(u'5400009999',[(1,u'gyj-cxm0003'),(2,u'zdj-cxm0002')])
        # self.card_generation_add()

