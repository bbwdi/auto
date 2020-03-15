#coding=utf-8
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from common.function import wait,log_info


class type_page(BasePage):
    """类型管理页面"""

    query_btn = (By.XPATH , '//span[text()="查询"]/..' )
    add_btn = (By.XPATH, '//span[contains(text(),"新增")]')
    reset_btn = (By.XPATH, '//span[text()="重置"]')
    open_btn = (By.XPATH, '//*[@id="main"]/div/div/div/div[1]/div[1]/form/div/div/button[3]/span')
    See_btn = (By.XPATH, '//tbody/tr[1]/td[6]/div/button[1]')
    modify_btn = (By.XPATH, '//tbody/tr[1]/td[6]/div/button[2]')

    def skip(self):
        """跳转到类型管理页面"""
        self.get_text_accurate('渠道资源管理').click()
        self.get_text_accurate('基本信息管理').click()
        self.get_text_accurate('类型管理').click()
        wait(1)

    def click_add_button(self):
        """点击新增按钮"""
        self.b.find_element(*self.add_btn).click()
        wait(1)

    def click_query_button(self):
        """点击查询按钮"""
        self.b.find_element(*self.query_btn).click()
        wait(1)

    def click_reset_button(self):
        """点击重置按钮"""
        self.b.find_element(*self.reset_btn).click()

    def click_open_button(self):
        """点击展开按钮"""
        self.b.find_element(*self.open_btn).click()

    def click_See_button(self):
        """点击查看按钮"""
        self.b.find_elements(*self.See_btn)[1].click()
        wait(2)

    def click_modify_button(self):
        """点击修改按钮"""
        self.b.find_elements(*self.modify_btn)[1].click()
        wait(1)

    def select_goodstype(self, str):
        """选择物品类别"""
        self.option_text('请选择物品类别').click()
        value = self.get_element_by_xpath('//span[text()="%s"]'%str)
        wait(1)
        self.b.execute_script("arguments[0].click()", value)


    def select_goodsname(self, str):
        """选择物品名称"""
        self.option_text('请选择物品名称').click()
        data = self.b.find_elements_by_xpath('//span[contains(text(),"%s")]'%str)
        value = data[0]
        wait(1)
        self.b.execute_script("arguments[0].click()", value)


    def select_goodsstatus(self, str):
        """选择物品状态"""
        self.option_text('请选择物品状态').click()
        if str == u"开":
            self.get_element_by_xpath("//div[@class='el-scrollbar']/div/ul/li/span[text()='开']").click()
        elif str == u"关":
            self.get_element_by_xpath("//div[@class='el-scrollbar']/div/ul/li/span[text()='关']").click()

    def search_info(self,num):
        #验证点击搜索后页面信息
        l = []
        table = self.b.find_elements_by_xpath('''//tr[starts-with(@class,'el-table__row')]''')
        for i in table:
            rv = i.find_elements_by_tag_name('td')
            value = rv[num].text
            if value:
                l.append(value)
        print l
        return l

    def click_operation_button(self):
        #点击状态开关按钮
        button = self.get_element_by_xpath("//tr[@class='el-table__row']/td[5]/div/div/span[2]")
        self.b.execute_script("arguments[0].click()", button)
        wait(1)

    def check_details(self):
        #返回详情信息的值为一个列表
        value = self.b.find_elements_by_xpath('//div[@class="base-info"]//p[@class="content"]')
        l = []
        for i in range(len(value)):
            va= value[i].text
            if va:
                l.append(va)
            else:
                l.append(None)
        print l
        return l

    def check_buttonstatus(self):
        "获取现在开关状态"
        #el为现在状态的元素
        el = self.b.find_elements_by_xpath("//span[contains(@class,'is-active')]")[0]
        print el.text
        return el.text