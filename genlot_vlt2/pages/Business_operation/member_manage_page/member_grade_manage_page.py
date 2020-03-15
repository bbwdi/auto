# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By

class MemberGradeManagePage(BasePage):
    '''会员积分管理'''

    def open_member_grade_management(self):
        '''打开会员积分管理'''
        integral_loc=[u'业务运营',u'会员管理',u'会员等级管理']
        self.user_login()
        sleep(3)
        self.click_button_for_one(integral_loc[0])
        sleep(2)
        self.click_more_button_for_one(integral_loc[1:])
        sleep(2)

    def get_member_grade_text(self,grade_text):
        '''获取会员等级文本信息'''
        return self.find_element_for_inside_text(grade_text).text

    def stop_status(self):
        '''冻结'''
        stop_list=[u'冻结',u'确定']
        self.click_button_for_more_than_one(stop_list[0],2)
        self.click_button_for_more_than_one(stop_list[1],2)

    def start_status(self):
        '''启用'''
        start_list=[u'启用',u'确定']
        self.click_button_for_more_than_one(start_list[0],2)
        self.click_button_for_more_than_one(start_list[1],2)
