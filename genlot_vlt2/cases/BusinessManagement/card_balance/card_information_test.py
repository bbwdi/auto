# -*- coding:utf-8 -*-

import unittest
from time import sleep
from common.base_class_province import Test
from pages.Business_management.card_balance_page.card_information_page import CardInformationPage


class CardInformationTest(Test,CardInformationPage):
    '''投注卡信息测试'''

    def test_card_information_search(self):
        '''投注卡信息-卡片查询'''
        select_sql=u"select * from T_CARD_INFO where card_code='%s'"
        self.open_card_information()
        card_code=self.get_table_cell_text(1,2)
        card_type=self.get_table_cell_text(1,4)
        search_list=[card_code,u'',u'',u'',card_type,u'']
        self.search_card_information(search_list)
        result_text=self.get_search_text()
        count=self.get_data_count(select_sql %card_code)
        self.assert_result_equal(1,count,u'投注卡信息查询')
        self.assert_result_equal(card_code,result_text,u'投注卡信息查询')
        sleep(5)

    def test_card_information_check_detail(self):
        '''投注卡信息-卡片查看'''
        self.open_card_information()
        card_code=self.get_table_cell_text(1,2)
        card_type=self.get_table_cell_text(1,4)
        search_list=[card_code,u'',u'',u'',card_type,u'']
        self.search_card_information(search_list)
        self.click_table_cell_operation_button(1,6,1,3)
        detail_text=self.get_text_info(u'投注卡编号：')
        self.assert_result_equal(card_code,detail_text,u'投注卡信息查看')

    def test_card_information_cancel(self):
        '''投注卡信息-卡片注销'''
        select_sql=u"select IS_DELETE from T_CARD_INFO where CARD_CODE='%s'"
        search_list=[u'',u'中福彩',u'安徽省',u'合肥市',u'',1]
        add_list=[u'安徽省',u'合肥市',u'投注卡',1,u'卡片生成,测试投注卡新增']
        self.open_card_generation()
        self.input_card_generation_add_info(add_list)
        self.click_button_for_one(u'确 定')
        sleep(2)
        self.switch_to_card_information()
        self.search_card_information(search_list)
        card_code=self.get_table_cell_text(1,2)
        card_type=self.get_table_cell_text(1,4)
        print(card_code)
        cancel_lsit=[card_code,u'',u'',u'',card_type,u'']
        self.search_card_information(cancel_lsit)
        self.click_table_cell_operation_button(1,6,2,3)
        self.click_button_for_one(u'确定')
        tips=self.get_tips()
        delete=self.get_column_value(select_sql %card_code)
        self.assert_result_equal(1,delete[0],u'投注卡信息注销')
        self.assert_result_equal(u'注销成功!',tips,u'投注卡信息注销')

if __name__=='__main__':
    unittest.main()

