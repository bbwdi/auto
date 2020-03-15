# -*-coding=utf-8 -*-

from common.base_class_province import Test
from pages.Business_management.game_public_mange_page.game_public_plan_page import GamePublicPlanPage
from time import sleep
from setting import *
import os
import unittest

@unittest.skip(u"跳过测试")
class PublicPlanTest(Test,GamePublicPlanPage):
    '''游戏上市计划'''


    #@unittest.skip(u"跳过测试")
    def rtest_game_public_plan_add(self):
        '''游戏上市计划新增'''
        now_date=self.get_now_date()
        now_time=self.get_now_time()

        plan_info={u'请输入计划编号':u'PL_%s',
                   u'请输入计划名称':u'幸运卡牌_auto',
                   u'请输入上市计划简介':u'上市计划'
                   }
        plan_choose_dict={u'请选择游戏':u'幸运卡牌-auto'}
        time_dict={u'选择日期':now_date,u'选择时间':now_time}
        self.open_game_public_plan()
        self.input_plan_info(plan_info,plan_choose_dict,time_dict)
        self.operation_step()
        sleep(5)

    def test_plan_add(self):
        '''游戏上市计划新增'''
        self.game_public_plan_add(u'幸运卡牌-auto')
        sleep(50)
