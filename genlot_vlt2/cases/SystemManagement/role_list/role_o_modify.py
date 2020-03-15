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
        select role_name,role_desc,role_code from (select * from t_role_info order by create_time desc ) aa where rownum =1
    	'''
        db = Oracle()
        result = db.run_sql(sql)
        role_name = unicode(result[0], 'utf-8')
        role_desc = unicode(result[1], 'utf-8')
        role_code = unicode(result[2], 'utf-8')

        role.input_text('用户角色',role_name)
        role.get_text_accurate('查询').click()


        try:
            role.get_text_accurate('启用').click()
        except:
            role.get_text_obscure('编缉').click()
        else:
            role.get_text_obscure('确定').click()
            role.get_text_obscure('编缉').click()

        #生成唯一ID
        role_code1 = str(role.create_id())

        role_name = u'自动化测试角色' + str(role_code1)
        role.input_text('用户角色',role_name)
        role_desc = u'自动化测试角色描述' + str(role_code1)
        role.input_text('描述',role_desc)
        role.get_text_accurate('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select role_code,role_name,role_desc,status from t_role_info where role_code='%s'
    	'''%role_code
        db = Oracle()
        result = db.run_sql(sql)

        role.assert2(result[0],role_code,u'角色编码')
        role.assert2(result[1],role_name,u'角色名称')
        role.assert2(result[2],role_desc,u'角色描述')
        role.assert2(result[3],0,u'角色状态')



if __name__ == '__main__':
    unittest.main()
