# coding:utf-8
from __future__ import division
from common.base_class_province import Test
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
        time.sleep(2)
        object.get_text_obscure('渠道业务管理').click()
        object.get_text_obscure('年度发展计划').click()

        log_info(u"删除新疆机构的当前年的数据")
        year = time.strftime('%Y',time.localtime(time.time()))
        sql = '''
           delete from T_DEVELOP_PLAN where plan_date = '%s' and ins_id = (select ins_id from t_ins_info where ins_name like '%s' )
    	'''%(year,'新疆%')
        db = Oracle()
        result = db.sql_delete(sql)

        object.get_text_obscure('新建发展计划').click()
        time.sleep(2)
        object.option_text('请选择所属机构').click()
        object.click_radio('新疆')

        #生成唯一ID
        unique_id = str(object.create_id())
        #省属新建销售厅数量
        province_sales_hall_new = unique_id
        object.input_text('省属新建销售厅数量',province_sales_hall_new)
        #省属销售厅投注机数量
        province_sales_machine_new = 20
        object.input_text('省属销售厅投注机数量',province_sales_machine_new)
        #省合作厅数量
        province_cooperate_amount = 30
        object.input_text('省合作厅数量',province_cooperate_amount)
        #省合作厅投注机数量
        province_cooperate_machine_amount = 40
        object.input_text('省合作厅投注机数量',province_cooperate_machine_amount)
        #发展预算金额
        develop_buget = 100
        object.input_text('发展预算金额',develop_buget)
        #计划说明
        plan_desc = u'说明'
        object.input_text('计划说明',plan_desc)

        object.get_text_obscure('提交并保存').click()

        log_info(u"检查数据")
        sql = '''
        select aa.NEW_SELLING_HALL , SELLING_MACHINE ,COOPERATION_HALL,COOPERATION_MACHINE,aa.DEVELOP_BUDGET,aa.plan_desc
        from T_DEVELOP_PLAN  aa
        left join t_ins_info bb on aa.ins_id = bb.ins_id
        where aa.ins_level = 1 and aa.plan_date = '%s'
    	'''%year
        db = Oracle()
        result = db.run_sql(sql)

        object.assert2(result[0],int(province_sales_hall_new),u'省属新建销售厅数量')
        object.assert2(result[1],province_sales_machine_new,u'省属销售厅投注机数量')
        object.assert2(result[2],province_cooperate_amount,u'省合作厅数量')
        object.assert2(result[3],province_cooperate_machine_amount,u'省合作厅投注机数量')
        object.assert2(result[4],develop_buget * 100,u'发展预算金额')
        object.assert2(result[5],plan_desc,u'计划说明')



if __name__ == '__main__':
    unittest.main()
