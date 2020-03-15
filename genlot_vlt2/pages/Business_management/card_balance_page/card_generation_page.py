# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from db.oracle_db import *
from selenium.webdriver.common.by import By
from time import sleep

class CardGenerationPage(BasePage):
    '''投注卡生成页面'''


    def open_card_generation(self):
        '''打开投注卡生成页面'''
        button_list=[u'业务管理',u'投注卡管理',u'投注卡生成',u'展开']
        self.user_login()
        sleep(2)
        self.click_button_for_one(button_list[0])
        sleep(2)
        self.click_more_button_for_one(button_list[1:4])
        sleep(2)

    def search_card_generation(self,info_list):
        '''投注卡生成查询'''
        if info_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入批次',info_list[0])
        if info_list[1]!=u'':
                self.open_list_menu_by_inside_text(u'请选择所属机构')
                self.choose_more_region_check_box_for_one(info_list[1:4])
                self.click_browser_spacing()
        if info_list[4]!=u'':
                self.open_list_menu_and_choose_option_by_inside_text(u'请选择投注卡类型',info_list[4])
        self.click_button_for_one(u'查询')
        sleep(2)

    def input_card_generation_add_info(self,info_list):
        '''输入新增信息'''
        self.click_button_for_one(u'新建卡片')
        sleep(1)
        self.open_list_menu_by_inside_text(u'请选择所属机构')
        self.click_button_for_one(info_list[0])
        self.choose_region_check_box_for_one(info_list[1])
        self.click_browser_spacing()
        sleep(1)
        self.click_option_by_inside_text_for_more_option(u'请选择投注卡类型',info_list[2])
        self.input_text_message_for_inside_text(u'请输入发卡数量',info_list[3])
        self.input_text_message_for_inside_text(u'请输入备注',info_list[4])

    def card_generation_add(self):
        '''投注卡生成'''
        select_sql=u"select * from T_CARD_INFO where batch='%s'"
        select_code=u"select card_code from T_CARD_INFO where batch='%s'"
        info_list=[u'宁夏回族自治区',u'银川市',u'投注卡',3,u'卡片生成,测试投注卡新增']
        self.open_card_generation()
        self.input_card_generation_add_info(info_list)
        self.click_button_for_one(u'确 定')
        tips=self.get_tips()
        batch_id=self.get_table_cell_text(1,2)
        num=self.get_data_count(select_sql %batch_id)
        card_code=self.get_column_value(select_code %batch_id)
        print(card_code)
        self.assert_result_equal(info_list[3],num,u'投注卡新增')
        self.assert_result_equal(u'操作成功',tips,u'投注卡新增')


