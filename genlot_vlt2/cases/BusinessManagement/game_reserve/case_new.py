# coding:utf-8
from __future__ import division
from common.login_b import Test
from pages.service_manage import ServiceManage
from common.function import log_info
from common.function import save_screenshot
from common.function import get_csv_data
import time
import datetime
from db.oracle_db import Oracle
import unittest
import setting
import SendKeys

class Apply_a(Test):
     def test_apply_page(self):
        log_info(u"跳转到页面")
        object = ServiceManage(self.driver)
        object.skip()
        object.get_text_obscure('游戏储备管理').click()
        object.get_text_obscure('游戏储备列表').click()

        time.sleep(2)
        object.get_text_obscure('新建游戏').click()

        #生成唯一ID
        unique_id = str(object.create_id())
        #游戏名称
        game_name = u'自动化游戏名字' + unique_id
        object.input_text('游戏名称',game_name)
        #游戏编码
        game_code = unique_id
        object.input_text('游戏编码',game_code)
        #游戏类型
        object.option_text('请选择游戏类型').click()
        object.get_text_obscure('奖组型').click()
        #游戏奖池
        object.option_text('请选择游戏奖池').click()
        object.get_text_obscure('多奖池').click()
        #游戏简介
        game_desc = u'游戏简介自动化'
        object.input_text('游戏简介',game_desc)
        #版权归属
        game_version = u'自动化版权归属'
        object.input_text('版权归属',game_version)
        #开发商名称
        developer_name = u'自动化开发商名称'
        object.input_text('开发商名称',developer_name)
        #联系人
        person = u'自动化联系人'
        object.input_text('联系人',person)
        #手机号码
        mobile = object.create_mobile()
        object.input_text('手机号码',mobile)
        #电子邮箱
        email = u'11@22.com'
        object.input_text('电子邮箱',email)
        #传真电话
        fax_phone = u'11223344'
        object.input_text('传真电话',fax_phone)
        #联系地址
        address = u'2233445566'
        object.input_text('联系地址',address)

        object.get_text_obscure('下一步').click()
        #点击上传
        object.get_text_obscure('上传游戏包').click()
        object.get_text_obscure('点击上传').click()
        object.upload_file(r"E:\genlot_vlt\static\install\game-logic-luckycards-1.0.0.jar")
        #游戏图标
        time.sleep(10)
        object.get_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/form/div[2]/div/div/div[1]/i').click()
        #object.input_text_click('游戏图标')
        object.upload_file(r"E:\genlot_vlt\static\images\test.png")
        #软件名称
        object.input_text('软件名称',u'多福多宝')
        #版本名称
        object.input_text('版本名称',u'V1.0.0')
        #版本号
        object.input_text('版本号',u'100')
        #软件描述
        object.input_text('软件描述',unique_id)
        #新版特性
        object.input_text('新版特性',unique_id)

        object.get_text_list('下一步')
        object.get_text_obscure('提 交').click()

       #创建字典
        game_tpye = {u'奖组型':1,u'概率型':2}
        jackpot_type = {u'无奖池':1,u'单奖池':2,u'多奖池':3}

        log_info(u"检查数据")
        sql = '''
        	select game_name,game_code,game_type,jackpot_type,game_desc,game_genlot,bb.developer_name,bb.person,bb.cell_phone,bb.email,bb.fax_phone,bb.address from T_GAME_INFO aa
	       left join T_DEVELOPER_INFO bb on bb.id = aa.developer_id
	       where aa.game_code ='%s'
    	'''%game_code
        db = Oracle()
        result = db.run_sql(sql)

        object.assert2(result[0],game_name,u'游戏名称')
        object.assert2(result[1],game_code,u'游戏编码')
        object.assert2(result[2],game_tpye[u'奖组型'],u'游戏类型')
        object.assert2(result[3],jackpot_type[u'多奖池'],u'游戏奖池')
        object.assert2(result[4],game_desc,u'游戏简介')
        object.assert2(result[5],game_version,u'版权归属')
        object.assert2(result[6],developer_name,u'开发商名称')
        object.assert2(result[7],person,u'联系人')
        object.assert2(result[8],mobile,u'手机号码')
        object.assert2(result[9],email,u'电子邮箱')
        object.assert2(result[10],fax_phone,u'传真电话')
        object.assert2(result[11],address,u'联系地址')



if __name__ == '__main__':
    unittest.main()
