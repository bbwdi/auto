# -*- coding:utf-8 -*-

from setting import *
import unittest
from time import sleep

from common.base_class_province import Test
from pages.Business_management.game_store_manage_page.game_list_page import GameListPage

@unittest.skip(u"跳过测试")
class gameListTest(Test,GameListPage):
    '''游戏列表测试'''


    #@unittest.skip(u"跳过测试")
    def rtest_game_add(self):
        '''新建游戏'''
        update_package=game_path + u'xykp_2-update-VLT01-01.00.04.tar.gz'
        system_package=game_path + u'xykp_2-system-VLT01-01.00.04.tar.gz'
        jar_package=game_path + u'vlt-xykp_2-genlot_161.jar'
        annex_name=upload_path + u'游戏需要配置属性.docx'
        config_code=self.get_role_number(config_number_file)
        name_num=self.get_role_number(name_number_file)
        game_name=[u'幸运卡牌_auto',u'多福多宝_auto',u'深海探宝_auto',u'美食奇缘_auto']
        name=game_name[0] + str(name_num)
        prize_id=int(u'1021') + name_num
        print(name,prize_id)
        choose_dict={u'请选择游戏类型':u'概率型'}
        info_dict={u'请输入游戏名称':name,
                   u'请填写游戏规则介绍':u'抽大奖',
                   u'请输入版权归属':u'auto',
                   u'请输入开发商名称':u'穗彩',
                   u'请输入联系人':u'zxl',
                   u'请输入手机号码':u'13568956862',
                   u'请输入电子邮箱':u'568505593@qq.com'
                  }
        game_config_dict={u'请输入配置编码':config_code,
                          u'请输入金额':u'1',
                          u'请输入数量':u'100',
                          u'请输入中福彩发行费比率':u'5',
                          u'请输入中福彩公益金比率':u'5',
                          u'请输入省福彩发行费比率':u'5',
                          u'请输入省福彩公益金比率':u'5',
                          u'请输入市福彩发行费比率':u'4',
                          u'请输入市福彩公益金比率':u'5',
                          u'请输入销售厅发行费比率':u'3',
                          u'请输入销售厅公益金比率':u'3',
                          u'请输入固定返奖率':u'59.9',
                          u'请输入奖池返奖率':u'5',
                          u'请输入调节基金比率':u'0.1',
                          u'请输入奖池ID':prize_id,
                          u'请输入奖池名称':u'auto_1021',
                          u'请输入初始化金额':u'0',
                          u'请输入单注最小金额':u'0.1',
                          u'请输入单注最大金额':u'1',
                          u'请输入最小投注数':u'1',
                          u'请输入最大投注数':u'5',
                          u'请输入档位数量':u'1',
                          u'请输入返奖率间隔':u'2',
                          u'请输入初始档位返奖率':u'23',
                          u'请输入最小档位返奖率':u'22',
                          u'请输入最大档位返奖率':u'24',
                          u'请输入游戏大奖金额':u'10000',
                          u'请输入游戏小奖金额':u'10000'
                          }
        remind_dict={u'兑奖提醒天数':u'30',u'弃奖天数':u'60'}
        game_desc_dict={u'请输入软件描述':u'幸运卡牌',u'请输入新版特性':u'增加七彩图案'}
        type_dict={u'请选择类型':u'新上市'}
        self.open_game_store_list()
        self.click_button_for_one(u'新建游戏')
        self.input_basic_game_info(info_dict,choose_dict)
        self.click_button_for_one(u'下一步')
        sleep(5)
        self.upload_file_for_more_than_one(2,update_package)
        sleep(15)
        self.upload_file_for_more_than_one(3,system_package)
        sleep(15)
        self.upload_file_for_more_than_one(4,jar_package)
        sleep(15)
        update_text=self.get_game_package_name_for_more_than_one(u'上传客户端游戏包',1)
        system_text=self.get_game_package_name_for_more_than_one(u'上传客户端游戏包',2)
        server_text=self.get_game_package_name_for_one(u'上传服务器游戏包')
        self.input_more_text_message_for_inside_text(game_desc_dict)
        print(update_text,system_text,server_text)
        self.click_button_for_more_than_one(u'下一步',2)
        self.input_more_text_message_for_inside_text(game_config_dict)
        self.input_more_text_message_for_outside_text(remind_dict)
        self.choose_more_option_by_inside_text(type_dict)
        for i in range(5,8):
            self.upload_file_for_more_than_one(i,annex_name)
        self.click_button_for_more_than_one(u'下一步',3)
        sleep(10)
        self.click_button_for_one(u'提 交')
        update_package_new=game_path + u'xykp_%s-update-VLT01-01.00.04.tar.gz' %name_num
        system_package_new=game_path + u'xykp_%s-system-VLT01-01.00.04.tar.gz'%name_num
        jar_package_new=game_path + u'vlt-xykp_%s-genlot_161.jar' %name_num
        tips=self.get_tips()
        if tips==u'提交成功':
            self.write_data_to_csv(game_name_file,game_name)
        os.rename(update_package,update_package_new)
        os.rename(system_package,system_package_new)
        os.rename(jar_package,jar_package_new)


    def test_game_add(self):
        self.game_add()
