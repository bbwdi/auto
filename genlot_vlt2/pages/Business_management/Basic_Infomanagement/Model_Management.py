#coding=utf-8
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from common.function import wait,log_info


class model_page(BasePage):
    """类型管理页面"""

    query_btn = (By.XPATH , '//span[text()="查询"]/..' )
    add_btn = (By.ID, 'modelManage-add')
    reset_btn = (By.XPATH, '//span[text()="重置"]')
    See_btn = (By.XPATH, '//tbody/tr[1]/td[6]/div/button[1]')
    modify_btn = (By.XPATH, '//tbody/tr[1]/td[6]/div/button[2]')

    def skip(self):
        """跳转到型号管理页面"""
        self.get_text_accurate('渠道资源管理').click()
        self.get_text_accurate('基本信息管理').click()
        self.get_text_accurate('型号管理').click()
        wait(1)

    def click_add_button(self):
        """点击新增按钮"""
        self.b.find_element(*self.add_btn).click()
        wait(2)

    def click_query_button(self):
        """点击查询按钮"""
        self.b.find_element(*self.query_btn).click()
        wait(2)

    def click_reset_button(self):
        """点击重置按钮"""
        self.b.find_element(*self.reset_btn).click()


    def click_See_button(self):
        """点击查看按钮"""
        self.b.find_elements(*self.See_btn)[1].click()
        wait(1)

    def click_modify_button(self):
        """点击修改按钮"""
        self.b.find_elements(*self.modify_btn)[1].click()
        wait(1)

    def select_goodstype(self, str):
        """选择物品类别"""
        self.option_text('请选择物品类别').click()
        value = self.get_element_by_xpath('//span[text()="%s"]'%str)
        self.b.execute_script("arguments[0].click()", value)
        wait(1)


    def select_goodsname(self, str):
        """选择物品名称"""
        self.option_text('请选择物品名称').click()
        data = self.b.find_elements_by_xpath('//span[contains(text(),"%s")]'%str)
        value = data[0]
        self.b.execute_script("arguments[0].click()", value)
        wait(1)

    def select_goodsmodel(self,str=None):
        """选择物品型号"""
        self.option_text('请选择物品型号').click()
        if str:
            data = self.get_element_by_xpath('//span[text()="%s"]'%str)
        else:
            data = self.b.find_elements_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]")[4]
        text = data.text
        self.b.execute_script("arguments[0].click()", data)
        wait(1)
        print text
        return text

    def select_goodsstatus(self, str):
        """选择物品状态"""
        self.option_text('请选择物品状态').click()
        if str == u"开":
            self.get_element_by_xpath("//div[@class='el-scrollbar']/div/ul/li/span[text()='开']").click()
        elif str == u"关":
            self.get_element_by_xpath("//div[@class='el-scrollbar']/div/ul/li/span[text()='关']").click()

    def search_info(self):
        #验证点击搜索后页面信息
        l = []
        table = self.b.find_elements_by_xpath('''//tr[starts-with(@class,'el-table__row')]''')
        for i in table:
            rv = i.find_elements_by_tag_name('td')
            for j in rv:
                value = j.text
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

    def Return_img(self):
        """返回图片元素的地址"""
        el = self.b.find_elements_by_xpath("//div[@class='el-image image']/img")
        l = []
        for i in range(len(el)):
            l.append(el[i].get_attribute("src"))
        return l