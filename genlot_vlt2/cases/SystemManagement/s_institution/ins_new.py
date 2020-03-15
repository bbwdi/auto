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
        log_info(u"跳转到页面")
        object = System(self.driver)
        object.skip()
        time.sleep(2)
        object.get_text_obscure('组织架构').click()
        time.sleep(2)
        object.get_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/ul/li[2]/li/li[4]/ul/li/li/span').click()

        time.sleep(2)
        object.get_text_obscure('中福彩').click()
        object.get_text_obscure('新增').click()

        log_info(u"删除香港机构的数据")
        sql = '''
        delete from T_INS_INFO where region_code=810000
    	'''
        db = Oracle()
        result = db.sql_delete(sql)

        #生成唯一ID
        unique_id = str(object.create_id())
        object.input_text('机构名称',u'香港')
        #机构编码
        ins_id = unique_id
        object.option_text('请输入机构编码').send_keys(ins_id)
        #区域
        object.option_text('请选择').click()
        object.get_text_obscure('香港特别行政区').click()
        #object.click_radio('香港特别行政区')
        #备注
        desc = u'备注' + unique_id
        object.input_text('备注',desc)

        object.get_text_obscure('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select ins_name,ins_code,region_code,remark from T_INS_INFO where ins_code='%s'
    	'''%ins_id
        db = Oracle()
        result = db.run_sql(sql)

        object.assert2(result[0],u'香港',u'机构名称')
        object.assert2(result[1],ins_id,u'机构编码')
        object.assert2(result[2],810000,u'地区编码')
        object.assert2(result[3],desc,u'备注')







if __name__ == '__main__':
    unittest.main()
