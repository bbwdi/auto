# -*- coding:utf-8 -*-
from interface_common import mysql_db
from interface_common.request import Request
from interface_common.commonfunc import read_excel_row,print_error
import json,re

class teller_login(Request):
    def test_tellerLogin_success(self):
        #获取柜员登录的token
        result = read_excel_row(u'柜员登录',1)
        url =result[1]
        data = result[2]
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        l2 = re.findall('=(.*?)&',data)
        channel_no = l2[0]
        code = l2[2]
        #数据库查找出密码
        sql = """select a.password from U_VLT_BMS.T_CHANNEL_FUND a left join U_VLT_BMS.T_CHANNEL_INFO b on
                 a.channel_id = b.channel_id where a.account_code = '%s' and b.channel_no = '%s'"""%(code,channel_no)
        result1 = self.check_database(sql)
        password =result1[0]
        lt = data.split('&')
        lt[-1] = "password=%s" % password
        data = '&'.join(lt)
        text = self.sendMsg_POST(url,data,headers)
        try:
            self.assertEqual(json.loads(text)["msg"],u'交易成功')
            return json.loads(text)["data"]
        except BaseException as msg:
            print_error(msg)

    def runTest(self):
        pass

