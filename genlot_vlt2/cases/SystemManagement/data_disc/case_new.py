# coding:utf-8
from __future__ import division
from common.login_b import Test
from pages.system import System
from common.function import log_info
from common.function import save_screenshot
from common.function import get_csv_data
import time
import datetime
from db.oracle_db import Oracle
import unittest
import setting
import random

class Apply_a(Test):
     def test_apply_page(self):
        log_info(u"跳转到系统管理页面")
        object = System(self.driver)
        object.skip()
        object.get_text_list('数据字典')
        object.get_text_list('数据字典')

        object.get_text_obscure('新增字典').click()

        #生成唯一ID
        unique_id = str(object.create_id())
        disc_name = u'字典名称' + unique_id
        object.get_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/form/div[1]/div/div/input').send_keys(disc_name)
        #object.input_text('数据字典名称',disc_name)

        disc_key = u'字典键' + unique_id
        object.input_text('数据字典键',disc_key)

        disc_value = u'字典键值' + unique_id
        object.input_text('字典数据值',disc_value)

        disc_desc = u'描述' + unique_id
        object.input_text('描述',disc_desc)

        object.get_text_obscure('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select name,key,value,description,is_allow_delete from T_DICT_DATA where name='%s'
    	'''%disc_name
        db = Oracle()
        result = db.run_sql(sql)

        object.assert2(result[0],disc_name,u'字典名称')
        object.assert2(result[1],disc_key,u'字典键')
        object.assert2(result[2],disc_value,u'字典值')
        object.assert2(result[3],disc_desc,u'字典描述')
        object.assert2(result[4],1,u'状态')









if __name__ == '__main__':
    unittest.main()
