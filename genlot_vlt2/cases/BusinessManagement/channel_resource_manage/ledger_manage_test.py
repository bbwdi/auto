# -*- coding:utf-8 -*-

import unittest
from time import sleep
from setting import *
from common.base_class_province import Test
from pages.Business_management.channel_resource_manage_page.ledger_manage_page import LedgerManagePage


class LedgerManageTest(Test,LedgerManagePage):
    '''台账管理测试'''

    def test_search_ledger(self):
        '''台账管理查询'''
        self.open_ledger_manage()
        self.click_button_for_one(u'展开')
        depot_name=self.get_table_cell_text(20,2)
        old_count=self.get_footer_count_by_inside_text()
        info_dict={u'请输入仓库名称':depot_name}
        choose_dict={u'请选择仓库类型':self.get_table_cell_text(20,3),u'请选择物品类型':u'设备'}
        choose_dict1={u'请选择物品名称':self.get_table_cell_text(20,4),u'请选择物品型号':self.get_table_cell_text(20,5)}
        self.search_information(info_dict,choose_dict,{})
        self.search_information({},choose_dict1,{})
        new_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(old_count,new_count,u'台账管理-查询')

    def test_ledger_reset(self):
        '''台账管理重置'''
        self.open_ledger_manage()
        self.click_button_for_one(u'展开')
        depot_name=self.get_table_cell_text(20,2)
        info_dict={u'请输入仓库名称':depot_name}
        choose_dict={u'请选择仓库类型':self.get_table_cell_text(20,3),u'请选择物品类型':u'设备'}
        choose_dict1={u'请选择物品名称':self.get_table_cell_text(20,4),u'请选择物品型号':self.get_table_cell_text(20,5)}
        self.search_information(info_dict,choose_dict,{})
        self.search_information({},choose_dict1,{})
        old_count=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_button_for_more_than_one(u'查询',1)
        new_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(old_count,new_count,u'台账管理-重置')

    def test_check_detail_ledger(self):
        '''台账管理查看详情'''
        self.open_ledger_manage()
        depot_name=self.get_table_cell_text(1,2)
        self.click_table_cell_operation_button(1,7,1,3)#查看台账明细
        detail_depot=self.get_table_cell_text(1,7)
        self.assert_result_equal(depot_name,detail_depot,u'台账管理-查看详情')

    def test_ledger_print(self):
        '''台账管理打印'''
        self.open_ledger_manage()
        self.click_button_for_one(u'打印当前')
        sleep(5)

    def test_ledger_export_present(self):
        '''台账管理导出当前'''
        file_path=download_path + u'台账管理数据.xls'
        self.open_ledger_manage()
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'台账管理-导出当前')

    def test_ledger_export_all(self):
        '''台账管理导出全部'''
        file_path=download_path + u'台账管理数据.xls'
        self.open_ledger_manage()
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'台账管理-导出全部')

    def test_ledger_detil_print(self):
        '''台账管理明细中的打印'''
        self.open_ledger_manage()
        self.click_table_cell_operation_button(1,7,1,3)#查看台账明细
        self.click_button_for_one(u'打印当前')
        sleep(10)

    def test_ledger_detail_export_present(self):
        '''台账管理明细中的导出当前'''
        file_path=download_path + u'台账明细数据.xls'
        self.open_ledger_manage()
        self.click_table_cell_operation_button(1,7,1,3)#查看台账明细
        sleep(1)
        self.click_button_for_one(u'导出当前')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'台账管理-导出当前')

    def test_ledger_detail_export_all(self):
        '''台账管理明细中的导出全部'''
        file_path=download_path + u'台账明细数据.xls'
        self.open_ledger_manage()
        self.click_table_cell_operation_button(1,7,1,3)#查看台账明细
        sleep(2)
        self.click_button_for_one(u'导出全部')
        result=self.get_download_file_and_clear(file_path)
        self.assert_result_equal(True,result,u'台账管理-导出当前')

    def test_ledger_detail_processes_detail(self):
        '''台账管理明细中的相关流程'''
        self.open_ledger_manage()
        self.click_table_cell_operation_button(1,7,1,3)#查看台账明细
        sleep(1)
        depot_name=self.get_table_cell_text(1,7)
        self.click_table_cell_operation_button(1,10,1,3)#相关流程
        check_name=self.get_text_info(u'出库仓库：')
        self.assert_result_equal(depot_name,check_name,u'明细中的相关流程')
        sleep(5)

    def test_ledger_detail_search_detail(self):
        '''台账管理明细中的查询'''
        time_dict={u'开始日期':u'2019-12-20',u'结束日期':u'2020-12-31'}
        self.open_ledger_manage()
        self.click_table_cell_operation_button(1,7,1,3)#查看台账明细
        sleep(1)
        outbound=self.get_table_cell_text(1,5)
        self.search_information({},{u'请选择出入库类型':outbound},time_dict)
        search_text=self.get_table_cell_text(1,5)
        self.assert_result_equal(outbound,search_text,u'台账管理明细中的查询')


if __name__=='__main__':
    unittest.main()