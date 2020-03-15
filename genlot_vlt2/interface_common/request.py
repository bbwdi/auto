#!/usr/bin/env python
#-*- coding:utf-8 -*-
from interface_common import commonfunc
from interface_common.commonfunc import *
from interface_common.commonfunc import print_info,traceback
from oracle_db import orcl_db
from socket import *
import struct
import sys
import setting
import unittest
import logging

reload(sys)
sys.setdefaultencoding("utf-8")
import requests,json

class Request(unittest.TestCase):
    def setUp(self):
        '''初始化url，headers'''
        # self.url = setting.URL_Login
        # self.headers = setting.headers
        # print_info('url:%s'%self.url)
        # print_info('headers:%s'%self.headers)

    # def send_msg(self,postData):
    #     try:
    #         print_info(u'执行：\n%s'%postData)
    #         postData = json.dumps(postData)             #转json
    #         URL_GetStationCurrency = setting.URL_GetStationCurrency
    #         # headers_GetStationCurrency =
    #         response = requests.post(url=URL_GetStationCurrency,data=postData,headers=self.headers).text  #获取返回信息
    #         print_info(u'返回的结果：\n%s\n\t'%response)
    #         return response
    #     except Exception,e:
    #         print traceback.print_exc()

    def sendMsg_POST(self,url,postData,headers):
        try:
            print_info(u'执行：\n%s'%postData)
            # postData_js = json.dumps(postData)   #对post方法而言，必须把字典格式的数据转为json后才能发起请求
            # data = json.dumps(params)
            # response = requests.post(url=self.url,data=postData,headers=self.headers).text #获取返回信息
            response = requests.post(url,data=postData,headers=headers).text #获取返回信息
            # requests.post()
            print_info(u'返回的结果：\n%s\n\t'%response)
            return response
        except Exception,e:
            print traceback.print_exc()

    def sendMsg_GET(self, getData, url, headers):
        try:
            print_info(u'执行：\n%s'%getData)
            # endpoint = "get"
            # url = ''.join([self.url, endpoint])   #这句有问题，舍弃；原因以后再查

            response = requests.get(url,headers=headers,params=getData).text

            # response = requests.get(url,headers=self.headers,params=getData).text
            # response = requests.get(url,headers=self.headers).text
            # response = requests.get(url).text

            print_info(u'返回的结果：\n%s\n\t'%response)
            return response
        except Exception,e:
            print traceback.print_exc()
    def check_database(self,sql):
        # 返回数据库查询到数据
        m = orcl_db()
        m.orcl_connect()
        data = m.run_sql(sql)
        m.orcl_close()
        return data

    def get_saletoken(self):
        # 获取柜员登录的token
        result = read_excel_row(u'柜员登录', 1)
        url = result[1]
        data = result[2]
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        logging.warn(url)
        print data
        print headers
        text = self.sendMsg_POST(url, data, headers)
        # text=requests.post(url=url, data=data, headers=headers).text
        print text
        return json.loads(text)["data"]

    def tearDown(self):
        pass
