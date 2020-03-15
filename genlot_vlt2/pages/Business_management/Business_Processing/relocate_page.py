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
dd='''(//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1])'''#选择一个
ee='''//ul/li[@class='el-select-dropdown__item hover']'''#选择输入框中下拉框
address='''(//*[@id="pane-1"]//form//input[@placeholder='请选择省 / 市 / 区'])[1]'''
address1='''//ul[@class='el-scrollbar__view el-cascader-menu__list']/li'''#点击省 进入下一级
gg='''//*[@id="pane-1"]//input[@placeholder='请输入标题']'''
titlename=u'''迁址申请'''
address3='''(//li/i[@class='el-icon-arrow-right el-cascader-node__postfix'])[3]'''
reason_path='''//*[@id="pane-1"]//textarea[@placeholder='请输入迁址原因']'''
input1='''//*[@id="pane-1"]//em[text()='点击上传']'''
detailaddress='''//*[@id="pane-1"]//form//input[@placeholder='填写详细地址']'''
addresstext=u'''迁址罗  地址随意哦~！@#￥%……&*（）——'''#详细地址
commit=''' //*[@id="channelRelocation-submit"]/span[text()='提交'] '''
cancel_path='''//*[@id="channelCreate-cancel"]'''
shi1='''//ul[@class='el-scrollbar__view el-cascader-menu__list']/li'''
groupnum='''//ul//li[@role='menuitem']/span[@class='el-cascader-node__label']'''#省市县加起来多少个
suiyi2='''//*[@id="pane-1"]//label[text()='渠道地址']'''#点完机构 弹出框不会自动消失，随意点个地方让弹出框消失
suiyi3='''//*[@id="pane-1"]//h2/span[text()='人员信息']'''
tte='''//ul[@class='el-scrollbar__view el-cascader-menu__list']/li[2]//span[1]'''#县定位基础方法


class Relocate(business_process):
    # def title(self):
    #     '''申请标题，目前去掉了 '''
    #     ll=self.channel_no()
    #     titlename1=ll + titlename
    #     self.input_xpath(gg,titlename1)
    #     return  titlename1


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

    def channeladdress(self,zz6=1):
        '''地址，先判断是省还是市，目前判断zz的值,zz为1代表省'''
        time.sleep(1)
        if zz6==1:
            self.get_element_by_xpath(address).click()#点击地址
            time.sleep(1)
            asd=self.get_elements_by_xpath(address1)#取定位有多少个，省的在最后
            tt=len(self.get_elements_by_xpath(address1))#取定位有多少个，省的在最后
            asd=self.xparh_join(address1,tt)#省的定位在最后一个
            self.get_element_by_xpath(asd).click()#点击省
            time.sleep(2)
            asd6 = self.get_elements_by_xpath(address1)  # 市出来后 取定位有多少个
            asd7=len(asd6)# 市出来后 取定位有多少个
            asd8=asd7-tt
            he=self.randomnum(asd8)#随机一个整数
            qq=int(he)+tt#点击省后出来的定位个数会增加，随机加一个数，点击
            asd1 = self.xparh_join(address1, qq)
            print asd1
            self.get_element_by_xpath(asd1).click()#选择一个市
            za=self.get_elements_by_xpath(address1)#县出来后 取定位公共有多少个
            ka=len(za)
            time.sleep(2)
            tttt=ka-asd8
            he1 = self.randomnum(tttt)  # 随机一个整数
            qq1 =  ka - int(he1)#总共的减去随机数 要选取县的定位
            asd2 = self.xparh_join(address1, qq1)
            self.get_element_by_xpath(asd2).click()  # 选择县
            time.sleep(1)
            self.input_xpath(detailaddress, addresstext)
            return addresstext
        else:
            self.get_element_by_xpath(address).click()  # 点击地址
            time.sleep(1)
            asd = self.get_elements_by_xpath(address1)  # 取定位有多少个，省的在最后
            tt = len(self.get_elements_by_xpath(address1))  # 取定位有多少个，省的在最后
            asd = self.xparh_join(address1, tt)  # 省的定位在最后一个
            self.get_element_by_xpath(asd).click()  # 点击省
            time.sleep(2)
            qq = 1 + tt  # 点击省后出来的定位个数会增加，市级渠道只会增加1
            asd1 = self.xparh_join(address1, qq)
            print asd1
            self.get_element_by_xpath(asd1).click()  # 选择一个市
            za = self.get_elements_by_xpath(address1)  # 县出来后 取定位公共有多少个
            ka = len(za)
            time.sleep(2)
            he1 = self.randomnum(3)  # 随机一个整数
            qq1 = ka - qq  # 总共的减去随机数 要选取县的定位
            qq2=self.randomnum(qq1)
            asd2 = self.xparh_join(address1, qq+qq2)
            self.get_element_by_xpath(asd2).click()  # 选择县
            time.sleep(1)
            self.input_xpath(detailaddress, addresstext)
            return addresstext

    def reason(self,xuyao=u'''没得办法，必须的走'''):
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