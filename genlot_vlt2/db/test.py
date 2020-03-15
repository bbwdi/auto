#coding=utf-8
from pages.Business_management.Business_Processing.Business_Processing_page import business_process
from pages.Business_management.Business_Processing.channelnewbuilt_page import New
from pages.Business_management.channel_list.channel_list_page import jump_channel_list_page
import unittest
from common.login_b import Login_B
from pages.home1_page import Home_Page
import time
import datetime


class aa(unittest.TestCase):
    def test_aa(self):
        list = [{"user": "gavin-sc", "password": "123456"}, {"user": "gavin-cq", "password": "123456"},{"user": "gavin-hn", "password": "123456"},{"user": "gavin-nmg", "password": "123456"}]
        rr1 = len(list)

        for i in range(rr1):

            try:
                a=Login_B(list[i]["user"],list[i]["password"])
                self.aa=Home_Page(a)
                self.aa.jumpBusinessmanagement()
                self.cc=business_process(a)
                self.cc.jump_channelnewbuilt()
                self.dd=New(a)
                time.sleep(2)
                self.dd.group()
                channel_no=self.dd.channelno()
                print channel_no
                # title=self.dd.title(channel_no)
                type=self.dd.channeltype()
                level=self.dd.channellevel()
                changsuo=self.dd.place1()
                mianji=self.dd.areainput()
                limit=self.dd.kailimit()
                limit1=self.dd.shiwanlimit()
                chongzhi=self.dd.Recharge()
                limit2=self.dd.people_limit()
                latitude=self.dd.latitude()
                longitude=self.dd.longitude()
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
                self.dd.Submission()
                time.sleep(2)
            except Exception  as e:
                print e

if __name__=="__main__":

    pass
