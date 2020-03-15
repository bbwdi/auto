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

        role.get_text_obscure('新建角色').click()
        #生成唯一ID
        role_code = str(role.create_id())
        role.input_text('角色编码',role_code)
        role_name = u'自动化测试角色' + str(role_code)
        role.input_text('用户角色',role_name)
        role_desc = u'自动化测试角色描述' + str(role_code)
        role.input_text('描述',role_desc)
        role.get_text_obscure('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select role_code,role_name,role_desc,status from t_role_info where role_code='%s'
    	'''%role_code
        db = Oracle()
        result = db.run_sql(sql)

        role.assert2(result[0],role_code,u'角色编码')
        role.assert2(result[1],role_name,u'角色名称')
        role.assert2(result[2],role_desc,u'角色描述')
        role.assert2(result[3],1,u'角色状态')








if __name__ == '__main__':
    unittest.main()
