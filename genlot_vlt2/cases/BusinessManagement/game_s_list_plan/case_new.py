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
        time.sleep(2)
        object.get_text_obscure('游戏发行管理').click()
        time.sleep(2)
        object.get_text_obscure('游戏上市计划').click()
        time.sleep(5)
        object.get_text_obscure('新建上市计划').click()

        #生成唯一ID
        unique_id = str(object.create_id())
        #上市计划名称
        plan_name = unique_id
        object.input_text('上市计划名称',plan_name)
        #上市时间
        start_time = object.next_day()
        object.input_text('上市时间',start_time)
        #上市计划简介
        plan_desc = u'上市计划简介'
        object.input_text('上市计划简介',plan_desc)
        #上市游戏
        object.get_text_accurate('上市计划简介').click()
        object.option_text('请选择上市游戏').click()
        object.get_text_obscure('自动化游戏名字').click()
        #销售区域
        object.option_text('请选择销售区域').click()
        object.click_radio('中福彩')
        object.get_text_obscure('下一步').click()

        #消费模式
        time.sleep(2)
        object.option_text('请选择消费模式').click()
        object.get_text_obscure('账户余额').click()
        #兑奖权限
        object.option_text('请选择兑奖权限').click()
        object.get_text_list('启用')
        #销售权限
        object.option_text('请选择销售权限').click()
        object.get_text_list('启用')
        #Jackpot比率
        Jackpot = 10
        object.input_text('Jackpot比率',Jackpot)
        #返奖比率
        return_prize_rate = 20
        object.input_text('返奖比率',return_prize_rate)
        #货币名称
        money_name = u'RMB'
        object.input_text('货币名称',money_name)
        #调节基金比率
        adjust_fund_ratio = 30
        object.input_text('调节基金比率',adjust_fund_ratio)
        #奖池比率
        reward_pool_ratio = 22
        object.input_text('奖池比率',reward_pool_ratio)
        #游戏兑换比例
        game_exchange_rate = 100
        object.input_text('游戏兑换比例',game_exchange_rate)
        #防沉迷
        object.get_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[1]/div[2]/div/div/div/form/div[10]/div/div/div/input').click()
        object.get_text_list('启用')
        #单次时长
        single_time_duration = 15
        object.input_text('单次时长',single_time_duration)
        #单日限额
        single_day_limit = 1000
        object.input_text('单日限额',single_day_limit)
        #游戏规则
        game_rule_desc = u'自动化游戏规则描述'
        object.input_text('游戏规则',game_rule_desc)


        #单注最小金额
        minimum_amount = 1
        object.input_text('单注最小金额',minimum_amount)
        #最小投注数
        minimum_number_bets = 2
        object.input_text('最小投注数',minimum_number_bets)
        #单注最大金额
        max_amount = 500
        object.input_text('单注最大金额',max_amount)
        #最大投注数
        max_number_bets = 5
        object.input_text('最大投注数',max_number_bets)
        #单次加注金额1
        single_filling_amount1 = 10
        object.input_text('单次加注金额1',single_filling_amount1)

        #资金规则
        #总发行经费占比
        ratio_total_issuance_funds = 10
        object.input_text('总发行经费占比',ratio_total_issuance_funds)
        #总公益金占比
        total_social_welfare_fund_ratio = 20
        object.input_text('总公益金占比',total_social_welfare_fund_ratio)
        #中福彩发行费占比
        china_lottery_issuance_fee_ratio = 22
        object.input_text('中福彩发行费占比',china_lottery_issuance_fee_ratio)
        #中福彩公益金占比
        china_welfare_lottery_public_interest_ratio = 23
        object.input_text('中福彩公益金占比',china_welfare_lottery_public_interest_ratio)
        #省福彩发行费占比
        provincial_welfare_lottery_issuance_fee_ratio = 24
        object.input_text('省福彩发行费占比',provincial_welfare_lottery_issuance_fee_ratio)
        #省福彩公益金占比
        provincial_welfare_lottery_commonwealth_ratio = 25
        object.input_text('省福彩公益金占比',provincial_welfare_lottery_commonwealth_ratio)
        #市福彩发行费占比
        city_welfare_lottery_issuance_fee_ratio = 26
        object.input_text('市福彩发行费占比',city_welfare_lottery_issuance_fee_ratio)
        #市福彩公益金占比
        city_welfare_lottery_commonwealth_ratio = 27
        object.input_text('市福彩公益金占比',city_welfare_lottery_commonwealth_ratio)
        #销售厅发行费占比
        hall_welfare_lottery_issuance_fee_ratio = 28
        object.input_text('销售厅发行费占比',hall_welfare_lottery_issuance_fee_ratio)
        #销售厅公益金占比
        hall_welfare_lottery_commonwealth_ratio = 29
        object.input_text('销售厅公益金占比',hall_welfare_lottery_commonwealth_ratio)
        #风控规则
        #最低中奖金额
        minimum_winning_amount = 30
        object.input_text('最低中奖金额',minimum_winning_amount)
        #最低返奖率
        minimum_return_rate = 31
        object.input_text('最低返奖率',minimum_return_rate)
        #最高中奖金额
        max_winning_amount = 10000
        object.input_text('最高中奖金额',max_winning_amount)
        #最高返奖率
        max_return_rate = 60
        object.input_text('最高返奖率',max_return_rate)
        #最低奖池金额
        min_prize_pool_amount = 61
        object.input_text('最低奖池金额',min_prize_pool_amount)
        #最高奖池金额
        max_prize_pool_amount = 20000
        object.input_text('最高奖池金额',max_prize_pool_amount)
        #最低销量
        min_sales_volume = 100
        object.input_text('最低销量',min_sales_volume)
        #最高销量
        max_sales_volume = 100000
        object.input_text('最高销量',max_sales_volume)
        #最低开机率
        min_power_rate = 10
        object.input_text('最低开机率',min_power_rate)
        #最低在线数量
        min_online = 20
        object.input_text('最低在线数量',min_online)
        #自动兑奖--最大兑奖金额
        max_auto_return = 1000
        object.get_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[6]/div[2]/div'
                                    '/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/input').send_keys(max_auto_return)
        #柜台兑奖--最大兑奖金额
        max_bar_return = 20000
        object.get_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[6]/div[2]/div'
                                    '/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/input').send_keys(max_bar_return)
        #兑奖处兑奖--最大兑奖金额
        max_cash_prize = 200000
        object.get_element_by_xpath('//*[@id="main"]/div/div/div[3]/div/div[6]/div[2]/div'
                                    '/div/div/div[3]/table/tbody/tr[3]/td[3]/div/div/input').send_keys(max_cash_prize)

        object.get_text_list('下一步')
        object.get_text_obscure('提 交').click()

if __name__ == '__main__':
    unittest.main()
