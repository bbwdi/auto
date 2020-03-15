#coding=utf-8
from selenium import webdriver
from  base_page import BasePage
import time
url = "http://10.6.0.203:8888/#/entry"#要登陆的url
# url = "http://10.6.0.83:8888/#/entry"#要登陆的url
user = "admin"
password = "123456"
userinput="//input[@placeholder='请输入用户账号']"
passwordinput="//input[@placeholder='请输入用户密码']"
button='''//*[@id="app"]//span[text()='登录']'''

class system_login(BasePage):
    def user_path(self,user):
        # self.b.find_element_by_xpath(userinput).clear()
        self.b.find_element_by_xpath(userinput).send_keys(user)#输入用户名
    def passwd_path(self,password):
        # self.b.find_element_by_xpath(userinput).clear()
        self.b.find_element_by_xpath(passwordinput).send_keys(password)  # 输入密码
    def click_path(self):
        self.b.find_element_by_xpath(button).click()  # 点击登陆


if __name__=='__main__':
    # a=system_login()
    # a.user_path(user)
    # a.passwd_path(password)
    # a.click_path()
    # time.sleep(1)
    pass