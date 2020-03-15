# -*- coding:utf-8 -*-

from time import sleep

from pages.Business_management.card_balance_page.card_manage_card_generation_page import cardGenerationPage


class cardInformationPage(cardGenerationPage):
    '''投注卡信息页面'''



    def open_card_information(self):
        '''打开投注卡信息页面'''
        button_list=[u'业务管理',u'投注卡管理',u'投注卡信息',u'展开']
        self.click_button_for_one(button_list[0])
        sleep(2)
        self.click_more_button_for_one(button_list[1:4])

    def search_card_information(self,info_list):
        '''投注卡信息查询'''
        if info_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入投注卡编号',info_list[0])
        if info_list[1]!=u'':
            self.open_list_menu_by_inside_text(u'请选择所属机构')
            self.choose_more_region_check_box_for_one(info_list[1:4])
            self.click_browser_spacing()
        if info_list[4]!=u'':
            self.click_option_by_inside_text_for_more_option(u'请选择投注卡类型',info_list[4])
        if info_list[5]!=u'':
            self.open_list_menu_and_choose_option_by_inside_text(u'请选择投注卡状态',info_list[5])
        self.click_button_for_one(u'查询')
        sleep(5)

    def switch_to_card_information(self):
        '''切换至投注卡信息查页面'''
        sleep(1)
        self.click_button_for_one(u'投注卡信息')
        sleep(2)
        self.click_button_for_one(u'展开')

