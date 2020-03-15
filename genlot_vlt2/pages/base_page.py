# coding:utf-8
import os
import sys
res=os.path.abspath(__file__) #获取当前文件的绝对路径
base_path=os.path.dirname(os.path.dirname(res)) #获取当前文件的上两级目录
sys.path.insert(0,base_path)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common import  function
from common.function import log_info
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
#from db.oracle_db import Oracle
import id_card
import SendKeys
from  run import create__browser_driver

#新增加
from selenium.webdriver.common.keys import Keys
from itertools import groupby
import re,csv
from db.oracle_db import Oracle
from datetime import datetime


base_url = "http://10.6.0.203:8888/#/login"
user_name='''//*[@id="app"]//div//span/span[@class='user-name']'''

class BasePage():
    def __init__(self, driver=''):
        b = driver
        if b == '':
            self.b = create__browser_driver()
        else:
            self.b = b
        self.b.maximize_window()
        self.b.implicitly_wait(10)

    def open(self,url = base_url):
        self.b.get(url)


    def get_title(self):
        return self.b.title

    def get_url(self):
        return self.b.current_url

    def close_browser(self):
        self.b.quit()

    def get_element_by_id(self,the_id):
        locator = (By.ID, the_id)
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            filename = 'can_not_find_element_by_id_%s' % the_id
            function.save_screenshot(self.b, filename)
            raise E
        return self.b.find_element_by_id(the_id)

    def get_element_by_tag_name(self,the_name):
        locator = (By.TAG_NAME, the_name)
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            filename = 'can_not_find_element_by_tag_name_%s' % the_name
            function.save_screenshot(self.b, filename)
            raise E
        return self.b.find_element_by_tag_name(the_name)

    def get_element_by_name(self, the_name):
        locator = (By.NAME, the_name)
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            filename = 'can_not_find_element_by_name_%s' % the_name
            function.save_screenshot(self.b, filename)
            raise E
        return self.b.find_element_by_name(the_name)

    def get_element_by_css(self, css):
        locator = (By.CSS_SELECTOR, css)
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            filename = 'can_not_find_element_by_css_%s' %css
            function.save_screenshot(self.b, filename)
            raise E
        return self.b.find_element_by_css_selector(css)

    def get_element_by_link_text(self, text):
        locator = (By.LINK_TEXT, text)
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            file_name = '%s_can_not_find_element_by_css_%s' %text
            function.save_screenshot(self.b, file_name)
            raise E
        return self.b.find_element_by_link_text(text)

    def get_element_by_xpath(self, xpath):
        locator = (By.XPATH, xpath)
        print locator
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            file_name = '%s_can_not_find_element_by_css_%s' %xpath
            function.save_screenshot(self.b, file_name)
            raise E
        return self.b.find_element_by_xpath(xpath)

    def get_elements_by_xpath(self, xpath):
        return self.b.find_elements_by_xpath(xpath)

    def get_frame(self,frame):
        return self.b.switch_to_frame(frame)
    def by_class(self, the_class_name):
        locator = (By.CLASS_NAME, the_class_name)
        try:
            WebDriverWait(self.b, 10).until(EC.visibility_of_element_located(locator))
        except EC.NoSuchElementException as E:
            file_name = '%s_can_not_find_element_by_id_%s' % the_class_name
            function.save_screenshot(self.b, file_name)
            raise E
        return self.b.find_element_by_class_name(the_class_name)

    def js(self, js_text):
        return self.b.execute_script(js_text)

    def accept(self):
        return self.b.switch_to.alert.accept()
    #断言：str3是字段名称，str1和str2是比较的字段
    def assert_message(self,str1,str2,str3):
        assert str1 == str2,u'%s断言失败,str1: %s  str2: %s'%(str3,str1,str2)
    def assert1(self,str1,str2):
        expect = self.b.find_element_by_xpath('''//*[contains(text(),'%s')]/following-sibling::div'''%str2).text
        #print self.assert_message(str1,expect,str2)
        if self.assert_message(str1,expect,str2) == None:
            print '%s 断言成功'%str2
    def assert2(self,str1,str2,str3):
        if self.assert_message(str1,str2,str3) == None:
            print '%s 断言成功'%str3
    def count_time(self,count):
        today = datetime.date.today()
        new_day = today + datetime.timedelta(days=count)
        return new_day
    #精确匹配字符串
    def get_text_accurate(self,str1):
        time.sleep(1)
        return self.b.find_element_by_xpath('''//*[text()='%s']'''%str1)
    #模糊匹配
    def get_text_obscure(self,str1):
        time.sleep(1)
        return self.b.find_element_by_xpath('''//*[contains(text(),'%s')]'''%str1)
    #多个相同的文字时，选择此方法
    def get_text_list(self,str1):
        time.sleep(1)
        list = self.b.find_elements_by_xpath('''//*[text()='%s']'''%str1)
        for i in list:
            try:
                i.click()
            except:
                continue
    #鼠标移动
    def mouse_over(self,el):
        ActionChains(self.b).move_to_element(el).perform()
    #通过输入字段名称，输入值
    def input_text(self,str1,str2):
         time.sleep(1)
         el = self.b.find_element_by_xpath('''//*[contains(text(),'%s')]/following-sibling::div/div/*'''%str1)
         el.clear()
         el.send_keys(str2)
    def input_text_accurate(self,str1,str2):
         time.sleep(1)
         el = self.b.find_element_by_xpath('''//*[text()=%s]/following-sibling::div/div/*'''%str1)
         el.clear()
         el.send_keys(str2)
    #根据前面的字段名称，点击挨着的字段
    def input_text_click(self,str1):
         time.sleep(1)
         el = self.b.find_element_by_xpath('''//*[text()=%s]/following-sibling::div/div/*'''%str1)
         el.click()
    #选择机构前面的圆圈
    def click_radio(self,str1):
         time.sleep(1)
         self.b.find_element_by_xpath('''//*[contains(text(),'%s')]/preceding-sibling::label/span'''%str1).click()

    #行数据，选择此方法
    def row_check(self,num):
        return self.b.find_element_by_xpath('''//tr[starts-with(@class,'el-table__row')]/td[%s]/div'''%num)

    def check_status(self):
        return self.b.find_element_by_xpath('''//div[starts-with(@role,'checkbox')]/span''').text
    #通过默认值选择
    def option_text(self,str):
        #选项函数，str为选项的输入提示#
        return self.b.find_element_by_xpath('''//input[starts-with(@placeholder,'%s')]'''%str)
    #输入所有的值
    def option_text_list(self,str):
        #选项函数，str1为选项的输入提示#
        list = self.b.find_elements_by_xpath('''//input[starts-with(@placeholder,'%s')]'''%str)
        for i in list:
            try:
                i.click()
            except:
                continue
    #生成身份证
    def id_card(self):
        return id_card.id_card()
    #下拉项
    def option(self,str):
        time.sleep(2)
        return self.b.get_element_by_xpath('''//*[text()='%s']/following-sibling::div/span/span'''%str)
    #生成唯一ID
    def create_id(self):
        return int(time.time())

    def create_mobile(self):
        return u'135' + str(int(time.time()))[2:]

    def create_identity_card(self):
        t=str(int(time.time()))+str(random.randint(1000000,9999999))
        return t

    def upload_file(self,path):
        time.sleep(2)
        SendKeys.SendKeys(path)
        SendKeys.SendKeys("{ENTER}")
    def next_day(self):
        return (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

    def check_database(self,sql):
        log_info(u"检查数据库")
        time.sleep(2)
        db = Oracle()
        result = db.run_sql(sql)
        db.disconnect()
        return result

    def find_rowdata(self,str):
        self.b.find_element_by_xpath()

    def input_xpath(self, str1, str2):
        time.sleep(1)
        el = self.b.find_element_by_xpath(str1)
        time.sleep(1)
        el.clear()
        time.sleep(1)
        el.send_keys(str2)

    def input_xpath_ComboBox(self, str1, str2):
        time.sleep(1)
        el = self.b.find_element_by_xpath(str1)
        time.sleep(1)
        # el.clear()
        # time.sleep(1)
        el.send_keys(str2)

    def export_file(self, filepath, filename):
        tt1 = '\\'
        print  filepath + tt1 + filename
        if os.path.exists(filepath + tt1 + filename):
            os.remove(filepath + tt1 + filename)
            print  u'删除成功'
            a = 'True'
            return a
        else:
            b = 'a'
            return b

    def sql_result(self, sql):
        a = Oracle()
        tt = a.run_sql_list(sql)
        if len(tt) == 0:
            a = 0
            return a
        else:
            return tt
    def sql_LOB_result(self, sql):
        a = Oracle()
        tt = a.run_sql_LOB(sql)
        if len(tt) == 0:
            a = 0
            return a
        else:
            return tt

    def ins(self):
        '''根据登陆用户拿相应的组织机构'''
        time.sleep(3)
        name=self.get_element_by_xpath(user_name).text
        user_ins_sql = ''' SELECT t.ins_id  from T_USER_INS t left join T_USER_INFO  k on t.user_id=k.user_id where  k.account='%s' '''%name
        kk=Oracle().run_sql_list(user_ins_sql)
        log_info(kk)
        print "kk=%s"%kk
        kk1=kk[0]
        log_info(kk1)
        return kk1



    '''====================================================新增加=============================================================='''

    def find_elements(self,*loc):
        '''查找一组元素'''
        time.sleep(1.2)
        return self.driver.find_elements(*loc)

    def find_element_for_xpath(self,*loc):
        '''查找一个元素'''
        time.sleep(1)
        return self.driver.find_element(*loc)

    def find_elements_for_xpath(self,*loc):
        '''查找一个元素'''
        time.sleep(1)
        return self.find_elements(*loc)

    def find_element_for_text(self,element_loc):
        '''查找一个文本元素'''
        visible_element=WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,element_loc)))
        operation=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,element_loc)))
        if visible_element and operation !='':
            time.sleep(0.1)
            return visible_element

    def find_elements_for_text(self,element_loc):
        '''查找一组文本元素'''
        visible_elements=WebDriverWait(self.driver,15).until(EC.presence_of_all_elements_located((By.XPATH,element_loc)))
        #operation=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,element_loc %ele_text)))
        if visible_elements:
            time.sleep(0.1)
            return visible_elements


    def find_element_for_text_link(self,link_text):
        '''查找文本链接元素'''
        link_loc=u'//*[contains(text(),"%s")]'
        return self.find_element_for_text(link_loc %link_text)

    def find_element_for_inside_text(self,inside_text):
        '''通过框内文本查找元素'''
        element_inside_loc=u'//*[starts-with(@placeholder,"%s")]'
        return self.find_element_for_text(element_inside_loc %inside_text)

    def find_element_for_outside_text(self,outside_text):
        '''通过框外文本查找元素'''
        element_outside_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/div/input'
        return self.find_element_for_text(element_outside_loc %outside_text)

    def find_elements_for_outside_text(self,outside_text):
        '''通过框外文本查找元素'''
        elements_outside_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/div/input'
        return self.find_elements_for_text(elements_outside_loc %outside_text)

    def input_time_for_more_than_one(self,element_text,time_text,num):
        '''输入时间（多个）'''
        time_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/input'
        self.find_elements_for_text(time_loc %element_text).pop(num-1).clear()
        self.find_elements_for_text(time_loc %element_text).pop(num-1).send_keys(time_text)

    def input_start_and_end_time(self,time_dict):
        '''输入开始时间和结束日期'''
        for key,value in time_dict.items():
            self.input_text_message_for_inside_text(key,value)
        self.click_browser_spacing()

    def input_time_for_one(self,element_text,time_text):
        '''输入时间（单个）'''
        time_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/input'
        self.find_element_for_text(time_loc %element_text).clear()
        self.find_element_for_text(time_loc %element_text).send_keys(time_text)

    def open_list_menu_by_inside_text(self,menu_name):
        '''打开下拉菜单,通过框内文本'''
        self.find_element_for_inside_text(menu_name).click()

    def open_list_menu_by_outside_text(self,menu_name):
        '''打开下拉菜单,通过框外文本'''
        self.find_element_for_outside_text(menu_name).click()

    def open_list_menu_and_choose_option_by_outside_text(self,menu_name,down_num):
        '''打开下拉菜单并选择选项,通过框外文本'''
        self.find_element_for_outside_text(menu_name).click()
        for n in range(down_num):
            down = self.find_element_for_outside_text(menu_name)
            down.send_keys(Keys.DOWN)
        self.find_element_for_outside_text(menu_name).send_keys(Keys.ENTER)

    def open_list_menu_and_choose_option_by_outside_text_for_more_than_one(self,menu_name,index,down_num):
        '''打开下拉菜单并选择选项,通过框外文本(有多个相同元素)'''
        self.find_elements_for_outside_text(menu_name).pop(index-1).click()
        for n in range(down_num):
            down = self.find_elements_for_outside_text(menu_name)
            down.pop(index-1).send_keys(Keys.DOWN)
        self.find_elements_for_outside_text(menu_name).pop(index-1).send_keys(Keys.ENTER)

    def open_list_menu_and_choose_option_by_inside_text(self,menu_name,down_num):
        '''打开下拉菜单并选择选项,通过框内文本'''
        self.find_element_for_inside_text(menu_name).click()
        for n in range(down_num):
            down = self.find_element_for_inside_text(menu_name)
            down.send_keys(Keys.DOWN)
        self.find_element_for_inside_text(menu_name).send_keys(Keys.ENTER)

    def open_menu_list_before_text_for_one(self,text_name):
            '''展开文本前的下拉菜单(元素唯一)'''
            menu_loc=u'//*[contains(text(),"%s")]/../span[1]'
            self.find_element_for_text(menu_loc %text_name).click()

    def click_option_by_inside_text_for_more_option(self,menu_name,option_name):
        '''打开下拉菜单并点击选择选项,通过框内文本'''
        option_loc=u'//div/ul/li/span[contains(text(),"%s")]'
        self.find_element_for_inside_text(menu_name).click()
        time.sleep(0.5)
        self.find_element_for_text(option_loc %option_name).click()
        time.sleep(1)

    def choose_more_option_by_inside_text(self,option_dict):
        '''操作多个下拉选择框(元素唯一)'''
        for key,value in option_dict.items():
            time.sleep(1)
            self.click_option_by_inside_text_for_more_option(key,value)

    def open_list_menu_by_outside_text_for_more_than_one(self,menu_name,index):
        '''打开下拉菜单,通过框外文本,定位元素多个'''
        self.find_elements_for_outside_text(menu_name).pop(index-1).click()

    def choose_list_option(self,option_num):
        '''选择列选项'''
        option_loc=u'//div[2]/table/tbody/tr[%s]/td[1]/div/label/span/span'
        self.find_element_for_text(option_loc %option_num).click()

    def click_button_for_one(self,button):
        '''点击按钮(按钮只有一个)'''
        button_loc=u'//*[contains(text(),"%s")]'
        self.find_element_for_text(button_loc %button).click()

    def click_search_button(self):
        '''点击查询按钮'''
        button_loc=u'//*[contains(text(),"查询")]/../i'
        self.find_element_for_text(button_loc).click()

    def click_edite_button(self,button):
        '''点击编辑按钮'''
        edite_loc=u'//*[contains(text(),"%s")]/following-sibling::div/label/span/span' %button
        self.find_element_for_text(edite_loc).click()

    def choose_check_box_before_text_for_one(self,box_text):
        '''选择文本前面的复选框，元素唯一'''
        box_loc=u'//*[contains(text(),"%s")]/../label/span/span'
        self.find_element_for_text(box_loc %box_text).click()

    def choose_check_box_before_text_for_more_than_one(self,box_text,index_num):
        '''选择文本前面的复选框,元素有多个'''
        box_loc=u'//*[contains(text(),"%s")]/../label/span/span'
        self.find_elements_for_text(box_loc %box_text).pop(index_num-1).click()

    def click_close_button_after_text_for_one(self,button_text):
        '''点击文本后的关闭按钮'''
        close_loc=u'//*[contains(text(),"%s")]/../i'
        self.find_element_for_text(close_loc %button_text).click()

    def choose_region_check_box_for_one(self,box_text):
        '''选择区域前的按钮(元素唯一)'''
        region_loc=u'//*[contains(text(),"%s")]/../label/span[1]'
        self.find_element_for_xpath(By.XPATH,region_loc %box_text).click()

    def choose_more_region_check_box_for_one(self,region_list):
        '''选择多个区域前的按钮(元素唯一)'''
        for value in region_list:
            self.choose_region_check_box_for_one(value)

    def choose_region_check_box_for_more_than_one(self,box_text,index_num):
        '''选择区域前的按钮(元素不唯一)'''
        region_loc=u'//*[contains(text(),"%s")]/../label/span[1]'
        self.find_elements_for_xpath(region_loc %box_text).pop(index_num-1).click()


    def click_button_for_more_than_one(self,button,element_index):
        '''点击按钮(有多个相同)'''
        button_more_loc=u'//*[contains(text(),"%s")]'
        self.find_elements_for_text(button_more_loc %button).pop(element_index-1).click()

    def click_more_button_for_one(self,click_list):
        '''点击多个按钮(每个按钮唯一)'''
        for value in click_list:
            time.sleep(1)
            self.click_button_for_one(value)

    def click_more_button_for_more_than_one(self,click_dict):
        '''点击多个按钮(按钮不唯一)'''
        for key,value in click_dict.items():
            self.click_button_for_more_than_one(key,value)

    def click_table_cell_button(self,list_nun,column_num):
        '''点击table某一单元按钮'''
        cell_loc=u'//table/tbody/tr[%s]/td[%s]//div/button'
        self.find_elements_for_text(cell_loc %(list_nun,column_num)).pop(1).click()

    def click_table_cell_operation_button(self,list_nun,column_num,button_num,index_num=2):
        '''点击table操作下的按钮'''
        cell_loc=u'//table/tbody/tr[%s]/td[%s]//div/button[%s]'
        time.sleep(0.5)
        self.find_elements_for_text(cell_loc %(list_nun,column_num,button_num)).pop(index_num-1).click()

    def input_text_message_for_outside_text(self,ele_text,message):
        '''输入文本信息(通过框外的文本)'''
        outside_text_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/*'
        self.find_element_for_text(outside_text_loc %ele_text).clear()
        self.find_element_for_text(outside_text_loc %ele_text).send_keys(message)

    def input_text_message_for_outside_text_more_than_one(self,ele_text,text_num,message):
        '''输入文本信息(通过框外的文本,有多各相同字段)'''
        outside_text_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/*'
        self.find_elements_for_text(outside_text_loc %ele_text).pop(text_num-1).clear()
        self.find_elements_for_text(outside_text_loc %ele_text).pop(text_num-1).send_keys(message)

    def input_text_message_for_inside_text_more_than_one(self,ele_text,text_num,message):
        '''输入文本信息(通过框内的文本,有多各相同字段)'''
        inside_text_loc=u'//*[starts-with(@placeholder,"%s")]'
        self.find_elements_for_text(inside_text_loc %ele_text).pop(text_num-1).clear()
        self.find_elements_for_text(inside_text_loc %ele_text).pop(text_num-1).send_keys(message)

    def input_text_message_for_inside_text(self,ele_text,message):
        '''输入文本信息(通过框内的文本)'''
        inside_text_loc=u'//*[starts-with(@placeholder,"%s")]'
        self.find_element_for_text(inside_text_loc %ele_text).clear()
        self.find_element_for_text(inside_text_loc %ele_text).send_keys(message)

    def input_more_text_message_for_outside_text(self,info_dict):
        '''输入多个信息,无编辑按钮'''
        for key,value in info_dict.items():
            self.input_text_message_for_outside_text(key,value)

    def input_more_text_message_for_outside_text_more_than_one(self,info_dict):
        '''输入多个文本信息(通过框外的文本,有多各相同字段,无编辑按钮)'''
        for key,value in info_dict.items():
            for i in range(len(value)):
                self.input_text_message_for_outside_text_more_than_one(key,value[i][0],value[i][1])

    def input_more_text_message_for_inside_text_more_than_one(self,info_dict):
        '''输入多个文本信息(通过框外的文本,有多各相同字段,无编辑按钮)'''
        for key,value in info_dict.items():
            for i in range(len(value)):
                self.input_text_message_for_inside_text_more_than_one(key,value[i][0],value[i][1])

    def input_more_text_message_for_inside_text(self,info_dict):
        '''输入多个信息,无编辑按钮'''
        for key,value in info_dict.items():
            self.input_text_message_for_inside_text(key,value)

    def input_more_text_message_with_edite_for_outside_text(self,info_dict):
        '''输入多个信息,有编辑按钮'''
        for key,value in info_dict.items():
            self.click_edite_button(key)
            self.input_text_message_for_outside_text(key,value)

    def choose_more_list_with_edite_by_outside_text(self,choose_dict):
        '''多个下拉菜单选择,有编辑按钮(传参为字典)'''
        for key,value in choose_dict.items():
            self.click_edite_button(key)
            self.open_list_menu_and_choose_option_by_outside_text(key,value)

    def choose_more_list_with_edite_for_outside_text_more_than_one(self,choose_dict):
        '''多个下拉菜单选择,有编辑按钮(传参为字典,通过框外的文本,有多各相同字段)'''
        for key,value in choose_dict.items():
            self.click_edite_button(key)
            for i in range(len(value)):
                 self.open_list_menu_and_choose_option_by_outside_text_for_more_than_one(key,value[i][0],value[i][1])

    def choose_more_list_by_outside_text(self,choose_dict):
        '''执行多项下拉菜单选择,无编辑按钮(传参为字典，框外文本)'''
        for key,value in choose_dict.items():
            self.open_list_menu_and_choose_option_by_outside_text(key,value)

    def choose_more_list_by_inside_text(self,choose_dict):
        '''执行多项下拉菜单选择,无编辑按钮(传参为字典，框内文本)'''
        for key,value in choose_dict.items():
            self.open_list_menu_and_choose_option_by_inside_text(key,value)

    down_text_loc=u'//*[contains(text(),"%s")]/following-sibling::div/div/div/input'
    def keyboard_down_by_outside_text_more_than_one(self,loc_values=down_text_loc,menu_name='',down_num='',index=0):
        '''操作键盘向下键选第n项'''
        for n in range(down_num):
            down = self.find_elements_for_text(loc_values %menu_name)
            down.pop(index-1).send_keys(Keys.DOWN)
        self.find_elements_for_text(loc_values %menu_name).pop(index-1).send_keys(Keys.ENTER)

    def keyboard_down_by_outside_text(self,menu_loc,down_num):
        '''通过框外文本操作键盘向下键选第n项'''
        for n in range(down_num):
            down = self.find_element_for_outside_text(menu_loc)
            down.send_keys(Keys.DOWN)
        self.find_element_for_outside_text(menu_loc).send_keys(Keys.ENTER)

    def keyboard_down_by_inside_text(self,menu_loc,down_num):
        u'''通过框内文本操作键盘向下键选第n项'''
        for n in range(down_num):
            down = self.find_element_for_inside_text(menu_loc)
            down.send_keys(Keys.DOWN)
        self.find_element_for_inside_text(menu_loc).send_keys(Keys.ENTER)

    path = u"D:/zxl_project/test.png"
    def upload_file_for_more_than_one(self,num=1,file_path = path):
        '''上传附件文件'''
        self.find_elements_for_xpath(By.NAME,u'file').pop(num-1).send_keys(file_path)
        time.sleep(1)

    def upload_file_for_one(self,file_path = path):
        '''上传附件文件'''
        self.find_element_for_xpath(By.NAME,u'file').send_keys(file_path)
        time.sleep(5)

    def upload_annex_file_for_one(self,description=u'上传图片'):
        '''上传附件(只有上传附件)'''
        self.click_button_for_one(u'打开上传')
        self.upload_file_for_one()
        self.input_text_message_for_outside_text(u'附件描述',description)
        self.click_button_for_one(u'上传到服务器')
        self.click_button_for_one(u'查看记录')
        self.click_button_for_more_than_one(u'关 闭',2)

    def upload_annex_file_for_more_than_one(self,upload_num,description=u'上传图片'):
        '''上传附件(有多各上传点)'''
        self.click_button_for_one(u'打开上传')
        self.upload_file_for_more_than_one(num=upload_num)
        self.input_text_message_for_outside_text(u'附件描述',description)
        self.click_button_for_more_than_one(u'上传到服务器',upload_num)
        self.click_button_for_one(u'查看记录')
        self.click_button_for_more_than_one(u'关 闭',2)

    def upload_certificate_file_for_one(self):
        '''上传证件照(只有一个上传点)'''
        self.upload_file_for_one()
        self.click_button_for_one(u'上传到服务器')

    def upload_certificate_file_for_more_than_one(self,upload_num):
        '''上传证件照(有多各上传点)'''
        self.upload_file_for_more_than_one(num=upload_num)
        self.click_button_for_more_than_one(u'上传到服务器',upload_num)

    def get_text_info(self,text_info):
        '''获取页面文本信息(详情)'''
        text_loc=u'//*[contains(text(),"%s")]/../p'
        return self.find_element_for_text(text_loc %text_info).text

    def get_search_text(self,list_num=1):
        '''获取查询列表第n行第二列的信息'''
        search_loc=u'//table/tbody/tr[%s]/td[2]/div'
        return self.find_element_for_xpath(By.XPATH,search_loc %list_num).text

    def get_table_cell_text(self,list_num,column_num):
        '''获取table某一单元信息'''
        cell_loc=u'//table/tbody/tr[%s]/td[%s]/div'
        return self.find_element_for_text(cell_loc %(list_num,column_num)).text

    def get_search_count(self,count_text=u'共搜索到'):
        '''获取搜索结果条数'''
        count_loc=u'//*[contains(text(),"%s")]/./em'
        return self.find_element_for_text(count_loc %count_text).text

    def get_footer_count_by_inside_text(self,inside_text=u"请选择"):
        '''获取页脚统计条数(提取数字)'''
        time.sleep(1)
        footer_loc=u'//*[starts-with(@placeholder,"%s")]/../../../../span'
        result_text=self.find_element_for_text(footer_loc %inside_text).text
        count_digital=re.sub(u"\D", u"", result_text)
        return count_digital

    def get_button_attribute(self,text_name,attr_name):
        '''获取元素属性'''
        attr_loc=u'//*[contains(text(),"%s")]/..'
        return self.find_element_for_xpath(By.XPATH,attr_loc %text_name).get_attribute(attr_name)

    def get_now_date(self):
        '''获取当前日期'''
        return datetime.now().strftime('%Y-%m-%d')

    def get_now_time(self):
        '''获取当前日期'''
        return datetime.now().strftime('%H:%M:%S')

    def search_information(self,info_dict,choose_dict,time_dict):
        '''页面信息查询'''
        if info_dict!={}:
            self.input_more_text_message_for_inside_text(info_dict)
        if choose_dict!={}:
            self.choose_more_option_by_inside_text(choose_dict)
        if time_dict!={}:
            self.input_start_and_end_time(time_dict)
        self.click_search_button()
        time.sleep(3)

    def get_print_title(self):
        '''获取打印页面title'''
        return self.driver.title

    imagePath = u'D:/zxl_project/VLT/genlot_vlt/static/images/%s.png'
    def screen_shot(self,path = imagePath,image_name=''):
        '''截屏'''
        nowTime = time.strftime(u'%Y-%m-%d.%H.%M.%S')
        file_name = image_name+nowTime
        self.driver.get_screenshot_as_file(path%file_name)


    def assert_result_equal(self,expected,actual,file_name):
        '''断言'''
        try:
            self.assertEqual(expected,actual)
        except:
            self.screen_shot(path=self.imagePath,image_name=file_name+u'-')
            raise

    def assert_result_not_equal(self,expected,actual,file_name):
        '''断言'''
        try:
            self.assertNotEqual(expected,actual)
        except:
            self.screen_shot(path=self.imagePath,image_name=file_name+u'-')
            raise

    def assert_result_in(self,expected,actual,file_name):
        '''断言(a in b)'''
        try:
            self.assertIn(expected,actual)
        except:
            self.screen_shot(path=self.imagePath,image_name=file_name+u'-')
            raise

    def assert_result_not_in(self,expected,actual,file_name):
        '''断言(a in b)'''
        try:
            self.assertNotIn(expected,actual)
        except:
            self.screen_shot(path=self.imagePath,image_name=file_name+u'-')
            raise

    def get_tips(self,tips_loc='/html/body/div'):
        '''获取提示信息'''
        time.sleep(1)
        tips=self.find_elements_for_text(tips_loc).pop(-1).text
        return tips

    def get_download_file_and_clear(self,file_name):
        '''判断是否存在某以文件'''
        time.sleep(8)
        result=os.path.exists(file_name)
        if result:
            os.remove(file_name)
            print(u'已删除文件%s' %file_name)
            return result
        else:
            print(u'文件：%s不存在' %file_name)

    def clear_download_file(self,result,download_file):
        '''删除导出的数据文件'''
        if result:
            os.remove(download_file)
            print(u'已删除文件%s' %download_file)

    def click_browser_spacing(self):
        '''点击浏览器空白处'''
        ActionChains(self.driver).move_by_offset(200,100).click().perform()


    def reader_csv(self,file):
        '''读取csv数据'''
        with open(file,'rb') as csvfile:
            code_reader=csv.reader(csvfile,dialect='excel')
            for row in code_reader:
                return row

    def write_data_to_csv(self,file,number):
        '''将数据写入csv'''
        with open(file,'wb+') as csvfile:
            code_writer=csv.writer(csvfile,dialect='excel')
            code_writer.writerow(number)

    def get_role_number(self,file_name):
        '''获取角色编号,加1后写入csv'''
        read_number=self.reader_csv(file_name)
        number=int(read_number[0])+1
        self.write_data_to_csv(file_name,[number])
        return number

    def get_plan_number(self,file_name):
        '''获取角色编号,加1后写入csv'''
        read_number=self.reader_csv(file_name)
        number=int(read_number[0])+1
        self.write_data_to_csv(file_name,[number])
        return number

    def get_data_count(self,select_sql):
        '''从数据库查询条数'''
        select=Oracle()
        result=select.get_data(select_sql)
        return len(result)

    def get_column_value(self,sql):
        '''从数据库查询列值'''
        select=Oracle()
        result=select.run_sql(sql)
        return result

    def refresh_page(self):
        '''刷新页面'''
        self.driver.refresh()

    def mouse_hover(self,*loc):
        '''鼠标悬停'''
        right_click = self.driver.find_element(*loc)
        ActionChains(self.driver).move_to_element(right_click).perform()

    def right_click(self,*loc):
        '''右击'''
        right = self.driver.find_element(*loc)
        ActionChains(self.driver).context_click(right).perform()

    def press_enter(self,*loc):
        '''enter键操作'''
        self.driver.find_element(*loc).send_keys(Keys.ENTER)

    def on_page(self):
        return self.driver.current_url == (self.base_url +self.url)

    def script(self,scr):
        return self.driver.execute_script(scr)

    def right_scroll(self,css_name,distance):
        '''向右滚动滚动条'''
        js = u"document.querySelector('.%s').scrollLeft = %s" %(css_name,distance)
        self.driver.execute_script(js)

    def user_login(self,user_name='zxl_test',password='123456'):
        '''用户登录'''
        log_info(u"开始登录")
        self.p = self.driver.get("http://10.6.0.203:8888/#/login")
        # username = u'zxl_test'
        # password = u'123456'
        time.sleep(5)
        un = self.driver.find_element_by_xpath('''//input[starts-with(@placeholder,'请输入用户账号')]''')
        pw = self.driver.find_element_by_xpath('''//input[starts-with(@placeholder,'请输入用户密码')]''')
        login_btn = self.driver.find_element_by_xpath('''//span[contains(text(),'登录')]''')
        # un.clear()
        # pw.clear()
        un.send_keys(user_name)
        pw.send_keys(password)
        login_btn.click()
        time.sleep(5)

    def keyboard_right(self,right_loc):
        '''键盘向右'''
        right = self.find_element_for_xpath(By.XPATH,right_loc)
        right.click()
        # right.send_keys(Keys.ENTER)
        right.send_keys(Keys.RIGHT)
        time.sleep(5)


    def browser_ask(self,Ask):
        '''处理浏览器弹框'''
        self.ask = self.driver.switch_to_alert()
        if Ask is u'accept':
            self.ask.accept()
        elif Ask is u'dismiss':
            self.ask.dismiss()

if __name__ == '__main__':
    pass