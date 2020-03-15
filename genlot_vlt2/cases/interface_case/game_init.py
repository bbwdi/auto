#coding=utf-8
from interface_common import commonfunc
from interface_common.request import Request
import json
import logging
from cases.interface_case.member_login import  MemberLogin


class Game_Init(Request):
    def test_game_init_normal(self):
        '''游戏初始化成功'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("游戏初始化", 1)
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            token=a.MemberLoginbypublic(1)
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s"%token}
            print  result[2]
            # 获取接口返回结果
            returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
            returnresult = json.loads(returnresult)  # 将返回结果变成字典
            print returnresult
            self.assertEquals(returnresult["msg"], testmsg)

        except Exception as e:
            logging.error(e)
            commonfunc.print_error(e)

    def test_game_init_normal_eror(self):
        '''游戏初始化失败，gameid不对'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("游戏初始化", 2)
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            token=a.MemberLoginbypublic(1)#调用彩民登陆，拿token
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s"%token}
            print  result[2]
            # 获取接口返回结果
            returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
            returnresult = json.loads(returnresult)  # 将返回结果变成字典
            self.assertEquals(returnresult["msg"], testmsg)#断言返回结果符合预期
        except Exception as e:
            logging.error(e)
    def test_game_init_normal_eror1(self):
        '''游戏初始化失败，token不对'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("游戏初始化", 3)
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            token=a.MemberLoginbypublic(1)+'a' '''#调用彩民登陆，拿token'''
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s"%token}
            print  result[2]
            # 获取接口返回结果
            returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
            returnresult = json.loads(returnresult)  # 将返回结果变成字典
            self.assertEquals(returnresult["msg"], testmsg)#断言返回结果符合预期
        except Exception as e:
            logging.error(e)

    def test_game_init_canshu(self,token):
        '''游戏初始化成功'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("游戏初始化", 1)#获取游戏初始化页签 第一行数据
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            # token=a.test_MemberLogin()
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s"%token}
            print  result[2]
            # 获取接口返回结果
            returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
            print returnresult
            self.assertEquals(returnresult["msg"], testmsg)

        except Exception as e:
            logging.error(e)
            commonfunc.print_error(e)

    def runTest(self):
        pass