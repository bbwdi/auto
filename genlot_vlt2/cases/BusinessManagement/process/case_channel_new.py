# coding:utf-8
from __future__ import division
from common.login_b import Test
from pages.process import Process
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
        object = Process(self.driver)
        object.skip()
        time.sleep(2)
        object.get_text_obscure('渠道新建').click()
        time.sleep(2)

        #生成唯一ID
        unique_id = str(object.create_id())
        #所属机构
        object.option_text('请选择所属机构').click()
        object.click_radio('新疆')
        #渠道类型
        object.get_text_obscure('渠道类型').click()
        time.sleep(2)
        object.option_text('请选择渠道类型').click()
        object.get_text_list('自营厅')
        #渠道编号
        channel_code = unique_id
        object.input_text('渠道编号',channel_code)
        #渠道等级
        object.option_text('请选择渠道等级').click()
        object.get_text_obscure('一级').click()
        #经营场所属性
        object.option_text('请选择经营场所属性').click()
        object.get_text_obscure('自有').click()
        #销售厅面积
        sale_hall_area = 100
        object.input_text('销售厅面积',sale_hall_area)
        #销售厅面积
        sale_hall_area = 100
        object.input_text('销售厅面积',sale_hall_area)
        #渠道地址
        object.option_text('请选择省 / 市 / 区').click()
        object.get_text_list('新疆')
        object.get_text_list('乌鲁木齐市')
        object.get_text_list('天山区')
        #详细地址
        address = u'天山区111222'
        object.option_text('填写详细地址').send_keys(address)

        #姓名
        leader_name = u'销售厅经理'
        object.input_text('姓名',leader_name)
        #年龄
        age = 18
        object.input_text('年龄',age)
        #手机号码
        mobile = object.create_mobile()
        object.input_text('手机号码',mobile)
        #身份证号
        id_card = object.id_card()
        object.input_text('身份证号',id_card)
        #联系地址
        address = u'自动化测试地址'
        object.input_text('联系地址',address)
        #卡数量
        card_number = 10
        object.option_text('请输入数量').send_keys(card_number)
        #收费
        card_fee = 100
        object.option_text('请输入金额').send_keys(card_fee)
        #销售游戏
        object.get_text_obscure('禁止').click()
        object.get_text_obscure('禁止').click()
        #销售时间
        object.option_text_list('开始时间')
        #选择资源类型
        object.option_text('请选择资源类型').click()
        object.get_text_obscure('设备').click()
        #选择资源名称
        object.option_text('请选择资源名称').click()
        object.get_text_obscure('终端机').click()
        #选择资源名称
        object.option_text('请选择资源名称').click()
        object.get_text_obscure('终端机').click()



if __name__ == '__main__':
    unittest.main()
