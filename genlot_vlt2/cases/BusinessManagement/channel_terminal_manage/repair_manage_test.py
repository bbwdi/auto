# -*- coding:utf-8 -*-

import unittest
from time import sleep

from common.base_class_province import Test
from pages.Business_management.channel_terminal_manage_page.repair_manage_page import RepairOrderPage
from pages.Business_management.channel_terminal_manage_page.repair_manage_page import ReplacementOrderPage


class channelTerminalRepairOrderTest(Test,RepairOrderPage):
    '''渠道终端管理维修管理测试'''

    repair_list=[u'业务管理',u'渠道终端管理',u'维修管理',u'维修工单']

    def test_repair_order_search(self):
        '''维修工单查询'''
        time_dict={u'开始日期':u'2019-12-05',u'结束日期':u'2020-12-31'}
        self.open_repair_manage(self.repair_list)
        search_list=[u'',1,2]
        old_count=self.get_footer_count_by_inside_text()
        self.input_repair_order_search_info(search_list,time_dict)
        new_count=self.get_footer_count_by_inside_text()
        print(old_count,new_count)
        self.assert_result_not_equal(old_count,new_count,u'维修工单查询')
        sleep(5)

    def test_repair_order_check_detail(self):
        '''维修工单查看'''
        self.open_repair_manage(self.repair_list)
        order_num=self.get_table_cell_text(1,2)
        self.click_table_cell_operation_button(1,11,1,3)
        detail_text=self.get_text_info(u'工单编号：')
        self.assert_result_equal(order_num,detail_text,u'维修工单查看')
        sleep(5)

    def test_repair_order_reset(self):
        '''维修工单重置'''
        time_dict={}
        self.open_repair_manage(self.repair_list)
        search_list=[u'',2,u'']
        self.input_repair_order_search_info(search_list,time_dict)
        first_count=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(5)
        second_count=self.get_footer_count_by_inside_text()
        print(first_count,second_count)
        self.assert_result_not_equal(first_count,second_count,u'维修工单重置')
        sleep(5)


    def test_repair_order_warn(self):
        '''一键提醒'''
        self.open_repair_manage(self.repair_list)
        self.click_button_for_one(u'一键提醒')
        sleep(2)
        tips=self.get_tips()
        self.assert_result_equal(u'提醒成功！',tips,u'一键提醒')

class ReplacementOrderTest(Test,ReplacementOrderPage):
    '''渠道终端管理置换工单测试'''
    replace_list=[u'业务管理',u'渠道终端管理',u'维修管理',u'置换工单']


    def test_replacement_order_search(self):
        '''置换工单查询'''
        time_dict={u'开始日期':u'2019-12-05',u'结束日期':u'2020-12-31'}
        search_list=[u'',u'终端机',u'待处理']
        self.open_repair_manage(self.replace_list)
        old_count=self.get_footer_count_by_inside_text()
        self.input_replacement_order_search_info(search_list,time_dict)
        new_count=self.get_footer_count_by_inside_text()
        print(old_count,new_count)
        self.assert_result_not_equal(old_count,new_count,u'置换工单查询')
        sleep(5)







if __name__=='__main__':
    unittest.main()
