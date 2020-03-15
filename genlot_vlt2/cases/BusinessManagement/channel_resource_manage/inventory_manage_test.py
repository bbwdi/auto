# -*- coding:utf-8 -*-

import unittest
from time import sleep

import setting
from common.base_class_province import Test
from pages.Business_management.channel_resource_manage_page.inventory_manage_page import ConsumableListPage
from pages.Business_management.channel_resource_manage_page.inventory_manage_page import DeviceListPage
from pages.Business_management.channel_resource_manage_page.inventory_manage_page import FacilityListPage
from pages.Business_management.channel_resource_manage_page.inventory_manage_page import FittingListPage


class DeviceListTest(Test,DeviceListPage):
    '''库存管理-设备列表测试'''

    def test_device_list_search(self):
        '''设备列表查询'''
        self.open_device_list()
        search_list=[self.get_table_cell_text(1,2),self.get_table_cell_text(1,3)]
        self.input_device_list_search_info(search_list)
        search_result=self.get_table_cell_text(1,2)
        self.assert_result_equal(search_list[0],search_result,u'设备列表查询')
        sleep(5)

    def test_device_list_reset(self):
        '''设备列表重置'''
        self.open_device_list()
        search_list=[self.get_table_cell_text(1,2),self.get_table_cell_text(1,3)]
        self.input_device_list_search_info(search_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'设备列表重置')
        sleep(5)

    def test_device_list_check(self):
        '''设备列表查看'''
        self.open_device_list()
        device_name=self.get_table_cell_text(1,2)
        device_count=self.get_table_cell_text(1,5)
        self.click_table_cell_button(1,6)
        sleep(1)
        if device_count==u'':
            print(u'无数据')
        else:
            search_text=self.get_table_cell_text(1,2)
            print(device_name,search_text)
            self.assert_result_equal(device_name,search_text,u'设备列表查看')

    def test_device_list_check_reset(self):
        '''设备列表查看中的重置'''
        self.open_device_list()
        search_list=[self.get_table_cell_text(1,2),u'']
        self.input_device_list_search_info(search_list)
        self.click_table_cell_button(1,6)
        sleep(1)
        check_list=[self.get_table_cell_text(3,4),{u'开始日期':u'2020-01-03',u'结束日期':u'2020-01-07'},u'']
        self.input_device_check_search_info(check_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'设备列表查看中的重置')
        sleep(5)

    def test_device_list_print(self):
        '''设备列表打印'''
        self.open_device_list()
        self.click_button_for_one(u'打印当前')
        sleep(5)

    def test_device_list_export_present(self):
        '''设备列表导出当前'''
        file_name=setting.download_path + u'设备库存数据.xls'
        self.open_device_list()
        count=self.get_footer_count_by_inside_text()
        print(count)
        present_result=self.export_present_data(file_name)
        self.assert_result_equal(True,present_result,u'设备列表-导出当前')

    def test_device_list_export_all(self):
        '''设备列表导出当前'''
        file_name=setting.download_path + u'设备库存数据.xls'
        self.open_device_list()
        all_result=self.export_all_data(file_name)
        self.assert_result_equal(True,all_result,u'设备列表-导出全部')


class FacilityListTest(Test,FacilityListPage):
    '''库存管理-设施列表测试'''

    def test_facility_list_search(self):
        '''设施列表查询'''
        self.open_facility_list()
        facility_name=self.get_table_cell_text(1,2)
        search_list=[facility_name]
        self.input_facility_list_search_info(search_list)
        search_result=self.get_table_cell_text(1,2)
        self.assert_result_equal(search_list[0],search_result,u'设施列表查询')

    def test_facility_list_reset(self):
        '''设施列表重置'''
        self.open_facility_list()
        goods_name=self.get_table_cell_text(1,3)
        search_list=[goods_name]
        self.input_facility_list_search_info(search_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'设施列表重置')
        sleep(5)

    #@unittest.skip(u'逃过测试')
    def test_facility_list_check(self):
        '''设施列表查看'''
        self.open_facility_list()
        search_list=[self.get_table_cell_text(1,2),u'']
        self.input_facility_list_search_info(search_list)
        self.click_table_cell_button(1,5)#点击查看按钮
        sleep(1)
        check_list=[{u'开始日期':u'2019-12-15',u'结束日期':u'2020-12-30'},self.get_table_cell_text(1,3)]
        old_count=self.get_footer_count_by_inside_text()
        print(old_count)
        self.input_facility_check_search_info(check_list)
        new_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(old_count,new_count,u'设施列表查看')

    #@unittest.skip(u'逃过测试')
    def test_facility_list_check_reset(self):
        '''设施列表查看中的重置'''
        self.open_facility_list()
        search_list=[self.get_table_cell_text(1,2),u'']
        self.input_facility_list_search_info(search_list)
        self.click_table_cell_button(1,5)
        sleep(1)
        check_list=[{u'开始日期':u'2019-12-15',u'结束日期':u'2020-12-30'},self.get_table_cell_text(1,5)]
        self.input_facility_check_search_info(check_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'设施列表查看中的重置')
        sleep(5)

    def test_facility_list_print(self):
        '''设备列表打印'''
        self.open_facility_list()
        self.click_button_for_one(u'打印当前')

    def test_facility_list_export_present(self):
        '''设施列表导出当前'''
        file_name=setting.download_path + u'设施库存数据.xls'
        self.open_facility_list()
        present_result=self.export_present_data(file_name)
        self.assert_result_equal(True,present_result,u'设施列表-导出当前')

    def test_facility_list_export_all(self):
        '''设施列表导出全部'''
        file_name=setting.download_path + u'设施库存数据.xls'
        self.open_facility_list()
        all_result=self.export_all_data(file_name)
        self.assert_result_equal(True,all_result,u'设施列表-导出全部')


class ConsumableListTest(Test,ConsumableListPage):
    '''库存管理-耗材列表测试'''


    def test_consumable_list_search(self):
        '''耗材列表查询'''
        self.open_consumable_list()
        search_list=[self.get_table_cell_text(1,2),u'']
        self.input_consumable_list_search_info(search_list)
        search_result=self.get_table_cell_text(1,2)
        self.assert_result_equal(search_list[0],search_result,u'耗材列表查询')
        sleep(5)

    def test_consumable_list_reset(self):
        '''耗材列表重置'''
        self.open_consumable_list()
        search_list=[self.get_table_cell_text(1,2),u'']
        self.input_consumable_list_search_info(search_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'耗材列表重置')

    #@unittest.skip(u'逃过测试')
    def test_consumable_list_check(self):
        '''耗材列表查看'''
        self.open_consumable_list()
        consumable_name=self.get_table_cell_text(1,2)
        search_list=[consumable_name]
        self.input_consumable_list_search_info(search_list)
        self.click_table_cell_button(1,5)#点击查看按钮
        sleep(1)
        check_text=self.get_table_cell_text(1,2)
        print(consumable_name,check_text)
        self.assert_result_equal(consumable_name,check_text,u'耗材列表查看')
        sleep(5)

    #@unittest.skip(u'逃过测试')
    def test_consumable_list_check_reset(self):
        '''耗材列表查看中的重置'''
        self.open_consumable_list()
        self.click_table_cell_button(1,5)
        sleep(1)
        check_list=[self.get_table_cell_text(1,3),{}]
        self.input_consumable_check_search_info(check_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'耗材列表查看中的重置')

    def test_consumable_list_print(self):
        '''耗材列表打印'''
        self.open_consumable_list()
        self.click_button_for_one(u'打印当前')

    def test_consumable_list_export_present(self):
        '''耗材列表导出当前'''
        file_name=setting.download_path + u'耗材库存数据.xls'
        self.open_consumable_list()
        present_result=self.export_present_data(file_name)
        self.assert_result_equal(True,present_result,u'耗材列表-导出当前')

    def test_consumable_list_export_all(self):
        '''耗材列表导出当前'''
        file_name=setting.download_path + u'耗材库存数据.xls'
        self.open_consumable_list()
        all_result=self.export_all_data(file_name)
        self.assert_result_equal(True,all_result,u'耗材列表-导出全部')


#@unittest.skip(u'逃过测试')
class FittingListTest(Test,FittingListPage):
    '''库存管理-配件列表测试'''


    def test_fitting_list_search(self):
        '''配件列表查询'''
        self.open_fitting_list()
        search_list=[self.get_table_cell_text(1,2),self.get_table_cell_text(1,3)]
        self.input_fitting_list_search_info(search_list)
        search_result=self.get_table_cell_text(1,2)
        self.assert_result_equal(search_list[0],search_result,u'配件列表查询')
        sleep(5)

    def test_fitting_list_reset(self):
        '''配件列表重置'''
        self.open_fitting_list()
        search_list=[self.get_table_cell_text(1,2),self.get_table_cell_text(1,3)]
        self.input_fitting_list_search_info(search_list)
        count_num=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(1)
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(count_num,reset_count,u'配件列表重置')

    #@unittest.skip(u'逃过测试')
    def test_fitting_list_check(self):
        '''配件列表查看'''
        self.open_fitting_list()
        fitting_name=self.get_table_cell_text(1,2)
        fitting_count=self.get_table_cell_text(1,5)
        self.click_table_cell_button(1,6)#点击查看按钮
        sleep(1)
        if fitting_count==u'':
            print(u'无数据')
        else:
            check_name=self.get_table_cell_text(1,2)
            self.assert_result_equal(fitting_name,check_name,u'配件列表查看')

    #@unittest.skip(u'逃过测试')
    def test_fitting_list_check_reset(self):
        '''配件列表查看中的重置'''
        self.open_fitting_list()
        fitting_count=self.get_footer_count_by_inside_text()
        sleep(1)
        if fitting_count==0:
            print(u'无数据')
        else:
            self.click_table_cell_button(1,6)#点击查看按钮
            check_list=[self.get_table_cell_text(2,4),{},u'']
            self.input_fitting_check_search_info(check_list)
            count_num=self.get_footer_count_by_inside_text()
            self.click_button_for_one(u'重置')
            self.click_button_for_one(u'查询')
            sleep(3)
            reset_count=self.get_footer_count_by_inside_text()
            print(count_num,reset_count)
            self.assert_result_not_equal(count_num,reset_count,u'配件列表查看中的重置')


    def test_fitting_list_print(self):
        '''配件列表打印'''
        self.open_fitting_list()
        self.click_button_for_one(u'打印当前')

    def test_fitting_list_export_present(self):
        '''配件列表导出当前'''
        file_name=setting.download_path + u'配件库存数据.xls'
        self.open_fitting_list()
        present_result=self.export_present_data(file_name)
        self.assert_result_equal(True,present_result,u'配件列表-导出当前')

    def test_fitting_list_export_all(self):
        '''配件列表导出全部'''
        file_name=setting.download_path + u'配件库存数据.xls'
        self.open_fitting_list()
        all_result=self.export_all_data(file_name)
        self.assert_result_equal(True,all_result,u'配件列表-导出全部')

if __name__=='main':
    unittest.main()



