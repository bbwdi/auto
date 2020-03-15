#coding=utf-8
from pages.base_page import BasePage
import time
from common.function import regex,log_info
from db.oracle_db import Oracle
import os
from    pages.home1_page import Home_Page


aa='''渠道业务管理'''#进入渠道业务管理
bb='''渠道列表'''
zhankai='''//*[@id="main"]//button[3]/span[contains(text(),'展开')]'''
input_channel_no='''//*[@id="main"]//input[@placeholder='请输入渠道编号']'''
input_channel_type='''//*[@id="main"]//input[@placeholder='请选择渠道类型']'''
input_channel_level='''//*[@id="main"]//input[@placeholder='请选择渠道等级']'''
input_person ='''//*[@id="main"]//input[@placeholder='请输入负责人']'''
input_phone='''//*[@id="main"]//input[@placeholder='请输入联系电话']'''
input_start_date='''//*[@id="main"]//input[@placeholder='开始日期']'''
input_end_date='''//*[@id="main"]//input[@placeholder='结束日期']'''
click_query_button='''//*[@id="main"]//button[1]/span[text()='查询']'''
click_reset='''//*[@id="main"]//button[2]/span[text()='重置']'''
click_export='''//*[@id="main"]//span[contains(text(),'导出当前')]'''
click_export_all='''//*[@id="main"]//span[contains(text(),'导出全部')]'''
click_view='''(//*[@id="main"]//button/span[text()='查看'])[3]'''
elements_path='''(//*[@id="main"]//table/tbody/tr[1])[1]'''
page_nums='''//*[@id="main"]//span[1][contains(text(),'共 ')]'''
ziyingting_channel_type='''//body//ul//span[text()='自营厅']'''
hezuoting_channel_type='''//body//ul//span[text()='合作厅']'''
yiji_channel_level=u'''//body//ul//span[text()='一级']'''
erji_channel_level=u'''//body//ul//span[text()='二级']'''
sanji_channel_level=u'''//body//ul//span[text()='三级']'''
siji_channel_level=u'''//body//ul//span[text()='四级']'''
path='''/Downloads'''
jibenpath='C:\Users\Bon\Downloads'
filename=u'渠道列表.xls'
base_info=r'''//*[@id="pane-detail"]//div[@class='base-info']/ul/li/p'''#查看页面 第一个基本信息
viewpath='''(//*[@id="main"]//table/tbody/tr[1]/td[2]/div)[1]'''#拿第一条数据的channel no
table_data='''//*[@id="main"]//table/tbody/tr'''

class  jump_channel_list_page(BasePage):
    def jump(self):
        '''跳转到渠道列表'''
        self.get_text_accurate(aa).click()
        self.get_text_accurate(bb).click()
        time.sleep(1)


    def query(self,channer_no='',channel_type='',channel_level='',person='',phone='',startdate='',enddate=''):
        '''查询，不输入参数默认全部'''
        self.get_element_by_xpath(zhankai).click()#点击展开
        self.input_xpath(input_channel_no, channer_no)
        self.channel_type(channel_type)
        self.channel_level(channel_level)
        self.input_xpath(input_person, person)
        self.input_xpath(input_phone, phone)
        self.input_xpath(input_start_date, startdate)
        self.input_xpath(input_end_date, enddate)
        self.get_element_by_xpath(click_query_button).click()
        # self.get_elements_by_xpath(page_data)

    def resetting(self,channer_no='123',channel_type='自营厅',\
                  channel_level='一级',person='人',phone='13570815689',startdate='',enddate=''):
        '''重置，传入各个参数'''
        self.get_element_by_xpath(zhankai).click()  # 点击展开
        self.input_xpath(input_channel_no, channer_no)
        self.channel_type(channel_type)
        self.channel_level(channel_level)
        self.input_xpath(input_person, person)
        self.input_xpath(input_phone, phone)
        self.input_xpath(input_start_date, startdate)
        self.input_xpath(input_end_date, enddate)
        self.get_element_by_xpath(click_reset).click()

    def export(self,channer_no='',channel_type='',channel_level='',person='',phone='',startdate='',enddate=''):
        '''导出当前数据'''
        self.get_element_by_xpath(zhankai).click()  # 点击展开
        self.input_xpath(input_channel_no, channer_no)
        self.channel_type(channel_type)
        self.channel_level(channel_level)
        self.input_xpath(input_person, person)
        self.input_xpath(input_phone, phone)
        self.input_xpath(input_start_date, startdate)
        self.input_xpath(input_end_date, enddate)
        self.get_element_by_xpath(click_reset).click()
        self.get_element_by_xpath(click_export).click()

    def export_all(self,channer_no='',channel_type='',channel_level='',person='',phone='',startdate='',enddate=''):
        '''导出所有数据'''
        self.get_element_by_xpath(zhankai).click()  # 点击展开
        self.input_xpath(input_channel_no, channer_no)
        self.channel_type(channel_type)
        self.channel_level(channel_level)
        self.input_xpath(input_person, person)
        self.input_xpath(input_phone, phone)
        self.input_xpath(input_start_date, startdate)
        self.input_xpath(input_end_date, enddate)
        self.get_element_by_xpath(click_reset).click()
        self.get_element_by_xpath(click_export_all).click()


    def view(self,channer_no='',channel_type='',channel_level='',person='',phone='',startdate='',enddate=''):
        '''查看，输入查询条件，查询后看第一条数据'''
        self.get_element_by_xpath(zhankai).click()  # 点击展开
        self.input_xpath(input_channel_no, channer_no)
        self.channel_type(channel_type)
        self.channel_level(channel_level)
        self.input_xpath(input_person, person)
        self.input_xpath(input_phone, phone)
        self.input_xpath(input_start_date, startdate)
        self.input_xpath(input_end_date, enddate)
        self.get_element_by_xpath(click_query_button).click()
        time.sleep(5)
        self.get_element_by_xpath(click_view).click()
        # self.get_element_by_css('''''').click()

    def elements_path(self):
        '''元素路径'''
        tt=self.get_elements_by_xpath(elements_path)
        return  tt

    def page_num(self):
        '''拿条数'''
        kk=self.get_element_by_xpath(page_nums).text
        log_info(kk)
        tt=regex("\d+",kk)
        log_info(tt)
        return  tt

    def queryresult(self):
        '''根据登陆用户查询渠道数据'''
        ins=self.ins()
        sql = '''SELECT count(*) FROM
        	(SELECT TMP.*,
        	ROWNUM ROW_ID FROM
        	(SELECT
        	aa.channel_no AS channelNo,
        	aa.channel_type AS channelType,
        	bb.ins_name AS insName,
        	ee.ch_level_name AS channelLevelName,
        	cc.account_name AS accountName,
        	cc.phone AS phone,
        	aa.create_time AS createTime 
        FROM
        	t_channel_info aa
        	LEFT JOIN t_ins_info bb ON aa.ins_id = bb.ins_id
        	LEFT JOIN t_channel_fund cc ON aa.channel_id = cc.channel_id
        	LEFT JOIN t_channel_role_info dd ON cc.role_id = dd.id
        	LEFT JOIN t_channel_grade_info ee ON aa.channel_level_id = ee.ch_grade_id 
        WHERE
        	dd.is_manager = 1 
        	AND ( bb.ins_id = %s OR bb.PARENT_ID = %s ) 
        	AND aa.is_his_channel = 0 
        	AND aa.STATUS = 2 
        	AND bb.region_code IN (
        	bb.region_code - MOD ( bb.region_code, 10000 ),
        	bb.region_code - MOD ( bb.region_code, 100 ),
        	bb.region_code - MOD ( bb.region_code, 1 ),
        	1 ) 
        ORDER BY
        	aa.create_time DESC ) TMP )''' % (ins, ins)
        tt=Oracle()
        kk=tt.run_sql_dir(sql)
        kk1=kk[0]#
        kk2=list(kk1)
        return kk2


    def channel_type(self,type1):
        '''渠道类型，根据输入值，选择相应的下拉框选项'''
        time.sleep(2)
        if type1 == u"自营厅":
            self.input_xpath_ComboBox(input_channel_type, type1)
            self.get_element_by_xpath(ziyingting_channel_type).click()
        elif type1 == u"合作厅":
            self.input_xpath_ComboBox(input_channel_type, type1)
            self.get_element_by_xpath(hezuoting_channel_type).click()
        else:
            self.input_xpath(input_channel_type, type1)

    def channel_level(self,level):
        '''渠道级别，根据输入值，选择相应的下拉框选项'''
        if level == u"一级":
            self.input_xpath_ComboBox(input_channel_level, level)
            self.get_element_by_xpath(yiji_channel_level).click()
        elif level == u"二级":
            self.input_xpath_ComboBox(input_channel_level, level)
            self.get_element_by_xpath(erji_channel_level).click()
        elif level == u"三级":
            self.input_xpath_ComboBox(input_channel_level, level)
            self.get_element_by_xpath(sanji_channel_level).click()
        elif level == u"四级":
            self.input_xpath_ComboBox(input_channel_level, level)
            self.get_element_by_xpath(siji_channel_level).click()
        else:
            self.input_xpath_ComboBox(input_channel_level, level)

    def channel_no_isnull(self):
        '''渠道编号框中的值'''
        tt=self.get_element_by_xpath(input_channel_no).text
        return tt
    def channel_type_isnull(self):
        '''渠道类型框中的值'''
        tt=self.get_element_by_xpath(input_channel_type).text
        return  tt
    def channel_level_isnull(self):
        '''渠道级别框中的值'''
        tt=self.get_element_by_xpath(input_channel_level).text
        return  tt
    def person_isnull(self):
        '''责任人框中的值'''
        tt=self.get_element_by_xpath(input_person ).text
        return tt
    def phone_isnull(self):
        '''手机号码框中的值'''
        tt=self.get_element_by_xpath(input_phone ).text
        return tt
    def start_date_isnull(self):
        '''开始时间框中的值'''
        tt=self.get_element_by_xpath(input_start_date).text
        return tt
    def end_date_isnull(self):
        '''结束时间框中的值'''
        tt=self.get_element_by_xpath(input_end_date).text
        return tt

    def export_check(self):
        '''导出校验'''
        t=self.export_file(jibenpath,filename)
        return t

    def channel_data(self,channel_no=''):
        '''渠道详情'''
        if channel_no=='':
            kk=self.page_num()
        else:
            kk=channel_no
        if int(kk)>0:
            tt=self.get_element_by_xpath(viewpath).text
            return tt
        else:
            a=0
            return a

    def querydetail(self,channel_no=''):
        '''查询详情中内容'''
        # tt=self.channel_data()
        if channel_no=='':
            tt=self.channel_data()
        else:
            tt=channel_no
        if int(tt)>0:
            sql = '''SELECT        t.ins_name AS insName,
            	case 
						WHEN	d.channel_type=0 then '自营厅'
						WHEN	d.channel_type=1 then '合作厅'
						else NULL
						  END,
            	( SELECT tcgi.ch_level_name FROM t_channel_grade_info tcgi WHERE tcgi.ch_grade_id = d.channel_level_id ) channelLevelName,d.channel_no AS channelNo,
							case 
						WHEN	a.RUN_FIELD=0 then '自有'
						WHEN	a.RUN_FIELD=1 then '租用'
						else NULL
						  END,a.POINT_AREA,
							d.channel_address AS channelAddress,
							d.longitude,
            	d.latitude,
							d.buy_card_limit buyCardLimit,
            	d.try_card_limit tryCardLimit,
							d.recharge_count rechargeCount,
							d.CHANNEL_LIMIT
							
            FROM
            	t_channel_info d
            	LEFT JOIN t_partner c ON d.partner_id = c.id
            	INNER JOIN t_ins_info t ON d.ins_id = t.ins_id
							LEFT JOIN T_FINANCE_INFO a on a.channel_id=d.channel_id
            WHERE d.channel_no = '%s'  '''%tt

            t = Oracle()
            kk = t.run_sql_dir(sql)
            log_info(kk)
            return kk
        else:
            a=0
            return a



    def view_channel(self):
        '''渠道详情中的基本信息'''
        aa = self.page_num()
        kk=self.channel_data()
        time.sleep(2)
        if  int(aa)>0:
            self.view(channer_no=kk)
            tt=[]
            for i in range(1,20):
                base_info1 = '('+ base_info + ')'+'[%d]'%i
                jieguo=self.get_element_by_xpath(base_info1).text

                if i==6:
                    jieguo=regex(('\d+'),jieguo)
                elif i==10:
                    jieguo = regex(('\d+'), jieguo)
                elif i==11:
                    jieguo = regex(('\d+'), jieguo)
                elif i==12:
                    jieguo = regex(('\d+'), jieguo)
                else:
                    pass
                print '%d' % i + jieguo
                tt.append(jieguo)
            log_info(tt)
            return tt
        else:
            a=0
            return a

    def pageresult1(self):
        '''渠道列表中表单数据'''
        aa = self.page_num()
        kk=self.get_element_by_xpath(viewpath).text#拿第一行的channel no
        time.sleep(2)
        if int(aa) > 0:
            tt = []

            table_data1 = '(' + table_data + ')' + '[1]'
            jieguo = self.get_element_by_xpath(table_data1).text
            tt.append(jieguo)
            log_info(tt)
            return tt
        else:
            a = 0
            return a

    def sql_page_result(self):
        kk=self.get_element_by_xpath(viewpath).text #拿第一行的channel no
        sql='''SELECT       d.channel_no AS channelNo, 
            	case 
						WHEN	d.channel_type=0 then '自营厅'
						WHEN	d.channel_type=1 then '合作厅'
						else NULL
						  END,
							t.ins_name AS insName,( SELECT tcgi.ch_level_name FROM t_channel_grade_info tcgi WHERE tcgi.ch_grade_id = d.channel_level_id ) 	channelLevelName,
            	dd.account_name,dd.phone
            FROM
            	t_channel_info d
            	LEFT JOIN t_partner c ON d.partner_id = c.id
            	INNER JOIN t_ins_info t ON d.ins_id = t.ins_id
							LEFT JOIN T_FINANCE_INFO a on a.channel_id=d.channel_id
							LEFT JOIN T_CHANNEL_FUND dd on dd.channel_id=d.channel_id
            WHERE d.channel_no =%s'''%kk

        yy=self.sql_result(sql)
        return  yy

