# -*- coding:utf-8 -*-

import unittest
from time import sleep
from setting import *
from db.oracle_db import *
from common.base_class_province import Test
from pages.base_page import BasePage
from pages.Business_operation.permission_maintain_page.role_manage_page import RoleListPage


class RoleListTest(Test,RoleListPage):
    '''角色管理-角色列表测试'''


    def test_role_manage_search(self):
        '''角色管理查询'''
        time_dict={u'开始日期':u'2019-12-16',u'结束日期':u'2020-12-30'}
        self.open_role_list()
        self.click_button_for_one(u'展开')
        role_name=self.get_table_cell_text(1,2)
        create_person=self.get_table_cell_text(1,6)
        info_dict={u'请输入创建人':create_person}
        choose_dict={u'请选择用户角色':role_name,u'请选择角色状态':u'启用'}
        self.search_information(info_dict,choose_dict,time_dict)
        tips=self.get_table_cell_text(1,2)
        self.assert_result_equal(role_name,tips,u'角色管理查询')

    #@unittest.skip(u"跳过测试")
    def test_role_manage_add(self):
        '''角色管理新增'''
        select_sql=u"select * from T_CHANNEL_ROLE_INFO where role_name='%s'"
        number=self.get_role_number(role_number_file)
        role_name=u'auto_%s' %number
        role_list=[role_name,u'否',u'新增用户测试']
        per_list=[u'投注卡管理',u'购卡充值',u'密码修改',u'退卡提现',u'我的申请']
        self.open_role_list()
        self.input_role_manage_add_info(role_list,per_list)
        sleep(1)
        tips=self.get_tips()
        count=self.get_data_count(select_sql %role_name)
        self.assert_result_equal(1,count,u'角色管理-新增')
        self.assert_result_equal(u'新增成功',tips,u'角色管理-新增')
        self.search_information({},{u'请选择用户角色':role_name},{})
        sleep(1)
        self.click_button_for_more_than_one(u'注销',1)
        self.click_button_for_more_than_one(u'确定',2)


    def test_role_status_start(self):
        '''角色状态-启用-冻结'''
        info_list=[u'auto-003']
        self.open_role_list()
        self.search_role(info_list)
        try:
            self.role_status_stop()
            tips=self.get_tips()
            stop=self.get_role_status(info_list[0])
            self.assert_result_equal(u'冻结',stop,u'角色状态-冻结')
            self.assert_result_equal(u'操作成功',tips,u'角色状态-冻结')
            sleep(2)
            self.role_status_start()
            tips=self.get_tips()
            start=self.get_role_status(info_list[0])
            self.assert_result_equal(u'启用',start,u'角色状态-启用')
            self.assert_result_equal(u'操作成功',tips,u'角色状态-启用')
        except:
            self.role_status_start()
            tips=self.get_tips()
            print(tips)
            start=self.get_role_status(info_list[0])
            print(start)
            self.assert_result_equal(u'启用',start,u'角色状态-启用')
            self.assert_result_equal(u'操作成功',tips,u'角色状态-启用')
            sleep(2)
            self.role_status_stop()
            tips=self.get_tips()
            stop=self.get_role_status(info_list[0])
            self.assert_result_equal(u'冻结',stop,u'角色状态-冻结')
            self.assert_result_equal(u'操作成功',tips,u'角色状态-冻结')

    #@unittest.skip(u'跳过测试')
    def test_role_status_cancel(self):
        '''角色状态注销'''
        number=self.get_role_number(role_number_file)
        role_name=u'auto-%s' %number
        role_list=[role_name,u'否',u'新增用户测试']
        per_list=[u'投注卡管理',u'购卡充值',u'密码修改',u'退卡提现',u'我的申请']
        self.open_role_list()
        self.input_role_manage_add_info(role_list,per_list)
        sleep(5)
        self.search_information({},{u'请选择用户角色':role_name},{})
        sleep(1)
        self.click_button_for_more_than_one(u'注销',1)
        self.click_button_for_more_than_one(u'确定',2)
        tips=self.get_tips()
        cancel_status=self.get_role_status(role_name)
        self.assert_result_equal(u'注销',cancel_status,u'角色状态-注销')
        self.assert_result_equal(u'操作成功',tips,u'角色状态-注销')


    def test_role_permisssion_edit(self):
        '''角色信息编辑'''
        search_list=[u'auto-003']
        permission_list=[u'投注卡管理',u'购卡充值',u'密码修改',u'退卡提现',u'失效申报',u'试玩卡购卡',u'我的申请']
        self.open_role_list()
        self.search_role(search_list)
        self.click_table_cell_operation_button(1,8,2)#点击编辑
        sleep(1)
        self.edite_role_info(permission_list)
        self.click_button_for_one(u'提 交')
        sleep(2)
        tips=self.get_tips()
        self.assert_result_equal(u'修改成功',tips,u'角色信息-编辑')

    def test_role_check_detail(self):
        '''查看角色详情'''
        search_info=[u'auto-003']
        self.open_role_list()
        self.search_role(search_info)
        self.click_table_cell_operation_button(1,8,1)
        sleep(1)
        role_text=self.get_text_info(u'用户角色：')
        print(role_text)
        self.assert_result_equal(u'auto-003',role_text,u'详情')
        sleep(5)


class RoleAccountTest(Test,BasePage):
    '''角色管理-角色账户测试'''


    def open_role_account(self,user_name='zxl_test',password='123456'):
        '''打开角色管理-角色账户界面'''
        role_account=[u'业务运营',u'角色管理',u'角色账户',u'展开']
        self.user_login(user_name,password)
        sleep(2)
        self.click_more_button_for_one(role_account)
        sleep(3)

    def get_and_input_search_info(self):
        '''获取并输入查询信息'''
        self.channel_code=self.get_table_cell_text(1,2)
        self.account_code=self.get_table_cell_text(1,3)
        self.account_name=self.get_table_cell_text(1,5)
        self.role_name=self.get_table_cell_text(1,7)
        self.identity_number=self.get_table_cell_text(1,8)
        text_dict={u'请输入渠道编号':self.channel_code,u'请输入账户编号':self.account_code,u'请输入姓名':self.account_name}
        choose_dict={u'请选择账户状态':u'启用中',u'请选择角色名称':self.role_name}
        time_dict={u'开始日期':u'2019-12-01',u'结束日期':u'2020-12-31'}
        self.search_information(text_dict,choose_dict,time_dict)

    def test_role_account_search(self):
        '''角色账户查询'''
        select_sql=u"select * from T_CHANNEL_FUND where account_name='%s' and channel_identity='%s'"
        self.open_role_account()
        self.get_and_input_search_info()
        search_text=self.get_table_cell_text(1,2)
        page_count=int(self.get_footer_count_by_inside_text())
        db_count=self.get_data_count(select_sql %(self.account_name,self.identity_number))
        self.assert_result_equal(page_count,db_count,u'角色账户-查询')
        self.assert_result_equal(self.channel_code,search_text,u'角色账户-查询')

    def test_role_account_check(self):
        '''角色账户查看'''
        self.open_role_account()
        self.get_and_input_search_info()
        self.click_table_cell_operation_button(1,10,1)#查看
        detail_text=self.get_text_info(u'账户编号：')
        self.assert_result_equal(self.account_code,detail_text,u'角色账户-查看')

    def test_role_account_reset(self):
        '''角色账户重置'''
        self.open_role_account()
        self.get_and_input_search_info()
        search_count=self.get_footer_count_by_inside_text()
        self.click_button_for_one(u'重置')
        self.click_search_button()
        reset_count=self.get_footer_count_by_inside_text()
        self.assert_result_not_equal(search_count,reset_count,u'角色账户-重置')



if __name__=='__main__':
    unittest.main()


