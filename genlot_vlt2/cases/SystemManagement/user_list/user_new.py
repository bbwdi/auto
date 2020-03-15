# coding:utf-8
from __future__ import division
from common.login_b import Test
from pages.user_manager import UserManager
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
        object = UserManager(self.driver)
        object.skip()

        object.get_text_obscure('新建用户').click()
        #生成唯一ID
        user_code = str(object.create_id())

        user_name = u'自动化测试名字' + str(user_code)
        object.input_text('姓名',user_name)
        object.input_text('用户账号',user_name)

        user_mobile = object.create_mobile()
        object.input_text('手机号码',user_mobile)

        user_mail = u'11@22.com'
        object.input_text('邮箱',user_mail)

        object.get_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[5]/div/div/div[1]/input').click()
        object.click_radio('中福彩')

        object.get_text_obscure('所属部门').click()
        object.get_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[6]/div/div/div[1]/input').click()
        object.click_radio('自动化测试部门')

        object.get_text_obscure('用户角色').click()
        object.get_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[8]/div/div/div[2]/input').click()
        object.get_text_obscure('自动化测试角色').click()

        object.get_text_obscure('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select user_name,account,mobile,email,user_status,cc.ins_name from t_user_info aa
        left join  t_user_ins bb on aa.user_id = bb.user_id
        left join  t_ins_info cc on cc.ins_id = bb.ins_id
        where account='%s'
    	'''%user_name
        db = Oracle()
        result = db.run_sql(sql)

        object.assert2(result[0],user_name,u'姓名')
        object.assert2(result[1],user_name,u'用户账号')
        object.assert2(result[2],user_mobile,u'手机号码')
        object.assert2(result[3],user_mail,u'邮箱')
        object.assert2(result[4],0,u'状态')
        object.assert2(result[5],u'中福彩',u'机构名称')








if __name__ == '__main__':
    unittest.main()
