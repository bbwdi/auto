#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.channelnewbuilt_page import New
from pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class new(unittest.TestCase):
    def setUp(self):
        a=Login_B()
        self.aa=Home_Page(a)
        self.aa.jumpBusinessmanagement()
        self.cc=business_process(a)
        self.cc.jump_channelnewbuilt()
        self.dd=New(a)


    def test_new(self):
        '''新建省级渠道'''
        jj=self.dd.isprocess()
        self.dd.group()
        channel_no=self.dd.channelno()
        print channel_no
        type=self.dd.channeltype()
        level=self.dd.channellevel()
        changsuo=self.dd.place1()
        mianji=self.dd.areainput()
        limit=self.dd.kailimit()
        limit1=self.dd.shiwanlimit()
        chongzhi=self.dd.Recharge()
        limit2=self.dd.people_limit()
        # latitude=self.dd.latitude()
        # longitude=self.dd.longitude()
        zhanshinum = self.dd.zhanshi()
        address=self.dd.channeladdress()
        name=self.dd.name()
        sex=self.dd.sex()
        phone=self.dd.phone()
        cardid=self.dd.cardid()
        tt=datetime.datetime.now()
        kk=tt.year
        age=str(int(kk)-int(cardid[6:10]))
        address1=self.dd.Contact_address()
        self.dd.Photo()
        cardnum=self.dd.cardnum()
        cardnaccount=self.dd.cardnaccount()
        self.dd.deposit()
        self.dd.gameJurisdiction()
        self.dd.gametime()
        self.dd.Resources()
        self.dd.appendix()
        '''通过判断jj的值 看是否存在流程，启用流程需要输入标题'''
        if jj == 1:
            time.sleep(2)
            title = self.dd.title(channel_no)
            time.sleep(2)
            self.dd.Submission()
            time.sleep(2)

            tt = self.dd.data()
            bb = len(tt)
            self.assertEqual(channel_no, tt["channelData"]["channelNo"])
            self.assertEqual(title, tt["channelData"]["title"])
            self.assertEqual(type, tt["channelData"]["channelType"])
            self.assertEqual(level, tt["channelData"]["channelLevelId"])
            # self.assertEqual(changsuo,tt["channelData"]["channelNo"])

            self.assertEqual(mianji, tt["financeData"]["pointArea"])
            self.assertEqual(limit, tt["channelData"]["buyCardLimit"])
            self.assertEqual(limit1, tt["channelData"]["tryCardLimit"])
            self.assertEqual(chongzhi, tt["channelData"]["rechargeCount"])
            self.assertEqual(limit2, tt["channelData"]["channelLimit"])
            # self.assertEqual(latitude, str(tt["channelData"]["latitude"]))
            # self.assertEqual(longitude, str(tt["channelData"]["longitude"]))
            self.assertEqual(address, tt["channelData"]["channelAddress"])
            self.assertEqual(name, tt["channelFundData"]["accountName"])
            self.assertEqual(sex, tt["channelFundData"]["sex"])
            self.assertIn(phone, str(tt["channelFundData"]["phone"]))
            # self.assertEqual(phone, tt["channelFundData"]["phone"])
            self.assertEqual(cardid, tt["channelFundData"]["channelIdentity"])
            self.assertEqual(age, str(tt["channelFundData"]["age"]))
            self.assertEqual(address1, tt["channelFundData"]["address"])
            self.assertEqual(zhanshinum, str(tt["channelData"]["showMachineCount"]))
            self.assertEqual(cardnum, str(tt["cardRuleData"]["costMoreThan"]))
            self.assertEqual(cardnaccount, str(tt["cardRuleData"]["charge"]))
            print '%%%%%%%%%%%%%%%%%%'
        else:
            time.sleep(2)
            self.dd.Submission()
            '''调用渠道列表  对比数据 暂时不用'''
            # channnel_list=jump_channel_list_page()
            # kk=channnel_list.querydetail()
            # tt1 = channnel_list.querydetail()  # 二进制
            # tt = channnel_list.view_channel()  # Unicode
            # aa = tt1[0]
            # for i in range(13):
            #     '''数据库拿出来的有float型，页面都是Unicode型，需要转化成str比较'''
            #     c = aa[i]
            #     c = str(c)
            #     self.assertEqual(c, tt[i])
            '''插入数据和数据库对比'''
            tt=self.dd.querydetail(channel_no)
            tt1=tt[0]
            bb=len(tt1)
            a=list(tt1)
            for i in range(bb):
                a[i]=str(a[i])
            self.assertEqual(channel_no,a[0])
            self.assertEqual(type, a[1])
            self.assertEqual(level, a[2])
            self.assertEqual(changsuo, a[3])
            self.assertEqual(mianji, a[4])
            self.assertEqual(limit, a[5])
            self.assertEqual(limit1, a[6])
            self.assertEqual(chongzhi,a[7])
            self.assertEqual(limit2, a[8])
            # self.assertEqual(latitude, a[9])
            # self.assertEqual(longitude, a[10])
            self.assertEqual(address, a[11])
            self.assertEqual(name, a[12])
            self.assertEqual(sex, a[13])
            self.assertEqual(phone, a[14])
            self.assertEqual(cardid, a[15])
            self.assertEqual(age, a[16])
            self.assertEqual(address1, a[17])
            self.assertEqual(channel_no, tt1[18])
            self.assertEqual(channel_no, tt1[19])
            self.assertEqual(channel_no, tt1[20])
            self.assertEqual(channel_no, tt1[0])
            print '*******************'


    def test_new_shi(self):
        '''新建市级渠道'''
        # 判断是否走流程 1代表走  需要从流程表中取数据对比 0代表不走流程 对比数据从channel info
        jj = self.dd.isprocess()
        self.dd.group(2)
        channel_no = self.dd.channelno()
        print channel_no
        type = self.dd.channeltype()
        level = self.dd.channellevel()
        changsuo = self.dd.place1()
        mianji = self.dd.areainput()
        limit = self.dd.kailimit()
        limit1 = self.dd.shiwanlimit()
        chongzhi = self.dd.Recharge()
        limit2 = self.dd.people_limit()
        # latitude=self.dd.latitude()
        # longitude=self.dd.longitude()
        zhanshinum = self.dd.zhanshi()
        address = self.dd.channeladdress()
        name = self.dd.name()
        sex = self.dd.sex()
        phone = self.dd.phone()
        cardid = self.dd.cardid()
        tt = datetime.datetime.now()
        kk = tt.year
        age = str(int(kk) - int(cardid[6:10]))
        address1 = self.dd.Contact_address()
        self.dd.Photo()
        cardnum = self.dd.cardnum()
        cardnaccount = self.dd.cardnaccount()
        self.dd.deposit()
        self.dd.gameJurisdiction()
        self.dd.gametime()
        self.dd.Resources()
        self.dd.appendix()
        '''通过判断jj的值 看是否存在流程，启用流程需要输入标题'''
        if jj == 1:
            time.sleep(2)
            title = self.dd.title(channel_no)
            time.sleep(2)
            self.dd.Submission()
            time.sleep(2)

            tt = self.dd.data()
            bb = len(tt)
            self.assertEqual(channel_no, tt["channelData"]["channelNo"])
            self.assertEqual(title, tt["channelData"]["title"])
            self.assertEqual(type, tt["channelData"]["channelType"])
            self.assertEqual(level, tt["channelData"]["channelLevelId"])
            # self.assertEqual(changsuo,tt["channelData"]["channelNo"])

            self.assertEqual(mianji, tt["financeData"]["pointArea"])
            self.assertEqual(limit, tt["channelData"]["buyCardLimit"])
            self.assertEqual(limit1, tt["channelData"]["tryCardLimit"])
            self.assertEqual(chongzhi, tt["channelData"]["rechargeCount"])
            self.assertEqual(limit2, tt["channelData"]["channelLimit"])
            # self.assertEqual(latitude, str(tt["channelData"]["latitude"]))
            # self.assertEqual(longitude, str(tt["channelData"]["longitude"]))
            self.assertEqual(address, tt["channelData"]["channelAddress"])
            self.assertEqual(name, tt["channelFundData"]["accountName"])
            self.assertEqual(sex, tt["channelFundData"]["sex"])
            self.assertIn(phone, str(tt["channelFundData"]["phone"]))
            # self.assertEqual(phone, tt["channelFundData"]["phone"])
            self.assertEqual(cardid, tt["channelFundData"]["channelIdentity"])
            self.assertEqual(age, str(tt["channelFundData"]["age"]))
            self.assertEqual(address1, tt["channelFundData"]["address"])
            self.assertEqual(zhanshinum, str(tt["channelData"]["showMachineCount"]))
            self.assertEqual(cardnum, str(tt["cardRuleData"]["costMoreThan"]))
            self.assertEqual(cardnaccount, str(tt["cardRuleData"]["charge"]))
            print '%%%%%%%%%%%%%%%%%%'
        else:
            time.sleep(2)
            self.dd.Submission()
            '''调用渠道列表  对比数据 暂时不用'''
            # channnel_list=jump_channel_list_page()
            # kk=channnel_list.querydetail()
            # tt1 = channnel_list.querydetail()  # 二进制
            # tt = channnel_list.view_channel()  # Unicode
            # aa = tt1[0]
            # for i in range(13):
            #     '''数据库拿出来的有float型，页面都是Unicode型，需要转化成str比较'''
            #     c = aa[i]
            #     c = str(c)
            #     self.assertEqual(c, tt[i])
            '''插入数据和数据库对比'''
            tt = self.dd.querydetail(channel_no)
            tt1 = tt[0]
            bb = len(tt1)
            a = list(tt1)
            for i in range(bb):
                a[i] = str(a[i])
            self.assertEqual(channel_no, a[0])
            self.assertEqual(type, a[1])
            self.assertEqual(level, a[2])
            self.assertEqual(changsuo, a[3])
            self.assertEqual(mianji, a[4])
            self.assertEqual(limit, a[5])
            self.assertEqual(limit1, a[6])
            self.assertEqual(chongzhi, a[7])
            self.assertEqual(limit2, a[8])
            # self.assertEqual(latitude, a[9])
            # self.assertEqual(longitude, a[10])
            self.assertEqual(address, a[11])
            self.assertEqual(name, a[12])
            self.assertEqual(sex, a[13])
            self.assertEqual(phone, a[14])
            self.assertEqual(cardid, a[15])
            self.assertEqual(age, a[16])
            self.assertEqual(address1, a[17])
            self.assertEqual(channel_no, tt1[18])
            self.assertEqual(channel_no, tt1[19])
            self.assertEqual(channel_no, tt1[20])
            self.assertEqual(channel_no, tt1[0])
            print '*******************'




    # def test_dd(self):
    #     kk=self.dd.data1()
    #     print kk

    def runTest(self):
        pass

    def tearDown(self):
        self.cc.close_browser()