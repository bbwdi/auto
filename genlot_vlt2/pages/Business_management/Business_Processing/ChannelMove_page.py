#coding=utf-8
import time
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.base_page import BasePage
import random
import os

from selenium.webdriver.common.action_chains import ActionChains



aa='''//*[@id="pane-1"]//input[@placeholder='请选择渠道编号']'''#点击渠道编号输入框
bb='''//ul/li[@class='el-select-dropdown__item hover']'''#选择渠道编号
cc='''//*[@id="pane-1"]//span[@class='el-switch__core']'''
dd='''(//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1])'''#选择一个
ee='''//ul/li[@class='el-select-dropdown__item hover']'''#选择输入框中下拉框
gg='''//*[@id="pane-1"]//input[@placeholder='请输入标题']'''
reason_path='''//*[@id="pane-1"]//textarea'''
input1='''//*[@id="pane-1"]//em[text()='点击上传']'''
detailaddress='''//*[@id="pane-1"]//form//input[@placeholder='填写详细地址']'''
addresstext=u'''迁址罗  地址随意哦~！@#￥%……&*（）——'''#详细地址
commit=''' //*[@id="channelMoveMachine-submit"]/span[text()='提交'] '''
cancel_path='''//*[@id="channelMoveMachine-cancel"]'''
clickModel1='''(//*[@id="pane-1"]//input[@placeholder='请选择设备型号'])'''#点击第一行型号
Model1='''(//div[@class='el-scrollbar']//ul/li[1])[4]'''#第一行型号
num1='''(//*[@id="pane-1"]//input[@placeholder='请选择设备序列号'])'''
new_channel_no='''//*[@id="pane-1"]//form//input[@placeholder='请选择新渠道编号']'''


class Move(business_process):
    def channel_no(self,no=''):
        '''输入渠道编号'''
        if no=='':
            self.get_element_by_xpath(aa).click()
            time.sleep(1)
            text=self.get_element_by_xpath(dd).text
            self.get_element_by_xpath(dd).click()
            return text
        else:
            self.input_xpath(aa,no)
            self.get_element_by_xpath(ee).click()
            return  no


    def Resources(self,num=1):
        '''资源，可以多个一起'''
        if num==1:
            time.sleep(1)
            self.get_element_by_xpath(clickModel1).click()
            time.sleep(1)
            self.get_element_by_xpath(Model1).click()
            self.input_xpath(num1, 1)
            time.sleep(1)
        else:
            pass

    def new_channel_no(self,no=''):
        '''输入新渠道编号'''
        if no=='':
            self.get_element_by_xpath(new_channel_no).click()
            time.sleep(1)
            tt=self.get_elements_by_xpath(dd)
            tt1=len(tt)
            dd1=self.xparh_join(dd,tt1)
            text=self.get_element_by_xpath(dd1).text
            self.get_element_by_xpath(dd1).click()
            return text
        else:
            self.input_xpath(aa,no)
            self.get_element_by_xpath(ee).click()
            return  no

    def reason(self,xuyao=u'''没得办法，需要搬走'''):
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

    def xpath_allnum(self):
        '''省市县相加有多少个'''
        tt=self.get_elements_by_xpath(groupnum)
        kk=len(tt)
        return  kk

    def xpath_num(self):
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