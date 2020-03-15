# -*- coding:utf-8 -*-

from time import sleep
from setting import *
from pages.Business_management.game_store_manage_page.game_list_page import GameListPage


class GamePublicPlanPage(GameListPage):
    '''游戏上市计划'''



    def open_game_public_plan(self):
        '''打开游戏上市计划页面'''
        public_list=[u'业务管理',u'游戏发行管理',u'游戏上市计划',u'展开']
        self.user_login()
        sleep(2)
        self.click_more_button_for_one(public_list)
        sleep(2)

    def input_plan_info(self,plan_info,choose_dict,time_dict):
        '''输入计划信息'''
        self.click_button_for_one(u'新建上市计划')
        sleep(1)
        self.input_more_text_message_for_inside_text(plan_info)
        self.choose_more_option_by_inside_text(choose_dict)
        self.open_list_menu_by_inside_text(u'请选择上市时间')
        self.input_start_and_end_time(time_dict)
        self.open_list_menu_by_inside_text(u'请选择销售区域')
        self.choose_check_box_before_text_for_one(u'中福彩')
        self.click_browser_spacing()

    def operation_step(self):
        '''操作下一步'''
        self.click_button_for_one(u'下一步')
        self.click_table_cell_operation_button(1,9,1,3)
        sleep(1)
        self.click_button_for_more_than_one(u'下一步',2)
        sleep(1)
        self.click_button_for_more_than_one(u'下一步',2)
        self.upload_file_for_one(upload_path + u'test_upload.png')
        #self.click_button_for_one(u'提 交')

    def game_public_plan_add(self,game_name):
        '''统一的新增发布计划'''
        now_date=self.get_now_date()
        now_time=self.get_now_time()
        pl_num=self.get_plan_number(plan_number_file)
        plan_code=u'PL_%s' %pl_num
        plan_name=game_name
        plan_info={u'请输入计划编号':plan_code,
                   u'请输入计划名称':plan_name,
                   u'请输入上市计划简介':u'卡牌上市计划'
                   }
        plan_choose_dict={u'请选择游戏':game_name}
        time_dict={u'选择日期':now_date,u'选择时间':now_time}
        self.open_game_public_plan()
        self.input_plan_info(plan_info,plan_choose_dict,time_dict)
        self.operation_step()




