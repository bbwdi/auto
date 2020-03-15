# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from time import sleep

class channelTerminalRepairOrderPage(BasePage):
    '''渠道终端管理维修工单页面'''

    def open_repair_manage(self,repair_list):
        '''打开维修工单页面'''
        self.click_button_for_one(repair_list[0])
        sleep(2)
        self.click_more_button_for_one(repair_list[1:])
        self.click_button_for_one(u'展开')

    def input_repair_order_search_info(self,search_list,time_dict):
        '''输入维修工单查询信息'''
        if search_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入维修人员',search_list[0])
        if search_list[1]!='':
                self.open_list_menu_and_choose_option_by_inside_text(u'请选择设备名称',search_list[1])
        if time_dict!=u'':
                self.input_star_and_end_time(time_dict)
        if search_list[2]!=u'':
                self.open_list_menu_and_choose_option_by_inside_text(u'请选择工单状态',search_list[2])
        self.click_button_for_one(u'查询')
        sleep(1)



class channelTerminalReplacementOrderPage(channelTerminalRepairOrderPage):
    '''渠道终端管理置换工单页面'''

    def open_replacement_order(self,repair_list):
        '''打开置换工单页面'''
        self.open_repair_manage(repair_list)

    def input_replacement_order_search_info(self,search_list,time_dict):
        '''输入置换工单查询信息'''
        if search_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入维修人员',search_list[0])
        if search_list[1]!='':
                self.click_option_by_inside_text_for_more_option(u'请选择物品名称',search_list[1])
        if time_dict!=u'':
                self.input_star_and_end_time(time_dict)
        if search_list[2]!=u'':
                self.click_option_by_inside_text_for_more_option(u'请选择工单状态',search_list[2])
        self.click_button_for_one(u'查询')
        sleep(1)