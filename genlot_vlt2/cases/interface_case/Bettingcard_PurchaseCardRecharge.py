# -*- coding:utf-8 -*-
from interface_common.request import Request
from interface_common.commonfunc import *
from cases.interface_case.Teller_login import teller_login
import json,re
import random


class bettingcard_Purchasecardrecharge(Request):
    def getdata_method(self,num):
        """获取excel里面的url，data"""
        self.result = read_excel_row(u'投注卡购卡充值', num)
        self.url = self.result[1]
        self.data = self.result[2]
        token = teller_login().test_tellerLogin_success()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded", "token": token}


    def modify_data(self,code,name = None,phonenum=None,loginPassword=None,paytype=None,cashPassword=None,amount=None):
        """修改传参数据,返回修改后的字符串data"""
        l = self.data.split('&')
        l[0] = "code=%s"%code
        if phonenum != None:
            l[1] = "phonenum=%s"%phonenum
        if paytype != None:
            l[2] = "paytype=%s"%paytype
        if loginPassword != None:
            l[2] = "paytype=%s"%loginPassword
        if name != None:
            l[2] = "paytype=%s"%name
        if cashPassword != None:
            l[2] = "paytype=%s"%cashPassword
        if amount != None:
            l[2] = "paytype=%s"%amount
        self.data = '&'.join(l)
        self.data = self.data.encode("utf-8")

    def get_Bettingcard(self,ins_name):
        """获得待激活状态的投注卡号"""
        sql = """select a.CARD_NUMBER from U_VLT_BMS.T_BETTING_CARD_INFO a 
        left join U_VLT_BMS.T_INS_INFO b on a.INS_ID = b.INS_ID 
        WHERE a.CARD_STATUS = 1 and a.BETTING_CARD_TYPE=0 and b.INS_NAME = '%s' order by a.create_time desc"""%ins_name
        d = self.check_database(sql)
        card_code = d[0]
        return card_code

    def get_balance_amount(self,card_code):
        """获取投注卡对应的账户余额"""
        sql = """select (b.cash_amount+b.reward_amount) from U_PRODUCT_TRADE.T_BET_CARD a join
        U_PRODUCT_TRADE.T_PURSE b on a.PURSE_ID = b.PURSE_ID where a.CARD_CODE = %s"""%card_code
        r = self.check_database(sql)
        return r[0]

    def test_cash_recharge(self):
        """现金购卡充值成功"""
        ins_name = u'江西省'
        num = 1
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*?)&',self.data)
        amount = l[0]
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])


    def test_weixin_recharge(self):
        """微信购卡充值成功"""
        ins_name = u'江西省'
        num = 2
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*?)&',self.data)
        amount = l[0]
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])

    def test_zhifubao_recharge(self):
        """支付宝购卡充值成功"""
        ins_name = u'江西省'
        num = 3
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*?)&',self.data)
        amount = l[0]
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])

    def test_bank_recharge(self):
        """按银行卡购卡充值成功"""
        ins_name = u'江西省'
        num = 4
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*?)&',self.data)
        amount = l[0]
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])

    def test_member_recharge(self):
        """按会员账户购卡充值成功"""
        ins_name = u'江西省'
        num = 5
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*?)&',self.data)
        amount = l[0]
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])

    def test_dianzi_recharge(self):
        """按其他电子支付购卡充值成功"""
        ins_name = u'江西省'
        num = 6
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*?)&',self.data)
        amount = l[0]
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])

    def test_default_recharge(self):
        """按默认现金购卡充值成功"""
        ins_name = u'江西省'
        num = 7
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        l = re.findall('amount=(.*)',self.data)
        amount = l[0]
        print amount
        print type(amount)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        balance = self.get_balance_amount(card_code)
        self.assertEqual(text["msg"], u'交易成功')
        #验证充值金额是否等于数据库投注卡钱包的金额
        self.assertEqual(int(amount) ,balance)
        #验证充值金额是否等于接口返回参数中钱包的金额
        self.assertEqual(int(amount),text['data']['balance'])

    def test_input_negative(self):
        """充值金额输入负数"""
        ins_name = u'江西省'
        num = 8
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], self.result[3])

    def test_input_nonum(self):
        """充值金额输入非数字"""
        ins_name = u'江西省'
        num = 9
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        card_code = self.get_Bettingcard(ins_name)
        self.modify_data(card_code,phonenum)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], self.result[3])

    def test_Nonbet_card(self):
        """非投注卡购卡充值"""
        ins_name = u'江西省'
        num = 10
        sql = """select a.CARD_NUMBER from U_VLT_BMS.T_BETTING_CARD_INFO a 
        join U_VLT_BMS.T_INS_INFO b on a.INS_ID = b.INS_ID 
        WHERE a.CARD_STATUS = 1 and a.BETTING_CARD_TYPE!=0 and b.INS_NAME = '%s'"""%ins_name
        card = self.check_database(sql)[-1]
        phonenum = phoneNORandomGenerator()
        self.getdata_method(num)
        self.modify_data(card,phonenum)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], self.result[3])