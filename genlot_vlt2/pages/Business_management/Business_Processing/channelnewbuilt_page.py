#coding=utf-8
import time
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.base_page import BasePage
from pages.home1_page import *
import random
import os
from  common.function import regex
from selenium.webdriver.common.action_chains import ActionChains
from db.oracle_db import Oracle
from pages.base_page import log_info
import json
import datetime



aa='''//*[@id="pane-1"]//input[@placeholder='请选择所属机构']'''#点开机构
bb='''//li[contains(@id,'cascader-menu')]//span[@class='el-radio__inner']'''#选择省
cc='''//*[@id="pane-1"]//form//div[@class='el-input-group__prepend']'''
dd='''//*[@id="pane-1"]//form//input[@placeholder='请输入四位渠道编号']'''
ee='''//*[@id="pane-1"]//form//input[@placeholder='请选择渠道类型']'''
ff='''//ul//span[text()='合作厅']'''
gg='''//*[@id="pane-1"]//form//input[@placeholder='请选择渠道等级']'''
hh='''//ul//span[text()='一级']'''
ii='''//ul//span[text()='二级']'''
jj='''(//div[@class='el-scrollbar']//ul/li[1])[3]'''#选择等级第一个
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
address='''//*[@id="pane-1"]//form//input[@placeholder='请选择省 / 市 / 区']'''
address1='''(//li/i[@class='el-icon-arrow-right el-cascader-node__postfix'])[2]'''#点击省 进入下一级
zz6=1#1代表选择省，非1代表选择市
shi='''(//li/i[@class='el-icon-arrow-right el-cascader-node__postfix'])[1]'''
# shi1='''//label[@role='radio']//span[@class='el-radio__inner']'''
shi1='''//ul[@class='el-scrollbar__view el-cascader-menu__list']/li'''
yuanqiu='''//ul[@class='el-scrollbar__view el-cascader-menu__list']/li//span[@class='el-radio__inner']'''
address2='''(//li/i[@class='el-icon-arrow-right el-cascader-node__postfix'])[2]'''#点击进入市选择
address3='''(//li/i[@class='el-icon-arrow-right el-cascader-node__postfix'])[3]'''#点击进入县选择
groupnum='''//ul//li[@role='menuitem']/span[@class='el-cascader-node__label']'''#省市县加起来多少个
tte='''//ul[@class='el-scrollbar__view el-cascader-menu__list']/li[2]//span[1]'''#县定位基础方法
detailaddress='''//*[@id="pane-1"]//form//input[@placeholder='填写详细地址']'''
addresstext=u'''1号哦'''#详细地址
name_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入姓名']'''
name1=u'''李四'''
sex_path='''//div[@role='radiogroup']/label[1]//span[@class='el-radio__inner']'''
sex_path1='''//div[@role='radiogroup']/label[2]//span[@class='el-radio__inner']'''
age_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入年龄']'''
age1='''18'''
phone_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入手机号码']'''
cardid_path='''//*[@id="pane-1"]//form//input[@placeholder='请输入身份证号码']'''
lianxiad='''//*[@id="pane-1"]//form//input[@placeholder='请输入联系地址']'''
lianxiaddresstext=u'''2号哦'''#联系地址
zhaopian='''//*[@id="pane-1"]//div/form//div/i[@class='el-icon-plus']'''
jiahao='''//*[@id="pane-1"]//div/form//div/i[@class='el-icon-plus']'''
cardnumber='''(//*[@id="pane-1"]//form//input[@placeholder='请输入数量'])[1]'''#投注卡卡费数量
cardmoney='''//*[@id="pane-1"]//form//input[@placeholder='请输入金额']'''
yajin='''//*[@id="pane-1"]//div/label/span[contains(text(),'收费')]'''
duijiang='''//*[@id="pane-1"]//span[@class='el-switch__core']'''
starttime='''//*[@id="pane-1"]//input[@placeholder='开始时间']'''
endtime='''//*[@id="pane-1"]//input[@placeholder='结束时间']'''
add='''//*[@id="pane-1"]//button/span[text()='添加设备']'''#点击添加设备
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
Model1='''(//div[@class='el-scrollbar']//ul/li[1])[7]'''#第一行型号
Model2='''(//div[@class='el-scrollbar']//ul/li[1])[9]'''#第二行型号
erdu1='''//div[@role="tooltip"])[2]'''#第一行额度剩余
erdu2='''//div[@role="tooltip"])[3]'''#第二行额度剩余
num1='''(//*[@id="pane-1"]//input[@placeholder='请输入数量'])[2]'''
num2='''(//*[@id="pane-1"]//input[@placeholder='请输入数量'])[3]'''
input1='''//*[@id="pane-1"]//em[text()='点击上传']'''
commit='''//*[@id="channelCreate-submit"]/span[text()='提交']'''
cancel_path='''//*[@id="channelCreate-cancel"]'''
suiyi='''//*[@id="pane-1"]//label[text()='所属机构']'''#点完机构 弹出框不会自动消失，随意点个地方让弹出框消失
suiyi_yinchuan='''//*[contains(text(),"银川市")]'''#点完机构 弹出框不会自动消失，随意点个地方让弹出框消失
suiyi2='''//*[@id="pane-1"]//label[text()='渠道地址']'''#点完机构 弹出框不会自动消失，随意点个地方让弹出框消失
suiyi3='''//*[@id="pane-1"]//h2/span[text()='人员信息']'''
yajinnum='''(//*[@id="pane-1"]//input[@placeholder='请输入金额'])[2]'''
zhanshi_path='''//*[@id="pane-1"]//input[@placeholder='请输入账户记录查询台数']'''
title_path='''//*[@id="pane-1"]//input[@placeholder='请输入标题']'''
title7=u'''建厅申请'''


class New(business_process):
    def title(self,tt):
        time.sleep(1)
        title1=tt + title7
        print "title1=%s"%title1
        self.input_xpath(title_path,title1)
        return  title1

    def group(self,num=zz6):
        '''渠道所属机构'''
        if  num==1:
            self.get_element_by_xpath(aa).click()#点开机构
            time.sleep(1)
            self.get_element_by_xpath(bb).click() #选择省
            time.sleep(1)
            self.get_element_by_xpath(suiyi).click()
        else:
            self.get_element_by_xpath(aa).click()  # 点开机构
            time.sleep(1)
            self.get_element_by_xpath(shi).click()  # 弹出市组织
            time.sleep(1)
            tt1 = self.xpath_num()  # 省市个数
            sd=self.randomnum(tt1-1)
            tt = tt1 - sd
            abc = self.xparh_join(yuanqiu, tt)  # 随机县的
            print tt1,sd ,tt,abc
            time.sleep(1)
            self.get_element_by_xpath(abc).click()  # 点击市
            time.sleep(1)
            self.get_element_by_xpath(suiyi).click()
        time.sleep(2)

    def choose_group(self,num=zz6):
        '''渠道所属机构'''
        if  num==1:
            self.get_element_by_xpath(aa).click()#点开机构
            time.sleep(1)
            self.get_element_by_xpath(bb).click() #选择省
            time.sleep(1)
            self.get_element_by_xpath(suiyi).click()
        else:
            self.get_element_by_xpath(aa).click()  # 点开机构
            time.sleep(1)
            self.get_element_by_xpath(shi).click()  # 弹出市组织
            time.sleep(1)
            tt1 = self.xpath_num()  # 省市个数
            sd=self.randomnum(tt1-1)
            tt = tt1 - sd
            abc = self.xparh_join(yuanqiu, tt)  # 随机县的
            print tt1,sd ,tt,abc
            time.sleep(1)
            self.get_element_by_xpath(suiyi_yinchuan).click()  # 点击市
            time.sleep(1)
            self.get_element_by_xpath(suiyi).click()
        time.sleep(2)

    def channelno(self):
        '''渠道编号，拿最大值后四位加一'''
        aa=self.data1()#返回业务表中数据
        tt=self.take_channelno()#返回channelinfo数据
        print 'tt=%s'%tt
        print 'aa=%s'%aa
        '''判断返回的值是否为0，为0则代表业务表中无数据存在，不为0则代表有数据存在  需要对比两个channelno的值'''
        if aa==0:
            gg=tt
        else:
            # zz=aa["channelData"]["channelNo"]
            zz1=aa[:6]
            tt1=tt[:6]
            print 'zz1=%s'%zz1
            print 'tt1=%s'%tt1
            if int(zz1)==int(tt1):#判断前六位是否相同
                if int(tt)>=int(aa):
                    gg=tt
                else:
                    gg=aa
            else:
                gg = tt

        print tt
        cc=str(int(gg)+1)
        print cc
        kk=cc[-4:]
        print kk
        self.input_xpath(dd,kk)
        return cc

    def channeltype(self,type=u'自营厅'):
        '''渠道类型，默认自营厅，反之合作厅'''
        if type == u'自营厅':
            a=0
            pass
        else:
            self.get_element_by_xpath(ee).click()
            self.get_element_by_xpath(ff).click()
            a=1
        return a
    def channellevel(self,level='一级'):
        '''渠道等级，默认一级,因为对比业务表中都是id  在这提前查询出id返回'''
        if level == u'一级':
            self.get_element_by_xpath(gg).click()
            time.sleep(1)
            self.get_element_by_xpath(hh).click()

        elif level==u'二级':
            self.get_element_by_xpath(gg).click()
            time.sleep(1)
            self.get_element_by_xpath(ii).click()

        else :
            self.get_element_by_xpath(gg).click()
            time.sleep(1)
            self.get_element_by_xpath(jj).click()
        sql='''SELECT ch_grade_id  from  T_CHANNEL_GRADE_INFO where ch_level_name='%s' '''%level
        tt=self.sql_result(sql)
        return tt[0]
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
        tt=int(num)
        return tt

    def kailimit(self,num=ll):
        '''投注卡限制'''
        self.input_xpath(kaikalimit,num)
        tt = int(num)
        return tt

    def shiwanlimit(self,num=mm):
        '''试玩卡限制'''
        self.input_xpath(shiwan,num)
        tt = int(num)
        return tt
    def Recharge(self,num=nn):
        '''充值'''
        self.input_xpath(chongzhi,num)
        tt = int(num)
        return tt
    def people_limit(self,num=oo):
        '''渠道人员上限'''
        self.input_xpath(peoplelimit, num)
        tt = int(num)
        return tt

    def latitude(self,num=pp):
        '''纬度'''
        self.input_xpath(latitude_path, num)
        return num
    def longitude(self,num=qq):
        '''经度'''
        self.input_xpath(longitude_path, num)
        return num
    def zhanshi(self):
        '''账户记录查询台数'''
        tt=self.randomnum(10)
        self.input_xpath(zhanshi_path,tt)
        return str(tt)

    def channeladdress(self):
        '''地址，先判断是省还是市，目前判断zz的值,zz为1代表省'''
        if zz6==1:
            self.get_element_by_xpath(address).click()#点击地址
            time.sleep(1)
            self.get_element_by_xpath(address1).click()#点击省
            time.sleep(1)
            numb=self.get_elements_by_xpath(shi1)
            tt3=len(numb)#得出市出来后 定位有多少个
            self.get_element_by_xpath(address3).click()#点击市
            # tt=self.xpath_allnum()#所有省市县个数
            # tt1=self.xpath_num()#省市个数
            numb1 = self.get_elements_by_xpath(shi1)
            tt2 = len(numb1)#得出县出来后 定位有多少个
            asd=tt2-tt3
            asd1=self.randomnum(asd)
            print ('asd=%s')%asd
            print ('asd1=%s')%asd1
            abc=self.xparh_join(shi1,tt3+asd1)#随机取一个县 tt3代表到市时个数 asd1代表第几个县 随机来的
            print ('abc=%s')%abc
            self.get_element_by_xpath(abc).click()#点击县
            time.sleep(1)
            self.get_element_by_xpath(suiyi2).click()
            rrr=self.get_element_by_xpath(suiyi3)
            time.sleep(1)
            ActionChains(self.b).move_to_element(rrr).perform()

            self.input_xpath(detailaddress, addresstext)
            self.get_element_by_xpath(suiyi2).click()  # 点击前面让弹出框消失
            return addresstext
        else:
            self.get_element_by_xpath(address).click()  # 点击地址
            time.sleep(1)
            self.get_element_by_xpath(address1).click()  # 点击地址
            self.get_element_by_xpath(address3).click()  # 点击地址
            zz=self.xpath_allnum()
            zz2=self.xparh_join(tte,zz)
            self.get_element_by_xpath(zz2).click()#
            self.input_xpath(detailaddress,addresstext)
            self.get_element_by_xpath(suiyi2).click()  # 点击前面让弹出框消失
            return addresstext


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

    def Contact_address(self):
        '''联系地址'''
        self.input_xpath(lianxiad, lianxiaddresstext)
        return lianxiaddresstext

    # def age(self):
    #     '''年纪，现在自动获取，不用输入,需要获取值校验'''
    #     time.sleep(3)
    #     tt=self.get_element_by_xpath().text
    def Photo(self):
        '''联系地址'''
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
        return str(numb)
    def cardnaccount(self):
        '''收费金额'''
        money=random.randint(1,10000)
        self.input_xpath(cardmoney,money)
        return str(money*100)
    def deposit(self):
        '''是否收押金，随机用1代表不收费，2代表收费'''
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

    def gameJurisdiction(self):
        '''销售游戏权限，目前默认第一个'''
        duijiang1=self.xparh_join(duijiang,1)
        self.get_element_by_xpath(duijiang1).click()
        duijiang2 = self.xparh_join(duijiang, 2)
        self.get_element_by_xpath(duijiang2).click()

    def gametime(self):
        '''销售游戏时间，目前点一下会有默认时间，先不做处理'''
        self.get_element_by_xpath(starttime).click()

    def Resources(self):
        '''资源，先增加一个终端机一个柜员机'''
        self.get_element_by_xpath(add).click()
        self.get_element_by_xpath(add).click()
        #第一行数据
        self.get_element_by_xpath(Resources1).click()
        time.sleep(1)
        self.get_element_by_xpath(type1).click()
        time.sleep(1)
        self.get_element_by_xpath(clickname1).click()
        time.sleep(2)
        self.get_element_by_xpath(rename1).click()
        time.sleep(1)
        self.get_element_by_xpath(clickModel1).click()
        time.sleep(1)
        #目前后面的提示去掉了 直接写死1
        self.get_element_by_xpath(Model1).click()
        # kk=self.get_element_by_xpath(erdu1).text
        # tt=regex('\d+',kk)
        self.input_xpath(num1,1)
        time.sleep(1)
        #第二行数据
        self.get_element_by_xpath(Resources2).click()
        time.sleep(1)
        self.get_element_by_xpath(type2).click()
        time.sleep(1)
        self.get_element_by_xpath(clickname2).click()
        time.sleep(1)
        self.get_element_by_xpath(rename2).click()
        time.sleep(1)
        self.get_element_by_xpath(clickModel2).click()
        time.sleep(1)
        self.get_element_by_xpath(Model2).click()
        # kk = self.get_element_by_xpath(erdu2).text
        # tt = regex('\d+', kk)
        self.input_xpath(num2, 1)

    def Resources1(self):
        '''资源，先增加一个终端机一个柜员机'''
        self.get_element_by_xpath(add).click()
        self.get_element_by_xpath(add).click()
        #第一行数据
        self.get_element_by_xpath(Resources1).click()
        time.sleep(1)
        self.get_element_by_xpath(type1).click()
        time.sleep(1)
        self.get_element_by_xpath(clickname1).click()
        time.sleep(2)
        self.get_element_by_xpath(rename1).click()
        time.sleep(1)
        self.get_element_by_xpath(clickModel1).click()
        time.sleep(1)
        #目前后面的提示去掉了 直接写死1
        self.get_element_by_xpath(Model1).click()
        # kk=self.get_element_by_xpath(erdu1).text
        # tt=regex('\d+',kk)
        self.input_xpath(num1,1)
        time.sleep(1)
        #第二行数据
        self.get_element_by_xpath(Resources2).click()
        time.sleep(1)
        self.get_element_by_xpath(type2).click()
        time.sleep(1)
        self.get_element_by_xpath(clickname2).click()
        time.sleep(1)
        self.get_element_by_xpath(rename2).click()
        time.sleep(1)
        self.get_element_by_xpath(clickModel2).click()
        time.sleep(1)
        self.get_element_by_xpath(Model2).click()
        # kk = self.get_element_by_xpath(erdu2).text
        # tt = regex('\d+', kk)
        self.input_xpath(num2, 1)

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
        time.sleep(2)
        self.get_element_by_xpath(commit).click()

    def cancel(self):
        '''取消'''
        self.get_element_by_xpath(cancel_path).click()




    def take_channelno(self):
        '''去数据库拿当前机构最大渠道编号'''
        tt=self.get_element_by_xpath(cc).text
        print tt
        tt1=tt+'%'
        print tt1
        sql="SELECT channel_no from T_CHANNEL_INFO where channel_no like '%s' and rownum=1  ORDER BY channel_no desc"%tt1
        kk1=self.sql_result(sql)#从数据库拿当前机构最大值
        if kk1==0:
            kk=tt+'0001'
        else:
            kk=kk1[0]#
        return kk



    def xparh_join(self,xpath,num):
        '''将xpatn 和数字组合起来，不然直接串报错'''
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
        kk=len(tt)
        return  kk

    def randomnum(self,num):
        if num==1:
            a=1
            return a
        else:
            tt=random.randint(1,num)
            return tt

    def querydetail(self, channel_no=''):
            '''查询新增中的东西'''

            sql = '''SELECT       d.channel_no AS channelNo, 
            	case 
						WHEN	d.channel_type=0 then '自营厅'
						WHEN	d.channel_type=1 then '合作厅'
						else NULL
						  END as shuxing,
            	( SELECT tcgi.ch_level_name FROM t_channel_grade_info tcgi WHERE tcgi.ch_grade_id = d.channel_level_id ) channelLevel,
							case 
						WHEN	a.RUN_FIELD=0 then '自有'
						WHEN	a.RUN_FIELD=1 then '租用'
						else NULL
						  END as filed,a.POINT_AREA as area,
							
							d.buy_card_limit as buyCardLimit,
            	d.try_card_limit as tryCardLimit,
							d.recharge_count as rechargeCount,
							d.CHANNEL_LIMIT as  CHANNELLIMIT,
							d.longitude ,
            	d.latitude,d.channel_address AS channelAddress,
							
							f.account_name as accountname,f.SEX as sex, f.PHONE as  phone,
							f.CHANNEL_IDENTITY as cardid ,f.AGE as age,f.ADDRESS as address
							
							
            FROM
            	t_channel_info d
            	LEFT JOIN t_partner c ON d.partner_id = c.id
            	INNER JOIN t_ins_info t ON d.ins_id = t.ins_id
							LEFT JOIN T_FINANCE_INFO a on a.channel_id=d.channel_id
							left JOIN T_CHANNEL_FUND f on d.channel_id=f.channel_id
            WHERE d.channel_no ='%s'  ''' %channel_no

            t = Oracle()
            kk = t.run_sql_dir(sql)
            log_info(kk)
            return kk

    def data(self):
        '''查询最新申请记录,数据库中是clob类型，需要只能在有效期内操作，转化成str，然后在转化成字典'''
        null = ''
        ss=self.ins()
        sql = '''SELECT data FROM
    	(SELECT  t.*  FROM  T_ACT_BUSINESS t WHERE t.ins_id = '%s' 
    	    AND t.PROC_DEF_ID LIKE ( SELECT ROUTER FROM T_ACT_BUSINESS_CONFIG WHERE NAME = '渠道新建' ) || '%%'  
    	    ORDER BY t.CREATE_time DESC ) WHERE rownum =1 '''%ss
        tt = self.sql_LOB_result(sql)
        print tt
        kk = tt[0]
        print "kk=%s"%kk
        print type(kk)
        zz=json.loads(kk)
        print type(zz)
        print zz
        return zz

    def data1(self):
        '''查询申请记录判断查询出来的channelno是否在里面,数据库中是clob类型，需要只能在有效期内操作，转化成str，然后在转化成字典'''
        null = ''
        tt = self.get_element_by_xpath(cc).text
        # tt='6401000003'
        tt1=tt[:6]
        sql1='''SELECT ins_id  from  T_INS_INFO where ins_code='%s' '''%tt1
        hh=self.sql_result(sql1)
        jj=hh[0]
        sql2 = '''SELECT count(*) FROM
            	(SELECT  t.*  FROM  T_ACT_BUSINESS t WHERE t.ins_id = '%s' 
            	    AND t.PROC_DEF_ID LIKE ( SELECT ROUTER FROM T_ACT_BUSINESS_CONFIG WHERE NAME = '渠道新建' ) || '%%'  
            	    ORDER BY t.CREATE_time DESC ) WHERE rownum =1 ''' % jj
        sql = '''SELECT data FROM
    	(SELECT  t.*  FROM  T_ACT_BUSINESS t WHERE t.ins_id = '%s' 
    	    AND t.PROC_DEF_ID LIKE ( SELECT ROUTER FROM T_ACT_BUSINESS_CONFIG WHERE NAME = '渠道新建' ) || '%%'  
    	    ORDER BY t.CREATE_time DESC )  '''%jj

        dd=self.sql_result(sql2)
        dd1=dd[0]
        if int(dd1)==1:
            ww = self.sql_LOB_result(sql)#返回data列表
            print 'ww=%s'%ww
            ll=[]
            ee=len(ww)
            for i in range(ee):
                kk=ww[i]
                # print 'kk1=%s'%kk1
                # kk = kk1[0]
                print "kk=%s"%kk
                print type(kk)
                zz=json.loads(kk)
                print type(zz)
                print zz

                if tt1 in zz["channelData"]["channelNo"]:
                    print '********************'
                    print zz["channelData"]["channelNo"]
                    return  zz["channelData"]["channelNo"]
                else:
                    asd=0
                    return asd
        else :
            asd=0
            return asd

    def isprocess(self):
        '''判断是否开启了走流程,a=1代表走流程=0代表不走'''
        null = ''
        tt=self.ins()
        sql=''' SELECT count(*) from  T_ACT_PROCESS WHERE latest=1 
        and  process_key='channelCreate-%d' and id like('channelCreate%%') '''%tt#查询是否有省流程

        sql2 = ''' SELECT status from  T_ACT_PROCESS WHERE latest=1 
                and  process_key='channelCreate-%d' and id like('channelCreate%%') ''' % tt#查询省流程状态
        print ('sql=%s')%sql
        sql3 = ''' SELECT status from  T_ACT_PROCESS WHERE latest=1 
                        and  process_key='channelCreate-1' and id like('channelCreate%%') '''#查询是否有全国流程

        sql1= ''' SELECT status from  T_ACT_PROCESS WHERE latest=1 
                and  process_key='channelCreate-1' and id like('channelCreate%%') '''#查询全国流程状态
        kk=self.sql_result(sql)
        print ('kk=%s')%kk
        if int(kk[0])>=1:
            cc=self.sql_result(sql2)
            if cc[0]==1:
                a=1
            else:
                a=0
        else:
            zz = self.sql_result(sql3)
            print ('zz=%s')%zz
            print sql3
            if int(zz[0])>=1:
                ff=self.sql_result(sql1)
                if ff[0]==1:
                    a=1
                else:
                    a=0
                # return a
            else:
                a=0
        print 'a=%s'%a
        log_info(a)
        return a

    def processnew(self):
        '''新建市级渠道'''
        # 判断是否走流程 1代表走  需要从流程表中取数据对比 0代表不走流程 对比数据从channel info
        jj = self.isprocess()
        self.choose_group(2)
        channel_no = self.channelno()
        print channel_no
        type = self.channeltype()
        level = self.channellevel()
        changsuo = self.place1()
        mianji = self.areainput()
        limit = self.kailimit()
        limit1 = self.shiwanlimit()
        chongzhi = self.Recharge()
        limit2 = self.people_limit()
        # latitude=self.dd.latitude()
        # longitude=self.dd.longitude()
        zhanshinum = self.zhanshi()
        address = self.channeladdress()
        name = self.name()
        sex = self.sex()
        phone = self.phone()
        cardid = self.cardid()
        tt = datetime.datetime.now()
        kk = tt.year
        age = str(int(kk) - int(cardid[6:10]))
        address1 = self.Contact_address()
        self.Photo()
        cardnum = self.cardnum()
        cardnaccount = self.cardnaccount()
        self.deposit()
        self.gameJurisdiction()
        self.gametime()
        self.Resources()
        self.appendix()
        '''通过判断jj的值 看是否存在流程，启用流程需要输入标题'''
        if jj == 1:
            time.sleep(2)
            title = self.title(channel_no)
            time.sleep(2)
            self.Submission()