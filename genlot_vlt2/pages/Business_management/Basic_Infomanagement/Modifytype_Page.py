#coding=utf-8
import os
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from common.function import wait,log_info
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class modifytype_page(BasePage):
    """修改类型管理页面"""

    keep_btn = (By.XPATH, '//span[text()="提交并保存"]')
    remove_btn = (By.XPATH, '//span[text()="取消"]')

    def click_keep_button(self):
        """点击提交按钮"""
        self.b.find_element(*self.keep_btn).click()
        wait(2)

    def click_remove_button(self):
        """点击取消按钮"""
        self.b.find_element(*self.remove_btn).click()

    def select_terminaltype(self, str):
        """选择设备类型"""
        button = self.get_element_by_xpath("//input[@placeholder='请选择设备类型']")
        self.b.execute_script("arguments[0].click()", button)
        if str == 1:
            self.get_element_by_xpath("//span[text()='终端机']").click()
            log_info(u"设备类型选择:终端机")
        elif str == 2:
            self.get_element_by_xpath("//span[text()='柜员机']").click()
            log_info(u"设备类型选择:柜员机")
        elif str == 3:
            self.get_element_by_xpath("//span[text()='其它']").click()
            log_info(u"设备类型选择:其它")
        wait(1)

    def select_Consumablestype(self, str):
        """选择耗材类型"""
        self.get_element_by_xpath("//input[@placeholder='请选择耗材类型']").click()
        if str == 1:
            self.get_element_by_xpath("//span[text()='投注卡']").click()
            log_info(u"耗材类型选择:投注卡")
        elif str == 2:
            self.get_element_by_xpath("//span[text()='其它']").click()
            log_info(u"耗材类型选择:其它")

    def input_tername(self,str):
        """输入设备名称"""
        self.input_text(u'设备名称',str)
        log_info(u"设备名称输入:%s" % str)

    def input_partsname(self,str):
        """输入配件名称"""
        self.input_text(u'配件名称',str)
        log_info(u"配件名称输入:%s" % str)

    def input_Consumablesname(self,str):
        """输入耗材名称"""
        self.input_text(u'耗材名称',str)
        log_info(u"耗材名称输入:%s" % str)

    def input_facilitiesname(self,str):
        """输入设施名称"""
        self.input_text(u'设施名称',str)
        log_info(u"设施名称输入:%s" % str)

    def input_Consumablesnum(self,str):
        """输入耗材编号"""
        self.input_text(u'耗材编号',str)
        log_info(u"耗材编号输入:%s" % str)

    def input_facilitiesnum(self,str):
        """输入设施编号"""
        self.input_text(u'施编号',str)
        log_info(u"施编号输入:%s" % str)

    def input_partsunit(self,str):
        """输入配件单位"""
        self.input_text(u'配件单位',str)
        log_info(u"配件单位输入:%s" % str)

    def input_facilitiesunit(self,str):
        """输入设施单位"""
        self.input_text(u'设施单位',str)
        log_info(u"设施单位输入:%s" % str)

    def input_ConsumablesunitPrice(self, str):
        """输入耗材单价"""
        self.input_text(u'耗材单价(元)', str)
        log_info(u"耗材单价(元)输入:%s" % str)

    def input_facilitiesunitPrice(self, str):
        """输入设施单价"""
        self.input_text(u'设施单价(元)', str)
        log_info(u"设施单价(元)输入:%s" % str)

    def input_Supplier(self,str):
        """输入供应商"""
        self.input_text(u'供应商',str)
        log_info(u"供应商输入:%s" % str)

    def input_factory(self,str):
        """输入厂家信息"""
        self.input_text(u'厂家信息',str)
        log_info(u"厂家信息输入:%s" % str)

    def input_Consumablesunit(self,str):
        """输入耗材单位"""
        self.input_text(u'耗材单位',str)
        log_info(u"耗材单位输入:%s" % str)

    def upload_picture(self,path):
        """上传图片"""
        el = self.get_element_by_xpath("//input[@name='file']/preceding-sibling::i[1]")
        el.click()
        wait(1)
        os.system(path)
        wait(3)
        log_info(u"上传图片ok")

    def input_terunit(self, str):
        """输入设备单位"""
        self.input_text(u'设备单位', str)
        log_info(u"设备单位输入:%s" % str)

    def select_standard(self,str):
        """选择是否标配"""
        if str == 1:
            self.get_element_by_xpath("//label[text()='是否标配']/following-sibling::div/div/label[1]/span/span").click()
            log_info(u"是否标配选择:是" )
        elif str == 2:
            self.get_element_by_xpath("//label[text()='是否标配']/following-sibling::div/div/label[2]/span/span").click()
            log_info(u"是否标配选择:否")

    def select_recycled(self,str):
        """选择是否回收"""
        if str == 1:
            self.get_element_by_xpath("//label[text()='是否回收']/following-sibling::div/div/label[1]/span/span").click()
            log_info(u"是否回收选择:是")
        elif str == 2:
            self.get_element_by_xpath("//label[text()='是否回收']/following-sibling::div/div/label[2]/span/span").click()
            log_info(u"是否回收选择:否")

    def input_Remarks(self, str):
        """输入备注"""
        el = self.get_element_by_xpath('//label[text()="备注"]')
        self.b.execute_script("arguments[0].scrollIntoView();", el)
        self.input_text(u'备注', str)
        log_info(u"输入备注")

    def delete_picture(self):
        """删除全部图片"""
        el = self.b.find_elements_by_xpath("//span[@class='el-upload-list__item-delete']")
        for i in range(len(el)):
            self.b.execute_script("arguments[0].click();", el[i])
        wait(1)
        log_info(u"删除全部的图片")