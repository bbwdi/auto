#coding=utf-8
from interface_common import commonfunc
from interface_common.request import Request
import json
class MemberLogin(Request):

    def MemberLoginbypublic(self,num):
        '''彩民电子投注卡登陆失败，密码不正确'''
        # 获取excel中第N行数--用例
        try:
            result = commonfunc.read_excel_row("彩民登陆",num)
            testurl = result[1]
            testmsg = result[3]
            Headers = {"Content-Type": "application/x-www-form-urlencoded"}
            # 获取接口返回结果
            returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
            returnresult = json.loads(returnresult)
            self.assertEquals(returnresult["msg"],testmsg)#判断是否交易成功
            return returnresult["data"]["token"]
        except  Exception as  e:
             commonfunc.print_error(e)




    def test_MemberLogin_by_betcard(self):
        '''彩民投注卡登陆'''
        MemberLogin().MemberLoginbypublic(1)

    def test_MemberLogin_by_betcard_error(self):
        '''彩民投注卡登陆,密码错误'''
        MemberLogin().MemberLoginbypublic(3)

    def test_MemberLogin_by_memberOnLineCard(self):
        '''彩民电子投注卡登陆'''
        MemberLogin().MemberLoginbypublic(2)

    def test_MemberLogin_by_memberOnLineCard_error1(self):
        '''彩民电子投注卡登陆失败，密码不正确'''
        # 获取excel中第N行数--用例
        MemberLogin().MemberLoginbypublic(4)

    def test_MemberLogin_by_betcard_error1(self):
        '''彩民电子投注卡登陆失败，卡号不正确'''
        # 获取excel中第N行数--用例
        MemberLogin().MemberLoginbypublic(5)

    def test_MemberLogin_by_memberOnLineCard_error2(self):
        '''彩民电子投注卡登陆失败，卡号不正确'''
        # 获取excel中第N行数--用例
        MemberLogin().MemberLoginbypublic(6)




    def runTest(self):
        pass