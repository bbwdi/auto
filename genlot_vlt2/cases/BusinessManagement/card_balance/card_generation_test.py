# -*- coding:utf-8 -*-

from setting import *
import unittest
from time import sleep
from common.base_class_province import Test
from pages.Business_management.card_balance_page.card_generation_page import CardGenerationPage


class CardGenerationTest(Test,CardGenerationPage):
    '''投注卡生成测试'''



    def test_card_generation_add(self):
        '''投注卡新增'''
        select_sql=u"select * from T_CARD_INFO where batch='%s'"
        info_list=[u'安徽省',u'合肥市',u'投注卡',2,u'卡片生成,测试投注卡新增']
        self.open_card_generation()
        self.input_card_generation_add_info(info_list)
        self.click_button_for_one(u'确 定')
        tips=self.get_tips()
        batch_id=self.get_table_cell_text(1,2)
        num=self.get_data_count(select_sql %batch_id)
        self.assert_result_equal(info_list[3],num,u'投注卡新增')
        self.assert_result_equal(u'操作成功',tips,u'投注卡新增')
        self.click_button_for_one(u'展开')
        self.search_information({u'请输入批次':batch_id},{u'请选择投注卡类型':u'投注卡'},{})
        self.click_table_cell_operation_button(1,7,3,3)#注销
        self.click_button_for_one(u'确定')
        sleep(5)

    #@unittest.skip(u'跳过测试')
    def test_generation_add(self):
        '''投注卡新增'''
        self.card_generation_add()
        sleep(10)

    def test_card_generation_search(self):
        '''投注卡查询'''
        select_sql=u"select * from T_CARD_INFO where batch='%s'"
        self.open_card_generation()
        batch_num=self.get_table_cell_text(1,2)
        card_count=int(self.get_table_cell_text(1,5))
        info_list=[batch_num,u'',u'',u'',u'']
        self.search_card_generation(info_list)
        search_text=self.get_search_text()
        db_count=self.get_data_count(select_sql %batch_num)
        print(card_count,db_count)
        self.assert_result_equal(card_count,db_count,u'投注卡查询')
        self.assert_result_equal(info_list[0],search_text,u'投注卡查询')
        sleep(5)

    def test_card_generation_reset(self):
        '''投注卡重置'''
        self.open_card_generation()
        batch_num=self.get_table_cell_text(1,2)
        info_list=[batch_num,u'',u'',u'',u'']
        self.search_card_generation(info_list)
        count_one=self.get_search_count(u'共搜索到')
        self.click_button_for_one(u'重置')
        self.click_button_for_one(u'查询')
        sleep(3)
        count_reset=self.get_search_count(u'共搜索到')
        self.assert_result_not_equal(count_one,count_reset,u'投注卡重置')

    def test_card_generation_detail(self):
        '''投注卡查看详情'''
        self.open_card_generation()
        batch_num=self.get_table_cell_text(1,2)
        info_list=[batch_num,u'',u'',u'',u'']
        self.search_card_generation(info_list)
        self.click_table_cell_operation_button(1,7,1,3)
        detail_text=self.get_text_info(u'批次：')
        print(detail_text)
        self.assert_result_equal(info_list[0],detail_text,u'投注卡查看')

    def test_card_generation_export(self):
        '''投注卡导出'''
        file_name=download_path + u'投注卡生成信息.xls'
        self.open_card_generation()
        batch_num=self.get_search_text(2)
        info_list=[batch_num,u'',u'',u'',u'']
        self.search_card_generation(info_list)
        self.click_table_cell_operation_button(1,7,2,3)
        result=self.get_download_file_and_clear(file_name)
        self.assert_result_equal(True,result,u'投注卡导出')


    def test_card_generation_cancel(self):
        '''投注卡注销'''
        select_sql=u"select is_delete from T_CARD_INFO where batch='%s'"
        search_list=[u'',u'中福彩',u'安徽省',u'合肥市',u'',1]
        add_list=[u'安徽省',u'合肥市',u'投注卡',1,u'卡片生成,测试投注卡新增']
        self.open_card_generation()
        self.input_card_generation_add_info(add_list)
        self.click_button_for_one(u'确 定')
        sleep(3)
        self.click_button_for_one(u'展开')
        self.search_card_generation(search_list)
        batch_num=self.get_table_cell_text(1,2)
        self.search_card_generation([batch_num,u'',u'',u'',u''])
        self.click_table_cell_operation_button(1,7,3,3)#注销
        self.click_button_for_one(u'确定')
        sleep(1)
        tips=self.get_tips()
        delete=self.get_column_value(select_sql %batch_num)
        self.assert_result_equal(1,delete[0],u'投注卡注销')
        self.assert_result_equal(u'注销成功！',tips,u'投注卡注销')
        sleep(2)
        self.click_button_for_one(u'查询')
        search_count=self.get_footer_count_by_inside_text()
        self.assert_result_equal(u'0',search_count,u'投注卡注销')

if __name__=='__main__':
    unittest.main()