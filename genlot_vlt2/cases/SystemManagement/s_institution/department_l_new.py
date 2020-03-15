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
        object = System(self.driver)
        object.skip()
        time.sleep(2)
        object.get_text_obscure('组织架构').click()
        time.sleep(2)
        object.get_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/ul/li[2]/li/li[4]/ul/li/li/span').click()

        time.sleep(2)
        object.get_text_obscure('中福彩').click()
        object.get_text_obscure('添加部门').click()

        #生成唯一ID
        id = str(object.create_id())
        dep_name = u'自动化测试部门' + id
        object.input_text('部门名称',dep_name)
        #部门负责人
        user_name = u'部门负责人' + id
        object.input_text('部门负责人',user_name)
        #负责人电话
        user_mobile = u'13534075566'
        object.input_text('负责人电话',user_mobile)
        #备注
        desc = u'备注' + dep_name
        object.input_text('备注',desc)
        #状态
        try:
            object.get_text_accurate('关闭').click()
        except:
            object.get_text_obscure('提交并保存').click()
        else:
            object.get_text_obscure('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select department_name,principal,principal_mobile,remark,status from T_DEPT_INFO where department_name='%s'
    	'''%dep_name
        db = Oracle()
        result = db.run_sql(sql)

        object.assert2(result[0],dep_name,u'部门名称')
        object.assert2(result[1],user_name,u'部门负责人')
        object.assert2(result[2],user_mobile,u'负责人电话')
        object.assert2(result[3],desc,u'备注')
        object.assert2(result[4],1,u'状态')








if __name__ == '__main__':
    unittest.main()
