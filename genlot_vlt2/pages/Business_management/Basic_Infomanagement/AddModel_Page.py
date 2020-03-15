#coding=utf-8
import os,random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from common.function import wait,log_info
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class addmodel_page(BasePage):
    """新增类型管理页面"""

    keep_btn = (By.XPATH, '//span[text()="提交并保存"]')
    remove_btn = (By.XPATH, '//span[text()="取消"]')
    msg_add = (By.XPATH, '//*[@id="main"]/div/div/div/h2')

    def click_keep_button(self):
        """点击提交按钮"""
        self.b.find_element(*self.keep_btn).click()
        wait(2)

    def click_remove_button(self):
        """点击取消按钮"""
        self.b.find_element(*self.remove_btn).click()

    def check_addmsg(self):
        """检查新增页面信息"""
        return self.b.find_element(*self.msg_add).text

    def select_goodstype(self, str):
        """选择物品类别"""
        button = self.get_element_by_xpath("//input[@placeholder='请选择']")
        self.b.execute_script("arguments[0].click()", button)
        if str == 1:
            self.get_element_by_xpath("//span[text()='设备']").click()
            log_info(u"物品类别选择:设备")
        elif str == 2:
            self.get_element_by_xpath("//span[text()='配件']").click()
            log_info(u"物品类别选择:配件")
        wait(1)

    def select_terminalname(self, str):
        """选择设备名称"""
        button = self.get_element_by_xpath("//input[@placeholder='请选择设备名称']")
        self.b.execute_script("arguments[0].click()", button)
        wait(1)
        el = self.b.find_elements_by_xpath("//span[contains(text(),'%s')]"%str)
        el[0].click()
        name = el[0].text
        log_info(u"设备名称选择:%s"%name)
        return name

    def select_partsname(self, str):
        """选择配件名称"""
        button = self.get_element_by_xpath("//input[@placeholder='请选择配件名称']")
        self.b.execute_script("arguments[0].click()", button)
        wait(1)
        el = self.b.find_elements_by_xpath("//span[contains(text(),'%s')]"%str)
        el[0].click()
        name = el[0].text
        log_info(u"配件名称选择:%s"%name)
        return name

    def input_termodel(self,str):
        """输入设备型号"""
        self.input_text(u'设备型号',str)
        log_info(u"设备型号输入:%s" % str)

    def input_partsmodel(self,str):
        """输入配件型号"""
        self.input_text(u'配件型号',str)
        log_info(u"配件型号输入:%s" % str)

    def input_terPrice(self, str):
        """输入设备单价"""
        self.input_text(u'设备单价(元)', str)
        log_info(u"设备单价(元)输入:%s" % str)

    def input_partsPrice(self, str):
        """输入配件单价"""
        self.input_text(u'配件单价(元)', str)
        log_info(u"配件单价(元)输入:%s" % str)

    def input_Supplier(self,str):
        """输入供应商"""
        self.input_text(u'供应商',str)
        log_info(u"供应商输入:%s" % str)

    def input_factory(self,str):
        """输入厂家信息"""
        self.input_text(u'厂家信息',str)
        log_info(u"厂家信息输入:%s" % str)

    def upload_picture(self,path):
        """上传图片"""
        el = self.get_element_by_xpath("//input[@name='file']/preceding-sibling::i[1]")
        el.click()
        wait(1)
        os.system(path)
        wait(3)
        # el.send_keys(path)
        log_info(u"上传图片ok")

    def input_Remarks(self, str):
        """输入备注"""
        el = self.get_element_by_xpath('//label[text()="备注"]')
        self.b.execute_script("arguments[0].scrollIntoView();", el)
        self.input_text(u'备注', str)
        log_info(u"输入备注")

    def select_terminal(self,str):
        """选择可用机型"""
        self.select_terminalname(str)
        button = self.get_element_by_xpath("//input[@placeholder='请选择设备型号']")
        self.b.execute_script("arguments[0].click()", button)
        #选择第一条型号
        self.b.find_elements_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]")[3].click()
