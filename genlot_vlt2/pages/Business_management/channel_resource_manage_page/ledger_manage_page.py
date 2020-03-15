# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from time import sleep


class LedgerManagePage(BasePage):
    '''台账管理页面'''

    def open_ledger_manage(self):
        '''打开台账管理页面'''
        ledger_list=[u'业务管理',u'渠道资源管理',u'台账管理']
        self.user_login()
        self.click_button_for_one(ledger_list[0])
        sleep(2)
        self.click_more_button_for_one(ledger_list[1:])
        sleep(2)

    def input_ledger_search_info(self,ledger_list):
        '''输入账单查询信息'''
        if ledger_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入仓库名称',ledger_list[0])
        if ledger_list[1]!=u'':
            self.click_option_by_inside_text_for_more_option(u'请选择仓库类型',ledger_list[1])
        if ledger_list[2]!=u'':
            self.click_option_by_inside_text_for_more_option(u'请选择物品类型',ledger_list[2])
        if ledger_list[3]!=u'':
            self.click_option_by_inside_text_for_more_option(u'请选择物品名称',ledger_list[3])
        if ledger_list[4]!=u'':
            self.click_option_by_inside_text_for_more_option(u'请选择物品型号',ledger_list[4])
        self.click_button_for_one(u'查询')
        sleep(2)

