# -*- coding:utf-8 -*-

import unittest
from time import sleep
from setting import *
from pages.Business_management.channel_resource_manage_page.out_put_manage_page import WarehouseManagePage
from pages.Business_management.channel_resource_manage_page.out_put_manage_page import OutDepotManagePage
from common.base_class_province import Test


class WarehouseManageTest(Test,WarehouseManagePage):
    '''入库管理测试'''


    def test_warehouse_search(self):
        '''入库管理-查询'''
        self.open_warehouse_manage()
        self.get_and_input_search_info()
        search_result=self.get_table_cell_text(1,2)
        self.assert_result_equal(self.order_code,search_result,u'入库管理-查询')

    def test_warehouse(self):
        '''入库管理-入库'''
        self.open_warehouse_manage()
        self.get_and_input_search_info()
        self.click_table_cell_operation_button(1,8,1,3)#点击入库
        sleep(5)
        #self.assert_result_equal(self.order_code,search_result,u'入库管理-查询')

    def test_in_depot(self):
        '''入库'''
        self.goods_warehouse(u'5400009999',[(1,u'0001'),(2,u'0002')])
        sleep(10)

    def test_warehouse_reset(self):
        '''入库管理-重置'''
        self.open_warehouse_manage()
        self.get_and_input_search_info()
        search_count=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_search_button()
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(search_count,reset_count,u'入库管理-重置')

    def test_warehouse_print(self):
        '''入库管理-打印'''
        self.open_warehouse_manage()
        self.click_button_for_one(u'打印当前')
        sleep(20)

    def test_wait_warehouse_export_present(self):
        '''入库管理-待入库-导出当前'''
        file_path=download_path + u'待入库管理数据.xls'
        self.open_warehouse_manage()
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'待入库-导出当前')

    def test_wait_warehouse_export_all(self):
        '''入库管理-待入库-导出全部'''
        file_path=download_path + u'待入库管理数据.xls'
        self.open_warehouse_manage()
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'待入库-导出全部')

    def test_already_warehouse_export_present(self):
        '''入库管理-已入库-导出当前'''
        file_path=download_path + u'已入库管理数据.xls'
        self.open_warehouse_manage()
        self.click_button_for_one(u'已入库')
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'已入库-导出当前')

    def test_already_warehouse_export_all(self):
        '''入库管理-已入库-导出全部'''
        file_path=download_path + u'已入库管理数据.xls'
        self.open_warehouse_manage()
        self.click_button_for_one(u'已入库')
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'已入库-导出全部')

    def test_already_warehouse_check(self):
        '''入库管理-已入库-查看 '''
        self.open_warehouse_manage()
        self.click_button_for_one(u'已入库')
        order_code=self.get_already_warehouse_cell_text(1,2)
        apply_title=self.get_already_warehouse_cell_text(1,3)
        info_dict={u'请输入单据编号':order_code,u'请输入申请标题':apply_title}
        self.search_information(info_dict,{},{})
        self.click_button_for_more_than_one(u'查看',3)
        result=self.get_text_info(u'单据编号：')
        self.assert_result_equal(order_code,result,u'已入库-查看')



class OutDepotManageTest(Test,OutDepotManagePage):
    '''出库管理测试'''

    def test_out_depot_search(self):
        '''出库管理-查询'''
        self.open_out_depot_manage()
        self.get_and_input_search_info()
        search_result=self.get_table_cell_text(1,2)
        self.assert_result_equal(self.order_code,search_result,u'出库管理-查询')

    def test_out_depot(self):
        '''出库管理-出库'''
        self.open_out_depot_manage()
        self.get_and_input_search_info()
        self.click_table_cell_operation_button(1,8,1,3)#点击出库
        sleep(5)
        #self.assert_result_equal(self.order_code,search_result,u'出库管理-查询')

    def test_out_depot_reset(self):
        '''出库管理-重置'''
        self.open_out_depot_manage()
        self.get_and_input_search_info()
        search_count=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_search_button()
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(search_count,reset_count,u'出库管理-重置')

    def test_out_depot_print(self):
        '''出库管理-打印'''
        self.open_out_depot_manage()
        self.click_button_for_one(u'打印当前')
        sleep(20)

    def test_wait_out_depot_export_present(self):
        '''出库管理-待出库-导出当前'''
        file_path=download_path + u'待出库管理数据.xls'
        self.open_out_depot_manage()
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'待出库-导出当前')

    def test_out_depot_export_all(self):
        '''出库管理-待出库-导出全部'''
        file_path=download_path + u'待出库管理数据.xls'
        self.open_out_depot_manage()
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'待出库-导出全部')

    def test_already_out_depot_export_present(self):
        '''出库管理-已出库-导出当前'''
        file_path=download_path + u'已出库管理数据.xls'
        self.open_out_depot_manage()
        self.click_button_for_one(u'已出库')
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'已出库-导出当前')

    def test_already_out_depot_export_all(self):
        '''出库管理-已出库-导出全部'''
        file_path=download_path + u'已出库管理数据.xls'
        self.open_out_depot_manage()
        self.click_button_for_one(u'已出库')
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'已出库-导出全部')

    def test_already_out_depot_check(self):
        '''出库管理-已出库-查看 '''
        self.open_out_depot_manage()
        self.click_button_for_one(u'已出库')
        order_code=self.get_already_out_cell_text(1,2)
        apply_title=self.get_already_out_cell_text(1,3)
        info_dict={u'请输入单据编号':order_code,u'请输入申请标题':apply_title}
        self.search_information(info_dict,{},{})
        self.click_button_for_more_than_one(u'查看',3)
        result=self.get_text_info(u'单据编号：')
        self.assert_result_equal(order_code,result,u'已出库-查看')
