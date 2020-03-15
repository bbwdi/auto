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
        log_info(u"跳转到角色列表页面")
        role = System(self.driver)
        role.skip()
        role.get_text_obscure('角色管理').click()
        role.get_text_obscure('角色列表').click()

        log_info(u"查询最新的数据")
        sql = '''
        select role_name,role_desc from (select * from t_role_info order by create_time desc ) aa where rownum =1
    	'''
        db = Oracle()
        result = db.run_sql(sql)
        role_name = unicode(result[0], 'utf-8')
        role_desc = unicode(result[1], 'utf-8')

        role.input_text('用户角色',role_name)
        role.get_text_accurate('查询').click()

        #检查序号
        role.assert2('1',role.row_check(1).text,u'序号')
        #检查用户角色
        role.assert2(role_name,role.row_check(2).text,u'用户角色')
        #检查角色描述
        role.assert2(role_desc,role.row_check(3).text,u'角色描述')




if __name__ == '__main__':
    unittest.main()
