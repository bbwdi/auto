# -*- coding:utf-8 -*-

import unittest
from time import sleep
from common.base_class_province import Test
from pages.Business_operation.lottery_manage_page.ticket_office_manage_page import TicketOfficeManagePage


class TicketOfficeManageTest(Test,TicketOfficeManagePage):
    '''彩票兑奖管理(兑奖处理)'''

    province_list=[u'中福彩',u'山西省']
    add_list=[u'山西省',u'新增兑奖处']
    info_dict={u'兑奖处名称':u'山西省兑奖处',u'负责人':u'李海天',u'联系方式':u'13652512582',u'兑奖地址':u'山西省市区'}

    def ticket_office_add(self):
        '''统一的新增入口'''
        self.open_ticket_office_manage()
        self.input_ticket_office_add_info(self.add_list,self.info_dict)
        self.click_button_for_one(u'确 定')

    def test_ticket_office_manage_add(self):
        '''兑奖处管理'''
        self.ticket_office_add()
        tips=self.get_tips()
        self.assert_result_equal(u'新增成功',tips,u'兑奖处管理新增')
        sleep(2)
        self.put_away_main_menu()
        self.choose_ticket_province_city(self.province_list)
        self.right_scroll(u'is-scrolling-left',100)
        self.click_table_cell_operation_button(1,7,3,1)#注销
        self.click_button_for_more_than_one(u'确定',2)

    def test_ticket_office_manage_edite(self):
        '''兑奖处管理编辑'''
        edite_list=[u'山西省',u'编辑']
        edite_dict={u'兑奖处名称':u'山西省太原兑奖处',u'负责人':u'李海地',u'联系方式':u'13652512581',u'兑奖地址':u'山西省太原市区'}
        self.ticket_office_add()
        sleep(3)
        self.put_away_main_menu()
        self.choose_ticket_province_city(self.province_list)
        self.right_scroll(u'is-scrolling-left',300)
        self.input_ticket_office_edite_info(edite_list,edite_dict)
        self.click_button_for_more_than_one(u'保 存',1)
        sleep(1)
        tips=self.get_tips()
        sleep(2)
        self.click_table_cell_operation_button(1,7,3,1)#注销
        self.click_button_for_more_than_one(u'确定',2)
        self.assert_result_equal(u'修改成功',tips,u'兑奖处管理编辑')
        sleep(5)

    #@unittest.skip(u"跳过测试")
    def test_ticket_office_status_cancel(self):
        '''兑奖处状态注销'''
        self.ticket_office_add()
        sleep(2)
        self.put_away_main_menu()
        self.choose_ticket_province_city(self.province_list)
        self.right_scroll(u'is-scrolling-left',100)
        self.click_table_cell_operation_button(1,7,3,1)#注销
        self.click_button_for_more_than_one(u'确定',2)
        tips=self.get_tips()
        self.assert_result_equal(u'操作成功',tips,u'兑奖处管理-注销')

    #@unittest.skip(u"跳过测试")
    def test_ticket_office_status_start_and_stop(self):
        '''兑奖处状态启用-冻结'''
        self.ticket_office_add()
        sleep(5)
        self.choose_ticket_province_city(self.province_list)
        self.right_scroll(u'is-scrolling-left',300)
        sleep(2)
        self.click_table_cell_operation_button(1,7,2,1)#冻结
        self.click_button_for_more_than_one(u'确定',2)
        tips_stop=self.get_tips()
        self.assert_result_equal(u'操作成功',tips_stop,u'兑奖处管理-冻结')
        self.click_table_cell_operation_button(1,7,1,1)#启用
        self.click_button_for_more_than_one(u'确定',2)
        tips_start=self.get_tips()
        self.assert_result_equal(u'操作成功',tips_start,u'兑奖处管理-启用')
        self.click_table_cell_operation_button(1,7,3,1)#注销
        self.click_button_for_more_than_one(u'确定',2)


if __name__=='__main__':
    unittest.main()
