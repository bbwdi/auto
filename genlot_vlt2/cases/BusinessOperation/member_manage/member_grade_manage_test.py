# -*- coding:utf-8 -*-

import unittest
from time import sleep

from common.base_class_province import Test
from pages.Business_operation.member_manage_page.member_grade_manage_page import MemberGradeManagePage


class MemberGradeManageTest(Test,MemberGradeManagePage):
    '''会员积分管理'''

    @unittest.skip(u"跳过测试")
    def test_member_grade_start_and_stop(self):
        '''会员等级启用-冻结'''
        self.open_member_grade_management()
        attr=self.get_button_attribute(u'启用',u'disabled')
        if attr:
            self.stop_status()
            stop_tips=self.get_tips()
            self.assert_result_equal(u'操作成功',stop_tips,u'会员等级-冻结')
            sleep(2)
            self.start_status()
            start_tips=self.get_tips()
            self.assert_result_equal(u'操作成功',start_tips,u'会员等级-启用')
        else:
            self.start_status()
            start_tips=self.get_tips()
            print(start_tips)
            self.assert_result_equal(u'操作成功',start_tips,u'会员等级-启用')
            sleep(2)
            self.stop_status()
            stop_tips=self.get_tips()
            self.assert_result_equal(u'操作成功',stop_tips,u'会员等级-冻结')


    def test_member_grade_check_detail(self):
        '''会员等级查看详情'''
        self.open_member_grade_management()
        self.click_button_for_more_than_one(u'查看',2)
        self.click_button_for_one(u'返 回')
        sleep(1)
        self.click_button_for_more_than_one(u'查看',2)
        self.click_button_for_one(u'下一步')
        self.click_button_for_more_than_one(u'上一步',1)
        sleep(1)
        self.click_button_for_more_than_one(u'下一步',1)
        self.click_button_for_more_than_one(u'下一步',2)
        self.click_button_for_more_than_one(u'上一步',2)
        sleep(1)
        self.click_button_for_more_than_one(u'下一步',2)
        sleep(1)
        detail_num=self.get_search_text()
        print(detail_num)
        self.assert_result_in(u'level',detail_num,u'查看详情')
        self.click_button_for_one(u'返回首页')
        sleep(1)
        case_text=self.get_search_text(1)
        print(case_text)
        self.assert_result_equal(u'会员等级方案',case_text,u'查看详情')
        sleep(5)

    @unittest.skip(u"跳过测试")
    def test_member_grade_edit(self):
        '''会员等级编辑'''
        info_list=[u'会员等级方案',u'方案简介（会员级别有6级，成长需要靠会员成长值，每级会员的权益都不一样，详情请电话咨询）',u'白银',500]
        self.open_member_grade_management()
        attr=self.get_button_attribute(u'编辑',u'disabled')
        if attr:
            self.click_button_for_more_than_one(u'冻结',2)
            self.click_button_for_more_than_one(u'确定',2)
            sleep(2)
        else:
            pass
        self.click_button_for_more_than_one(u'编辑',2)
        self.input_text_message_for_outside_text(u'方案名称',info_list[0])
        self.input_text_message_for_outside_text(u'方案简介',info_list[1])
        self.click_button_for_more_than_one(u'下一步',1)
        self.click_button_for_more_than_one(u'下一步',2)
        self.click_button_for_more_than_one(u'编辑',2)
        sleep(1)
        self.input_text_message_for_outside_text(u'等级名称',info_list[2])
        self.input_text_message_for_outside_text(u'成长值范围',info_list[3])
        self.click_button_for_one(u'保存')
        self.click_button_for_one(u'完成')
        sleep(5)

if __name__=='__main__':
    unittest.main()