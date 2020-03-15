#coding=utf-8
import time
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.base_page import BasePage
import random
import os
from  common.function import regex
from selenium.webdriver.common.action_chains import ActionChains



aa='''//*[@id="pane-1"]//input[@placeholder='请选择渠道编号']'''#点击渠道编号输入框
bb='''//ul/li[@class='el-select-dropdown__item hover']'''#选择渠道编号
cc='''//*[@id="pane-1"]//span[@class='el-switch__core']'''
dd='''//ul[@class='el-scrollbar__view el-select-dropdown__list']/li'''#选择一个
ee='''//ul/li[@class='el-select-dropdown__item hover']'''#选择输入框中下拉框
address='''//*[@id="pane-1"]//form//input[@placeholder='请选择省 / 市 / 区']'''
gg='''//*[@id="pane-1"]//input[@placeholder='请输入申请标题']'''
titlename=u'''增机申请'''
address3='''(//li/i[@class='el-icon-arrow-right el-cascader-node__postfix'])[3]'''
reason_path='''//*[@id="pane-1"]//div/textarea'''
input1='''//*[@id="pane-1"]//em[text()='点击上传']'''
detailaddress='''//*[@id="pane-1"]//form//input[@placeholder='填写详细地址']'''
addresstext=u'''迁址罗  地址随意哦~！@#￥%……&*（）——'''#详细地址
commit='''//*[@id="channelBackMachine-submit"]/span[text()='提交'] '''
cancel_path='''//*[@id="channelBackMachine-cancel"]/span[text()='取消']'''
add='''//*[@id="pane-1"]//button/span[text()='新增设备']'''#点击添加设备
Resources1='''(//*[@id="pane-1"]//input[@placeholder='请选择资源类型'])[1]'''#点击资源类型第一行
Resources2='''(//*[@id="pane-1"]//input[@placeholder='请选择资源类型'])[2]'''#点击资源类型第二行
type1='''(//ul/li[@class='el-select-dropdown__item']/span[text()='设备'])[2]'''#设备第一行类型
type2='''(//ul/li[@class='el-select-dropdown__item']/span[text()='设备'])'''#设备第二行类型
clickname1='''(//*[@id="pane-1"]//input[@placeholder='请选择资源名称'])[1]'''#点击第一行名称
clickname2='''(//*[@id="pane-1"]//input[@placeholder='请选择资源名称'])[2]'''#点击第二行名称
rename1='''(//ul/li/span[text()='终端机'])[1]'''#名称第一行类型
rename2='''(//ul/li/span[text()='柜员机'])[2]'''#名称第二行类型
clickModel1='''(//*[@id="pane-1"]//input[@placeholder='请选择设备型号'])'''#点击第一行型号
Model1='''(//div[@class='el-scrollbar']//ul/li[1])[4]'''#第一行型号
num1='''(//*[@id="pane-1"]//input[@placeholder='设备序列号'])'''


class Back(business_process):
    def channel_no(self,no=''):
        '''输入渠道编号'''
        if no=='':
            self.get_element_by_xpath(aa).click()
            time.sleep(1)
            tt=self.get_elements_by_xpath(dd)
            tt1=len(tt)
            kk=random.randint(2,tt1)#数字从10开始
            print kk
            dd1=self.xparh_join(dd,kk)
            print dd1
            text=self.get_element_by_xpath(dd1).text
            self.get_element_by_xpath(dd1).click()
            return text
        else:
            self.input_xpath(aa,no)
            self.get_element_by_xpath(ee).click()
            return  no

    def Resources(self):
        '''资源，目前只能一个一个退'''
        time.sleep(1)
        self.get_element_by_xpath(clickModel1).click()
        time.sleep(1)
        self.get_element_by_xpath(Model1).click()
        self.input_xpath(num1, 1)
        time.sleep(1)


    def reason(self,xuyao=u'''没得办法，没搞头罗￥%sdf'''):
        self.input_xpath(reason_path,xuyao)

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
        self.get_element_by_xpath(commit).click()

    def cancel(self):
        '''取消'''
        self.get_element_by_xpath(cancel_path).click()


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