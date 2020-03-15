#coding=utf-8
from pages.base_page import BasePage
import  sys
print sys.path
import time
from pages.Business_management.channel_list import jump_channel_list_page

zhankai='''//*[@id="main"]//button[3]/span[contains(text(),'展开')]'''
input_channel_no='''//*[@id="main"]//input[@placeholder='请输入渠道编号']'''
input_channel_type='''//*[@id="main"]//input[@placeholder='请选择渠道类型']'''
input_channel_level='''//*[@id="main"]//input[@placeholder='请选择渠道等级']'''
input_person ='''//*[@id="main"]//input[@placeholder='请输入负责人']'''
input_phone='''//*[@id="main"]//input[@placeholder='请输入联系电话']'''
input_date='''//*[@id="main"]//input[@placeholder='开始日期']'''
click_query_button='''//*[@id="main"]//button[1]/span[text()='查询']'''
class channellist_query(BasePage):
    def query(self,channer_no='',channel_type='',channel_level='',person='',phone='',date=''):
        a=jump_channel_list_page()
        a.jump()
        self.get_element_by_xpath(zhankai).click()#点击展开
        self.input_text_click(input_channel_no).send_keys(channer_no)
        self.input_text_click(input_channel_type).send_keys(channel_type)
        self.input_text_click(input_person ).send_keys(channel_level)
        self.input_text_click(input_person).send_keys(person)
        self.input_text_click(input_person).send_keys(phone)
        self.input_text_click(input_person).send_keys(date)
        self.get_element_by_xpath(click_query_button).click()







if __name__=="__main__":
    pass

