#coding=utf-8
import time
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.channelnewbuilt_page import New
from pages.base_page import BasePage
import random
import os
from  common.function import regex
from selenium.webdriver.common.action_chains import ActionChains
from db.oracle_db import Oracle
from common.function import log_info


aa='''//*[@id="pane-1"]//input[@placeholder='请选择渠道编号']'''#点击渠道编号输入框
bb='''//ul/li[@class='el-select-dropdown__item hover']'''#选择渠道编号
cc='''//*[@id="pane-1"]//span[@class='el-switch__core']'''
dd='''(//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1])[2]'''#选择一个
ee='''//ul/li[@class='el-select-dropdown__item hover']'''#选择输入框中下拉框
place='''//*[@id="pane-1"]//form//input[@placeholder='请选择经营场所属性']'''
ziyou='''//ul//span[text()='自有']'''
zulin='''//ul//span[text()='租赁']'''
area='''//*[@id="pane-1"]//form//input[@placeholder='请输入销售厅面积']'''
kk='''100'''#销售厅面积num
kaikalimit='''//*[@id="pane-1"]//form//input[@placeholder='请输入投注卡开卡次数']'''
ll='''1000'''#投注卡开卡次数num
mm='''100'''#试玩卡开卡次数num
shiwan='''//*[@id="pane-1"]//form//input[@placeholder='请输入试玩卡开卡次数']'''
chongzhi='''//*[@id="pane-1"]//form//input[@placeholder='请输入充值次数']'''
nn='''10000000'''#充值次数num
oo='''100'''#渠道人数上限人数num
peoplelimit='''//*[@id="pane-1"]//form//input[@placeholder='请输入渠道人员上限']'''
latitude_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入渠道纬度']'''
pp='''12.362356'''#纬度
longitude_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入渠道经度']'''
qq='''12.362356'''#经度
zhanshi_path='''//*[@id="pane-1"]//input[@placeholder='请输入账户记录查询台数']'''
name_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入姓名']'''
name1=u'''李四'''
sex_path='''//div[@role='radiogroup']/label[1]//span[@class='el-radio__inner']'''
sex_path1='''//div[@role='radiogroup']/label[2]//span[@class='el-radio__inner']'''
age_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入年龄']'''
age1='''18'''
phone_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入手机号码']'''
cardid_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入身份证号码']'''
jiahao='''//*[@id="pane-1"]//div/form//div/i[@class='el-icon-plus']'''
cardnumber='''(//*[@id="pane-1"]//form//input[@placeholder='请输入数量'])[1]'''#投注卡卡费数量
cardmoney='''//*[@id="pane-1"]//form//input[@placeholder='请输入金额']'''
yajin='''//*[@id="pane-1"]//div/label/span[contains(text(),'收费')]'''
yajinnum='''(//*[@id="pane-1"]//input[@placeholder='请输入张数'])'''
input1='''//*[@id="pane-1"]//em[text()='点击上传']'''
commit='''//*[@id="channelChange-submit"]/span'''
cancel_path='''//*[@id="channelChange-canvel"]/span'''

class Change(business_process):
    def channel_no(self,no=''):
        '''输入渠道编号，默认为空选择第一个'''
        if no=='':
            self.get_element_by_xpath(aa).click()
            time.sleep(1)
            text=self.get_element_by_xpath(dd).text
            self.get_element_by_xpath(dd).click()
            return str(text)
        else:
            self.input_xpath(aa,no)
            self.get_element_by_xpath(ee).click()
            return no

    def base_switch(self):
        '''切换到编辑'''
        time.sleep(5)
        self.switch(1)

    def place1(self,aa=u'自有'):
        '''经营场所属性'''
        self.get_element_by_xpath(place).click()
        if aa=='自有':
            pass
        else:
            self.get_element_by_xpath(zulin).click()
        return aa

    def areainput(self,num=kk):
        '''面积大小'''
        self.input_xpath(area,num)
        return num

    def zhanshi(self):
        '''展示厅展示数量'''
        tt=self.randomnum(10)
        self.input_xpath(zhanshi_path,tt)
        return str(tt)


    def kailimit(self,num=ll):
        '''投注卡限制'''
        self.input_xpath(kaikalimit,num)
        return num

    def shiwanlimit(self,num=mm):
        '''试玩卡限制'''
        self.input_xpath(shiwan,num)
        return num
    def Recharge(self,num=nn):
        '''充值'''
        self.input_xpath(chongzhi,num)
        return num
    def people_limit(self,num=oo):
        '''渠道人员上限'''
        self.input_xpath(peoplelimit, num)
        return num
    def latitude(self,num=pp):
        '''纬度'''
        self.input_xpath(latitude_path, num)
        return num
    def longitude(self,num=qq):
        '''经度'''
        self.input_xpath(longitude_path, num)
        return num

    def name(self):
        '''人员信息：姓名'''
        time.sleep(1)
        self.input_xpath(name_path,name1)
        return name1
    def sex(self):
        '''性别'''
        a=random.randint(1,2)
        if a==1:
            self.get_element_by_xpath(sex_path).click()
            c=u"男"
            return c
        else:
            self.get_element_by_xpath(sex_path1).click()
            c = u"女"
            return c

    def phone(self):
        '''手机号'''
        phone1=self.create_mobile()
        self.input_xpath(phone_path, phone1)
        time.sleep(0.5)
        return phone1

    def cardid(self):
        '''身份证号'''
        cardid1=self.id_card()
        time.sleep(1)
        self.input_xpath(cardid_path, cardid1)
        return cardid1

    def Photo(self):
        '''照片，默认路径下的图片'''
        self.get_element_by_xpath(jiahao).click()
        # tt=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#拿上一级目录
        tt=os.path.abspath(os.path.join(os.getcwd(), "../../.."))
        pngpath=tt+r'''\static\images\test.png'''
        self.upload_file(pngpath)
        return  pngpath

    def cardnum(self):
        '''投注卡数量'''
        numb=random.randint(1,10000)
        self.input_xpath(cardnumber,numb)
        return numb
    def cardnaccount(self):
        '''收费金额'''
        money=random.randint(1,10000)
        self.input_xpath(cardmoney,money)
        return money
    def deposit(self):
        '''是否收押金，随机用1代表不收费，2代表收费'''
        time.sleep(2)
        tt=random.randint(1,2)
        kk = self.xparh_join(yajin, tt)
        if int(tt)==1:
            self.get_element_by_xpath(kk).click()
            return tt
        else:
            self.get_element_by_xpath(kk).click()
            zz=str(self.randomnum(100))
            print zz
            self.input_xpath(yajinnum,zz)
            return zz

    def Submission(self):
        '''提交'''
        self.get_element_by_xpath(commit).click()

    def cancel(self):
        '''取消'''
        self.get_element_by_xpath(cancel_path).click()

    def switch(self,num):
        '''切换成启用，num为几就对应相应的启用'''
        time.sleep(2)
        tt=self.xparh_join(cc,num)
        print tt
        self.get_element_by_xpath(tt).click()

    def appendix(self):
        '''添加附件'''
        self.get_element_by_xpath(input1).click()
        tt = os.path.abspath(os.path.join(os.getcwd(), "../../.."))
        pngpath = tt + r'''\static\images\test.png'''
        self.upload_file(pngpath)
        time.sleep(1)
        return pngpath

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

    def querydetail(self, channel_no=''):
            '''查询修改的东西'''
            sql = '''SELECT   case 
    						WHEN	a.RUN_FIELD=0 then '自有'
    						WHEN	a.RUN_FIELD=1 then '租用'
    						else NULL
    						  END as filed,a.POINT_AREA as area,
									d.SHOW_MACHINE_COUNT as zhanshi,
    							d.buy_card_limit as buyCardLimit,
                	d.try_card_limit as tryCardLimit,
    							d.recharge_count as rechargeCount,
    							d.CHANNEL_LIMIT as  CHANNELLIMIT,
    							d.longitude ,d.latitude,
    							f.account_name as accountname,f.SEX as sex, f.PHONE as  phone,
    							f.CHANNEL_IDENTITY as cardid 
                FROM
                	t_channel_info d
                	LEFT JOIN t_partner c ON d.partner_id = c.id
                	INNER JOIN t_ins_info t ON d.ins_id = t.ins_id
    							LEFT JOIN T_FINANCE_INFO a on a.channel_id=d.channel_id
    							left JOIN T_CHANNEL_FUND f on d.channel_id=f.channel_id	
                WHERE d.channel_no ='%s'  ''' % channel_no

            t = Oracle()
            kk = t.run_sql_dir(sql)
            log_info(kk)
            return kk