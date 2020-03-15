# -*- coding=utf-8 -*-

from pages.base_page import BasePage
from setting import *
from time import sleep

class WarehouseManagePage(BasePage):
    '''入库管理'''

    def get_already_warehouse_cell_text(self,list_num,column_num):
        '''获取已入库表格文本'''
        cell_loc=u'//*[@id="pane-already"]/div[1]/div[3]/table/tbody/tr[%s]/td[%s]/div'
        return self.find_element_for_text(cell_loc %(list_num,column_num)).text

    def open_warehouse_manage(self,user_name=u'zxl_test',password=u'123456'):
        '''打开入库管理页面'''
        warehouse_list=[u'业务管理',u'渠道资源管理',u'出入库管理',u'入库管理']
        self.user_login(user_name,password)
        sleep(2)
        self.click_button_for_one(warehouse_list[0])
        sleep(2)
        self.click_more_button_for_one(warehouse_list[1:3])
        sleep(2)
        self.click_button_for_more_than_one(warehouse_list[3],2)
        sleep(3)

    def get_and_input_search_info(self):
        '''获取并输入查询信息'''
        sleep(1)
        self.order_code=self.get_table_cell_text(1,2)
        self.apply_title=self.get_table_cell_text(1,3)
        info_dict={u'请输入单据编号':self.order_code,u'请输入申请标题':self.apply_title}
        self.search_information(info_dict,{},{})

    def goods_warehouse(self,apply_title,sequence_list):
        '''入库管理-入库'''
        user_name=u'admin'
        password=u'123456'
        self.open_warehouse_manage(user_name,password)
        info_dict={u'请输入申请标题':apply_title}
        sequence_dict={u'请输入序列号':sequence_list}
        self.search_information(info_dict,{},{})
        self.click_table_cell_operation_button(1,8,1,3)#点击入库
        self.input_more_text_message_for_inside_text_more_than_one(sequence_dict)
        self.click_button_for_more_than_one(u'入库',6)
        print(u'入库完成')
        sleep(5)

class OutDepotManagePage(BasePage):
    '''出库管理'''


    def open_out_depot_manage(self):
        '''打开出库管理页面'''
        out_list=[u'业务管理',u'渠道资源管理',u'出入库管理',u'出库管理']
        self.user_login()
        sleep(2)
        self.click_button_for_one(out_list[0])
        sleep(2)
        self.click_more_button_for_one(out_list[1:3])
        sleep(2)
        self.click_button_for_one(out_list[3])
        sleep(3)

    def get_already_out_cell_text(self,list_num,column_num):
        '''获取已出库表格文本'''
        cell_loc=u'//*[@id="pane-already"]/div[1]/div[3]/table/tbody/tr[%s]/td[%s]/div'
        return self.find_element_for_text(cell_loc %(list_num,column_num)).text


    def get_and_input_search_info(self):
        '''获取并输入查询信息'''
        sleep(1)
        self.order_code=self.get_table_cell_text(1,2)
        self.apply_title=self.get_table_cell_text(1,3)
        info_dict={u'请输入单据编号':self.order_code,u'请输入申请标题':self.apply_title}
        self.search_information(info_dict,{},{})

    def goods_out_depot(self,apply_title):
        '''出库管理-出库'''
        self.open_out_depot_manage()
        info_dict={u'请输入申请标题':apply_title}
        info_dict={u'请输入申请标题':apply_title}
        self.search_information(info_dict,{},{})
        self.click_table_cell_operation_button(1,8,1,3)#点击出库
        sleep(5)
        #self.assert_result_equal(self.order_code,search_result,u'出库管理-查询')