#coding=utf-8
from interface_common import commonfunc
from interface_common.request import Request
import json
import logging
from cases.interface_case.member_login import  MemberLogin

class Gamr_Configuration(Request):
    def test_game_configuration(self):
        '''获取游戏配置参数成功'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("获取游戏配置参数", 1)
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            token=a.MemberLoginbypublic(1)  # 调用彩民登陆，拿token
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s" % token}
            print  result[2]
            data1={}
            # 获取接口返回结果
            returnresult = self.sendMsg_GET(getData=data1,url=testurl,  headers=Headers)
            returnresult = json.loads(returnresult)  # 将返回结果变成字典
            self.assertEquals(returnresult["msg"], testmsg)  # 断言返回结果符合预期

        except Exception as e:
            logging.error(e)

    def test_game_configuration_error(self):
        '''获取游戏配置参数失败，gameid不对'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("获取游戏配置参数", 2)
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            token=a.MemberLoginbypublic(1)  # 调用彩民登陆，拿token
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s" % token}
            print  result[2]
            data1={}
            # 获取接口返回结果
            returnresult = self.sendMsg_GET(getData=data1,url=testurl,  headers=Headers)
            returnresult = json.loads(returnresult)  # 将返回结果变成字典
            self.assertEquals(returnresult["msg"], testmsg)  # 断言返回结果符合预期

        except Exception as e:
            logging.error(e)


    def test_game_configuration_error2(self):
        '''获取游戏配置参数失败，token不对'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("获取游戏配置参数", 3)
            testurl = result[1]
            testmsg = result[3]
            a=MemberLogin()
            token=a.MemberLoginbypublic(1)+"a"  # 调用彩民登陆，拿token
            Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s" % token}
            print  result[2]
            data1={}
            # 获取接口返回结果
            returnresult = self.sendMsg_GET(getData=data1,url=testurl,  headers=Headers)
            returnresult = json.loads(returnresult)  # 将返回结果变成字典
            self.assertEquals(returnresult["msg"], testmsg)  # 断言返回结果符合预期

        except Exception as e:
            logging.error(e)

    def runTest(self):
        pass