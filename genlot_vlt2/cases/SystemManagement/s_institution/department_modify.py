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
        time.sleep(2)
        #点击第一行的修改按钮
        object.row_check(8).click()

        #生成唯一ID
        dep_id = str(object.create_id())
        #部门负责人
        user_name = u'部门负责人' + dep_id
        object.input_text('部门负责人',user_name)
        #负责人电话
        user_mobile = u'13534075566'
        object.input_text('负责人电话',user_mobile)
        #备注
        desc = u'备注' + dep_id
        object.input_text('备注',desc)
        #状态
        try:
            #如果是关闭状态，点击关闭变成开启
            object.get_text_accurate('关闭').click()
        except:
            #如果不是关闭状态，点击开启变成关闭
            object.get_text_accurate('开启').click()
            object.get_text_obscure('提交并保存').click()
            #所以状态为0，关闭
            status = 0
        else:
            status = 1
            object.get_text_obscure('提交并保存').click()

        #根据部门名称，查询数据库数据
        sql = '''
        select principal,principal_mobile,remark,status from T_DEPT_INFO where principal='%s'
    	'''%user_name
        db = Oracle()
        result = db.run_sql(sql)

        #得到部门负责人
        user_name = unicode(result[0], 'utf-8')
        #得到负责人电话
        user_mobile = unicode(result[1], 'utf-8')
        #得到备注
        desc = unicode(result[2], 'utf-8')

        #检查
        object.assert2(result[0],user_name,u'部门负责人')
        object.assert2(result[1],user_mobile,u'负责人电话')
        object.assert2(result[2],desc,u'备注')
        object.assert2(result[3],status,u'状态')


if __name__ == '__main__':
    unittest.main()
