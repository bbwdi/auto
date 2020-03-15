# -*- coding:utf-8 -*-
from interface_common.request import Request
from interface_common.commonfunc import *
from cases.interface_case.Teller_login import teller_login
import json,re

class device_login(Request):
    def getdata_method(self, num, token=None):
        """获取excel里面的url，data"""
        self.result = read_excel_row(u'设备登录验证', num)
        self.url = self.result[1]
        self.data = self.result[2]
        if token == None:
            token = teller_login().test_tellerLogin_success()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded", "token": token}


    def modify_data(self, channel=None, device=None, serial=None):
        """修改传参数据,返回修改后的字符串data"""
        l = self.data.split('&')
        if channel != None:
            l[0] = "channel=%s" % channel
        if device != None:
            l[1] = "device=%s" % device
        if serial != None:
            l[2] = "serial=%s" % serial
        self.data = '&'.join(l)
        self.data = self.data.encode("utf-8")
        print self.data

    def get_deviceinfo(self,device_name):
        """
        输入参数：设备名称
        生成参数：渠道编码self.channel_code、设备编码self.device_code、销售厅经理身份证后六位self.card
        """
        self.result2 = read_excel_row(u'柜员登录', 1)
        self.channel_no = re.findall('=(.*?)&',self.result2[2])[0]
        sql = """select a.serial,a.DEVICE_CODE,a.CHANNEL_ID from U_VLT_BMS.T_DEVICE a join U_VLT_BMS.T_GOODS_TYPE b 
        on a.ARTICLE_ID = b.ID join U_VLT_BMS.T_CHANNEL_INFO c on a.CHANNEL_ID = c.CHANNEL_ID 
        where c.channel_no = '%s' and b.goods_name = '%s'"""%(self.channel_no,device_name)
        result = self.check_database(sql)
        self.serial = result[0]
        self.device_code = result[1]
        self.channel_id = result[2]

    def test_activation_atm(self):
        """柜员机设备登录成功"""
        self.getdata_method(1)
        self.get_deviceinfo(u'柜员机')
        self.modify_data(self.channel_no,self.device_code,self.serial)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], u'交易成功')

    def test_activation_terminal(self):
        """终端机设备登录成功"""
        self.getdata_method(2)
        self.get_deviceinfo(u'终端机')
        self.modify_data(self.channel_no,self.serial,self.device_code)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], u'交易成功')

    def test_terminal_error(self):
        """设备不存在"""
        self.getdata_method(3)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], self.result[3])

    def test_channelno_error(self):
        """销售厅不存在"""
        self.getdata_method(4)
        result1 = self.sendMsg_POST(self.url,self.data, self.headers)
        text = json.loads(result1)
        self.assertEqual(text["msg"], self.result[3])
