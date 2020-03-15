# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class TicketOfficeManagePage(BasePage):
    '''彩票兑奖管理页面(兑奖处理)'''

    def open_ticket_office_manage(self):
        '''打开彩票管理页面'''
        manage_list=[u'业务运营',u'彩票兑奖',u'兑奖处管理']
        self.user_login()
        sleep(3)
        self.click_button_for_one(manage_list[0])
        sleep(2)
        self.click_more_button_for_one(manage_list[1:])
        sleep(3)

    def put_away_main_menu(self):
        '''收起左边主菜单'''
        menu_loc=u'//*[contains(text(),"业务运营")]/../i'
        self.find_element_for_text(menu_loc).click()

    def input_ticket_office_add_info(self,add_list,entry_dict):
        '''新增兑奖处并输入兑奖处信息'''
        self.click_more_button_for_one(add_list)
        self.input_more_text_message_for_outside_text(entry_dict)

    def click_ticket_edite_button(self,button_num=1):
        '''点击兑奖处列表后面的编辑按钮(按钮有多个)'''
        buton_loc=u'//button[@id="ticketOfficeManage-edit%s"]/span'
        self.find_elements_for_xpath(By.XPATH,buton_loc %(button_num-1)).pop(1).click()

    def input_ticket_office_edite_info(self,entry_list,entry_dict):
        '''输入兑奖处编辑信息'''
        self.click_button_for_one(entry_list[0])
        sleep(2)
        self.click_table_cell_operation_button(1,8,1)
        self.input_more_text_message_for_outside_text(entry_dict)

    def click_ticket_stop_button(self,list_num=1):
        '''点击兑奖处列表冻结按钮'''
        stop_loc=u'//table/tbody/tr[%s]/td[7]/div/div/button[2]/span'
        self.find_element_for_xpath(By.XPATH,stop_loc %list_num).click()

    def click_ticket_scroll(self):
        '''点击滚动条'''
        srcoll_loc=u'//*[@id="main"]/div/div/div/section/main/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        self.find_element_for_xpath(By.XPATH,srcoll_loc).click()

    def choose_ticket_province_city(self,entry_list):
        '''选择兑奖处省份'''
        self.open_menu_list_before_text_for_one(entry_list[1])
        sleep(2)
        self.click_more_button_for_one(entry_list)
        sleep(2)



