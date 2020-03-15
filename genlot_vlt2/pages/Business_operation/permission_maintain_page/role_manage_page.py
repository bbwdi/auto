# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from db.oracle_db import Oracle
from selenium.webdriver.common.by import By
from time import sleep

class RoleListPage(BasePage):
    '''渠道角色权限维护页面'''


    def get_role_status(self,role_name):
        '''sql查询'''
        select_sql=u"select * from T_CHANNEL_ROLE_INFO where role_name='%s'"
        select=Oracle()
        data=select.run_sql(select_sql %role_name)
        if data[3]==u'1':
            return  u'启用'
        elif data[3]==u'2':
            return u'冻结'
        elif data[3]==u'3':
            return u'注销'
        else:
            return u'状态位异常'


    def open_role_list(self):
        '''打开角色管理-角色列表界面'''
        role_list=[u'业务运营',u'角色管理',u'角色列表']
        self.user_login()
        sleep(3)
        self.click_button_for_one(role_list[0])
        sleep(2)
        self.click_more_button_for_one(role_list[1:])
        sleep(5)


    def input_role_manage_search_info(self,entry_list,time_dict):
        '''输入角色管理查询信息'''
        self.click_button_for_one(u'展开')
        self.open_list_menu_by_inside_text(u'请选择用户角色')
        self.click_button_for_more_than_one(entry_list[0],3)
        self.input_text_message_for_inside_text(u'请输入创建人',entry_list[1])
        self.input_start_and_end_time(time_dict)
        self.open_list_menu_and_choose_option_by_inside_text(u'请选择角色状态',entry_list[2])
        self.click_button_for_more_than_one(u'查询',2)
        sleep(1)

    def input_role_manage_add_info(self,role_list,permission_list):
        '''输入角色管理新增信息'''
        self.click_button_for_one(u'新增角色')
        sleep(1)
        self.input_text_message_for_inside_text(u'请输入角色名称',role_list[0])
        self.open_role_permission_list_for_one(permission_list[0])
        for value in permission_list[1:4]:
            self.choose_permission_check_box_before_text_for_one(value)
        self.choose_app_permission_before_text(permission_list[4])
        self.click_button_for_more_than_one(role_list[1],2)
        self.input_text_message_for_outside_text(u'描述',role_list[2])
        self.click_button_for_one(u'提 交')


    def search_role(self,entry_list):
        '''查询角色'''
        self.click_button_for_one(u'展开')
        self.click_option_by_inside_text_for_more_option(u'请选择用户角色',entry_list[0])
        self.click_search_button()
        sleep(2)

    def open_role_permission(self):
        '''打开角色权限'''
        permission_loc=u'//*[@id="main"]/div/div/div/div[5]/div/div/div[2]/div/form/div[1]/div/div/div[2]/span/span'
        self.find_element_for_xpath(By.XPATH,permission_loc).click()

    def get_permission_text(self):
        '''获取权限信息'''
        text_loc=u'//*[@id="main"]/div/div/div/div[5]/div/div/div[2]/div/form/div[1]/div/div/div[2]'
        return self.find_element_for_xpath(By.XPATH,text_loc).text

    def operation_role_set_permission(self,button_list):
        '''权限设置'''
        self.click_button_for_more_than_one(button_list[0],2)
        self.open_role_permission()
        self.click_button_for_more_than_one(button_list[1],5)
        self.choose_check_box_before_text_for_one(button_list[2])
        self.click_browser_spacing()

    def operation_role_cancel_permission(self,button_list):
        '''权限取消'''
        self.click_button_for_more_than_one(button_list[0],2)
        self.open_role_permission()
        self.click_button_for_more_than_one(button_list[1],7)
        self.choose_check_box_before_text_for_one(button_list[2])
        self.click_browser_spacing()

    def choose_permission_check_box_before_text_for_one(self,permission_name):
        '''选择权限前的复选框(元素唯一)'''
        per_loc=u'//*[contains(text(),"%s")]/../../label/span/span'
        self.find_element_for_text(per_loc %permission_name).click()

    def choose_permission_check_box_before_text_for_more_than_one(self,permission_name,index_num):
        '''选择权限前的复选框(元素多个)'''
        per_loc=u'//*[contains(text(),"%s")]/../../label/span/span'
        self.find_elements_for_text(per_loc %permission_name).pop(index_num-1).click()

    def open_role_permission_list_for_one(self,permission_name):
            '''展开下拉菜单(元素唯一)'''
            per_loc=u'//*[contains(text(),"%s")]/../../span[1]'
            self.find_element_for_text(per_loc %permission_name).click()

    def choose_app_permission_before_text(self,per_text):
        '''选择app权限'''
        app_loc=u'//*[contains(text(),"%s")]/../span/span'
        self.find_element_for_text(app_loc %per_text).click()


    def edite_role_info(self,entry_list):
        '''编辑角色信息'''
        sleep(1)
        self.open_role_permission_list_for_one(entry_list[0])
        sleep(1)
        for value in entry_list[1:6]:
            self.choose_permission_check_box_before_text_for_one(value)
        self.choose_app_permission_before_text(entry_list[6])

    def role_status_start(self):
        '''角色状态启用'''
        self.click_table_cell_operation_button(1,4,1,1)#启用
        self.click_button_for_more_than_one(u'确定',2)
        sleep(1)

    def role_status_stop(self):
        '''角色状态冻结'''
        self.click_table_cell_operation_button(1,4,2,1)#冻结
        self.click_button_for_more_than_one(u'确定',2)
        sleep(0.5)