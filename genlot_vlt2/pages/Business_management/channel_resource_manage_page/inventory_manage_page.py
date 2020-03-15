# -*- coding:utf-8 -*-

from pages.base_page import BasePage
from time import sleep

class DeviceListPage(BasePage):
    '''库存管理-设备列表页面'''

    inventory=[u'业务管理',u'渠道资源管理',u'库存管理']


    def open_inventory_manage(self,open_list=inventory):
        '''打开库存管理'''
        sleep(3)
        self.click_button_for_one(open_list[0])
        sleep(3)
        self.click_more_button_for_one(open_list[1:])
        sleep(2)

    def open_device_list(self):
        '''打开设备列表'''
        device=[u'业务管理',u'渠道资源管理',u'库存管理',u'设备列表']
        self.user_login()
        self.open_inventory_manage(device)

    def input_device_list_search_info(self,search_list):
        '''输入设备列表查询信息'''
        if search_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入设备名称',search_list[0])
        if search_list[1]!=u'':
            self.input_text_message_for_inside_text(u'请输入物品型号',search_list[1])
        self.click_button_for_one(u'查询')
        sleep(1)

    def input_device_check_search_info(self,check_list):
        '''输入查看部分的查询信息'''
        sleep(2)
        self.click_button_for_one(u'展开')
        if check_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入序列号',check_list[0])
        if check_list[1]!=u'':
            self.input_start_and_end_time(check_list[1])
        if check_list[2]!=u'':
            self.input_text_message_for_inside_text(u'请输入仓库名称',check_list[2])
        self.click_button_for_one(u'查询')
        sleep(1)


    def export_present_data(self,file_name):
        '''导出当前'''
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_name)
        return result


    def export_all_data(self,file_name):
        '''导出全部'''
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_name)
        return result


class FacilityListPage(DeviceListPage):
    '''库存管理-设施列表页面'''

    def open_facility_list(self):
        '''打开设施列表'''
        facility=[u'业务管理',u'渠道资源管理',u'库存管理',u'设施列表']
        self.user_login()
        self.open_inventory_manage(facility)

    def input_facility_list_search_info(self,search_list):
        '''输入设备列表查询信息'''
        if search_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入设施名称',search_list[0])
        self.click_button_for_one(u'查询')
        sleep(1)

    def input_facility_check_search_info(self,check_list):
        '''输入查看部分的查询信息'''
        if check_list[0]!=u'':
            self.input_start_and_end_time(check_list[0])
        if check_list[1]!=u'':
            self.input_text_message_for_inside_text(u'请输入仓库名称',check_list[1])
        self.click_button_for_one(u'查询')
        sleep(1)

class ConsumableListPage(DeviceListPage):
    '''库存管理-耗材列表页面'''


    def open_consumable_list(self):
        '''打开耗材列表'''
        consumable=[u'业务管理',u'渠道资源管理',u'库存管理',u'耗材列表']
        self.user_login()
        self.open_inventory_manage(consumable)

    def input_consumable_list_search_info(self,search_list):
        if search_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入耗材名称',search_list[0])
        self.click_button_for_one(u'查询')
        sleep(1)

    def input_consumable_check_search_info(self,check_list):
        '''输入查看部分的查询信息'''
        if check_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入仓库名称',check_list[0])
        if check_list[1]!=u'':
            self.input_start_and_end_time(check_list[1])
        self.click_button_for_one(u'查询')
        sleep(1)

class FittingListPage(DeviceListPage):
    '''库存管理-配件列表页面'''

    def open_fitting_list(self):
        '''打开配件列表'''
        fitting=[u'业务管理',u'渠道资源管理',u'库存管理',u'配件列表']
        self.user_login()
        self.open_inventory_manage(fitting)

    def input_fitting_list_search_info(self,search_list):
        if search_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入配件名称',search_list[0])
        if search_list[1]!=u'':
                self.input_text_message_for_inside_text(u'请输入物品型号',search_list[1])
        self.click_button_for_one(u'查询')
        sleep(1)

    def input_fitting_check_search_info(self,check_list):
        '''输入查看部分的查询信息'''
        if check_list[0]!=u'':
            self.input_text_message_for_inside_text(u'请输入序列号',check_list[0])
        if check_list[1]!=u'':
            self.input_start_and_end_time(check_list[1])
        if check_list[2]!=u'':
            self.input_text_message_for_inside_text(u'请输入仓库名称',check_list[2])
        self.click_button_for_one(u'查询')
        sleep(1)