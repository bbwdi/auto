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
commit='''//*[@id="channelAddMachine-submit"]/span[text()='提交'] '''
cancel_path='''//*[@id="channelAddMachine-cancel"]/span[text()='取消']'''
add='''//*[@id="pane-1"]//button/span[text()='新增设备']'''#点击添加设备
Resources1='''(//*[@id="pane-1"]//input[@placeholder='请选择资源类型'])[1]'''#点击资源类型第一行
Resources2='''(//*[@id="pane-1"]//input[@placeholder='请选择资源类型'])[2]'''#点击资源类型第二行
type1='''(//ul/li[@class='el-select-dropdown__item']/span[text()='设备'])[2]'''#设备第一行类型
type2='''(//ul/li[@class='el-select-dropdown__item']/span[text()='设备'])'''#设备第二行类型
clickname1='''(//*[@id="pane-1"]//input[@placeholder='请选择资源名称'])[1]'''#点击第一行名称
clickname2='''(//*[@id="pane-1"]//input[@placeholder='请选择资源名称'])[2]'''#点击第二行名称
rename1='''(//ul/li/span[text()='终端机'])[1]'''#名称第一行类型
rename2='''(//ul/li/span[text()='柜员机'])[2]'''#名称第二行类型
clickModel1='''(//*[@id="pane-1"]//input[@placeholder='请选择型号'])[1]'''#点击第一行型号
clickModel2='''(//*[@id="pane-1"]//input[@placeholder='请选择型号'])[2]'''#点击第二行型号
Model1='''(//div[@class='el-scrollbar']//ul/li[1])[4]'''#第一行型号
Model2='''(//div[@class='el-scrollbar']//ul/li[1])[9]'''#第二行型号
num1='''(//*[@id="pane-1"]//input[@placeholder='请输入数量'])'''
num2='''(//*[@id="pane-1"]//input[@placeholder='请输入数量'])[3]'''




class Add(business_process):
    def title(self,tt):

        titlename1=tt + titlename
        self.input_xpath(gg,titlename1)
        return  titlename1


    def channel_no(self,no=''):
        '''输入渠道编号'''
        if no=='':
            self.get_element_by_xpath(aa).click()
            time.sleep(1)
            tt=self.get_elements_by_xpath(dd)
            tt1=len(tt)
            kk=random.randint(10,tt1)#数字从10开始
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
        '''资源，先增加一个终端机一个柜员机'''
        # self.get_element_by_xpath(add).click()
        # 第一行数据
        time.sleep(1)
        self.get_element_by_xpath(clickname1).click()
        time.sleep(2)
        self.get_element_by_xpath(rename1).click()
        self.get_element_by_xpath(clickModel1).click()
        time.sleep(1)
        # 目前后面的提示去掉了 直接写死1
        self.get_element_by_xpath(Model1).click()
        # kk=self.get_element_by_xpath(erdu1).text
        # tt=regex('\d+',kk)
        self.input_xpath(num1, 1)
        time.sleep(1)
        # # 第二行数据
        # time.sleep(1)
        # self.get_element_by_xpath(clickname2).click()
        # time.sleep(1)
        # self.get_element_by_xpath(rename2).click()
        # time.sleep(1)
        # self.get_element_by_xpath(clickModel2).click()
        # time.sleep(1)
        # self.get_element_by_xpath(Model2).click()
        # # kk = self.get_element_by_xpath(erdu2).text
        # # tt = regex('\d+', kk)
        # self.input_xpath(num2, 1)

    def reason(self,xuyao=u'''没得办法，就是人多'''):
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

    def xpath_allnum(self,groupnum):
        '''省市县相加有多少个'''
        tt=self.get_elements_by_xpath(groupnum)
        kk=len(tt)
        return  kk

    def xpath_num(self,shi1):
        '''省市相加有多少个'''
        tt=self.get_elements_by_xpath(shi1)
        kk=len(tt)-4
        return  kk

    def randomnum(self,num):
        if num==1:
            a=1
            return a
        else:
            tt=random.randint(1,num)
            return tt