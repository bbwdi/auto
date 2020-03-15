#coding=utf-8
import time
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.base_page import BasePage
from pages.home1_page import Home_Page
import random
import os
import datetime
from  db.oracle_db import Oracle


title_path='''//*[@id="pane-1"]//input[@placeholder='请输入申请标题']'''
titlename=u'''autotest资源发放'''
warehouse_path='''//*[@id="pane-1"]//input[@placeholder='请选择入库仓库']'''
click_path='''//ul[@class='el-scrollbar__view el-select-dropdown__list']/li'''#选择仓库

add_path='''//*[@id="pane-1"]//button/span[text()='新增物品']'''
Resources1='''(//*[@id="pane-1"]//input[@placeholder='请选择物品名称'])[1]'''#点击资源类型第一行
Resources2='''(//*[@id="pane-1"]//input[@placeholder='请选择物品名称'])[2]'''#点击资源类型第二行
type1='''(//ul/li[@class='el-select-dropdown__item']/span[text()='终端机'])'''#设备第一行类型
type2='''(//ul/li[@class='el-select-dropdown__item']/span[text()='柜员机'])'''#设备第二行类型
serial='''(//*[@id="pane-1"]//input[@placeholder='请输入序列号'])[1]'''
serialnum='''gavin'''
clickModel1='''(//*[@id="pane-1"]//input[@placeholder='请选择物品型号'])[1]'''#点击第一行型号
clickModel2='''(//*[@id="pane-1"]//input[@placeholder='请选择物品型号'])[2]'''#点击第二行型号
Model1='''//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]/span'''#第一行型号
Model2='''(//div[@class='el-scrollbar']//ul/li[1])[9]'''#第二行型号
remake_path1='''(//*[@id="pane-1"]//input[@placeholder='请输入备注'])[1]'''
goodstype=u'''终端机'''
goodstype1=u'''柜员机'''
list1='''//ul[@class='el-scrollbar__view el-select-dropdown__list']'''
zdj='''//ul//span[text()='终端机']'''
gyj='''//ul//span[text()='柜员机']'''
reason_path='''(//*[@id="pane-1"]//textarea[@placeholder='请输入调拨说明'])'''
input1='''//*[@id="pane-1"]//em[text()='点击上传']'''
commit='''//*[@id="pane-1"]//span[text()='提交']'''
cancel_path='''//*[@id="pane-1"]//span[text()='取消']'''
zancun_path='''//*[@id="pane-1"]//span[text()='暂存']'''
ca='''//ul[@class='el-scrollbar__view el-select-dropdown__list']/li'''
remake=u'''备注信息year'''
money='''//*[@id="pane-1"]//input[@placeholder='合计金额']'''



class Provide(business_process):
    def title(self):
        '''申请标题 '''
        self.input_xpath(title_path,titlename)
        return  titlename

    def warehouse(self):
        '''仓库'''
        time.sleep(1)
        self.get_element_by_xpath(warehouse_path).click()
        time.sleep(0.5)
        tt=self.get_elements_by_xpath(click_path)
        tt1=len(tt)
        kk=self.randomnum(tt1)
        click_path1=self.xparh_join(click_path,kk)
        text=self.get_element_by_xpath(click_path1).text
        self.get_element_by_xpath(click_path1).click()

        return text

    def goodsname_zhongduanji(self):
        '''添加设备终端机'''
        self.get_element_by_xpath(add_path).click()
        self.get_element_by_xpath(Resources1).click()#加终端机
        tt=self.get_elements_by_xpath(list1)#加终端机
        tt1=len(tt)
        kk=self.xparh_join(list1,tt1)#加终端机，判断终端机在列表中是否存在
        text=self.get_element_by_xpath(kk).text
        if goodstype in text:
            # self.input_xpath(Resources1,goodstype)
            # self.get_element_by_xpath(Resources1).send_keys(goodstype)
            aa=self.get_elements_by_xpath(zdj)
            aa1=len(aa)
            bb=self.xparh_join(zdj,aa1)
            self.get_element_by_xpath(bb).click()
            time.sleep(1)
            return goodstype
        else:
            ss=self.get_elements_by_xpath(ca)
            hh=len(ss)
            ss1=self.xparh_join(ca,hh)
            text1=self.get_element_by_xpath(ss1).text
            self.get_element_by_xpath(ss1).click()
            return text1

    def goodsname_guiyuanji(self):
        '''添加设备柜员机'''
        self.get_element_by_xpath(add_path).click()
        self.get_element_by_xpath(Resources1).click()  # 加柜员机
        tt = self.get_elements_by_xpath(list1)  # 加柜员机
        tt1 = len(tt)
        kk = self.xparh_join(list1, tt1)  # 加柜员机，判断终端机在列表中是否存在
        text = self.get_element_by_xpath(kk).text
        if goodstype1 in text:
            # self.input_xpath(Resources1,goodstype)
            # self.get_element_by_xpath(Resources1).send_keys(goodstype)
            aa = self.get_elements_by_xpath(gyj)
            aa1 = len(aa)
            bb = self.xparh_join(gyj, aa1)
            self.get_element_by_xpath(bb).click()
            time.sleep(1)
            return goodstype1
        else:
            ss = self.get_elements_by_xpath(ca)
            hh = len(ss)
            ss1 = self.xparh_join(ca, hh)
            text1 = self.get_element_by_xpath(ss1).text
            self.get_element_by_xpath(ss1).click()
            return  text1

    def modle(self):
        '''选择型号'''
        time.sleep(1)
        self.get_element_by_xpath(clickModel1).click()
        zz=self.get_elements_by_xpath(Model1)
        zz1=len(zz)
        Model3=self.xparh_join(Model1,zz1)
        text= self.get_element_by_xpath(Model3).text
        self.get_element_by_xpath(Model3).click()#选择第一个，定位位置在最后一个
        return text

    def Remarks(self):
        '''备注'''
        self.input_xpath(remake_path1,remake)
        return remake

    def Money(self):
        '''合计金额'''
        time.sleep(2)
        kk=self.get_element_by_xpath(money).text
        return  kk

    def reason(self,xuyao=u'''没得办法，不够用罗'''):
        '''输入原因'''
        self.input_xpath(reason_path,xuyao)
        return  xuyao

    def appendix(self):
        '''添加附件'''
        self.get_element_by_xpath(input1).click()
        tt = os.path.abspath(os.path.join(os.getcwd(), "../../.."))
        pngpath = tt + r'''\static\images\test.png'''
        self.upload_file(pngpath)
        time.sleep(1)
        return pngpath

    def Submission(self):
        '''提交'''
        time.sleep(1)
        self.get_element_by_xpath(commit).click()

    def cancel(self):
        '''取消'''
        time.sleep(1)
        self.get_element_by_xpath(cancel_path).click()

    def zancun(self):
        time.sleep(1)
        self.get_element_by_xpath(zancun_path).click()

    def data(self):
        '''查询最新申请记录,数据库中是clob类型，需要只能在有效期内操作，转化成str，然后在转化成字典'''
        null = ''
        sql='''SELECT data FROM
	(SELECT  t.*  FROM  T_ACT_BUSINESS t WHERE t.title = 'autotest资源申请' 
	    AND t.PROC_DEF_ID LIKE ( SELECT ROUTER FROM T_ACT_BUSINESS_CONFIG WHERE NAME = '资源采购' ) || '%' 
    ORDER BY t.CREATE_time DESC ) WHERE rownum =1 '''
        tt=self.sql_LOB_result(sql)
        kk=tt[0]
        zz=eval(kk)
        print zz
        return zz

    def xparh_join(self,xpath,num):
        # num=random.randint(2,num)
        a='('+ xpath + ')'+'[%d]'%num
        return a

    def randomnum(self,num):
        if num==1:
            a=1
            return a
        else:
            tt=random.randint(1,num)
            return tt