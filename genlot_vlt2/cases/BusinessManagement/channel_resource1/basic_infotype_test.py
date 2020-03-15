#coding=utf-8
import unittest,random
from common.login_b import Login_B
from pages.home1_page import Home_Page
from pages.Business_management.Basic_Infomanagement.Type_Management import type_page
from pages.Business_management.Basic_Infomanagement.AddType_Page import addtype_page
from pages.Business_management.Basic_Infomanagement.Modifytype_Page import modifytype_page
from common.function import wait,log_info,GetDataFile_P,get_current_dir

path = get_current_dir()+'\\pages\\Business_management\\Basic_Infomanagement\\upload\\uploadFile.exe'
path1 = get_current_dir()+'\\pages\\Business_management\\Basic_Infomanagement\\upload\\uploadFile2.exe'
add_path = get_current_dir()+'\\static\\data\\addtype.yaml'
modify_path = get_current_dir()+'\\static\\data\\modifytype.yaml'

class basic_type(unittest.TestCase):
    def setUp(self):
        #进入类型管理
        b = Login_B()
        obj = Home_Page(b)
        obj.jumpBusinessmanagement()
        self.obb = type_page(b)
        self.oba = addtype_page(b)
        self.obc = modifytype_page(b)
        self.obb.skip()
        self.status = {"开":1, "关":2}  #状态


    def test_addbutton_success(self):
        """新增按钮成功跳转"""
        self.obb.click_add_button()
        msg = self.oba.check_addmsg()
        self.assertEqual(u'新增类型管理',msg)

    def test_addterminal_success(self):
        """新增其他设备成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addterminal_success_01']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        self.oba.select_terminaltype(lst[1])
        lst[2] = lst[2]+str(random.randint(0,10000))
        self.oba.input_tername(lst[2])
        self.oba.input_terunit(lst[3])
        self.oba.select_standard(lst[4])
        self.oba.select_recycled(lst[5])
        self.oba.input_Remarks(lst[6])
        self.oba.click_keep_button()
        sql = "select goods_type,device_type,goods_name,device_unit,IS_STANDARD,IS_RECOVERY,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[2]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            self.assertEqual(lst[i], res[i])

    @unittest.skip('跳过测试')
    def test_addter1_success(self):
        """新增终端机成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addter1_success_05']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        self.oba.select_terminaltype(lst[1])
        self.oba.input_terunit(lst[3])
        self.oba.select_standard(lst[4])
        self.oba.select_recycled(lst[5])
        self.oba.input_Remarks(lst[6])
        self.oba.click_keep_button()
        sql = "select goods_type,device_type,goods_name,device_unit,IS_STANDARD,IS_RECOVERY,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[2]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            self.assertEqual(lst[i], res[i])

    @unittest.skip('跳过测试')
    def test_addter2_success(self):
        """新增柜员机成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addter2_success_06']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        self.oba.select_terminaltype(lst[1])
        self.oba.input_terunit(lst[3])
        self.oba.select_standard(lst[4])
        self.oba.select_recycled(lst[5])
        self.oba.input_Remarks(lst[6])
        self.oba.click_keep_button()
        sql = "select goods_type,device_type,goods_name,device_unit,IS_STANDARD,IS_RECOVERY,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[2]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            self.assertEqual(lst[i], res[i])


    def test_addparts_success(self):
        """新增配件成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addparts_success_02']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        lst[1] = lst[1]+str(random.randint(0,10000))
        self.oba.input_partsname(lst[1])
        self.oba.input_partsunit(lst[2])
        self.oba.select_recycled(lst[3])
        self.oba.input_Remarks(lst[4])
        self.oba.click_keep_button()
        sql = "select goods_type,goods_name,device_unit,IS_RECOVERY,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[1]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            self.assertEqual(lst[i], res[i])


    def test_addConsumables_success(self):
        """新增其他耗材成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addConsumables_success_03']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        self.oba.select_Consumablestype(lst[1])
        lst[2] = lst[2]+str(random.randint(0,10000))
        self.oba.input_Consumablesname(lst[2])
        self.oba.input_Consumablesnum(lst[3])
        self.oba.input_ConsumablesunitPrice(lst[4])
        self.oba.input_Consumablesunit(lst[5])
        self.oba.input_Supplier(lst[6])
        self.oba.input_factory(lst[7])
        self.oba.input_Remarks(lst[8])
        self.oba.upload_picture(path)
        self.oba.click_keep_button()
        sql = "select goods_type,CONSUMABLES_TYPE,goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[2]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            if i !=4:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))

    @unittest.skip('跳过测试')
    def test_addBettingcard_success(self):
        """新增投注卡耗材成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addBettingcard_success_07']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        self.oba.select_Consumablestype(lst[1])
        self.oba.input_Consumablesnum(lst[3])
        self.oba.input_ConsumablesunitPrice(lst[4])
        self.oba.input_Consumablesunit(lst[5])
        self.oba.input_Supplier(lst[6])
        self.oba.input_factory(lst[7])
        self.oba.input_Remarks(lst[8])
        self.oba.upload_picture(path)
        self.oba.click_keep_button()
        sql = "select goods_type,CONSUMABLES_TYPE,goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[2]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            if i !=4:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))


    def test_addfacilities_success(self):
        """新增设施成功"""
        f = GetDataFile_P(add_path)
        lst = f['test_addfacilities_success_04']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        lst[1] = lst[1]+str(random.randint(0,10000))
        self.oba.input_facilitiesname(lst[1])
        self.oba.input_facilitiesnum(lst[2])
        self.oba.input_facilitiesunitPrice(lst[3])
        self.oba.input_facilitiesunit(lst[4])
        self.oba.input_Supplier(lst[5])
        self.oba.input_factory(lst[6])
        self.oba.input_Remarks(lst[7])
        self.oba.upload_picture(path)
        self.oba.click_keep_button()
        sql = "select goods_type,goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'"%lst[1]
        res = self.oba.check_database(sql)
        #断言数据库保存数据是否正确
        for i in range(len(res)):
            if i !=3:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))


    def test_modifystatus_close(self):
        """修改状态为关闭"""
        self.obb.click_open_button()
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(u'终端机')
        self.obb.select_goodsstatus(u'开')
        self.obb.click_query_button()
        self.obb.click_operation_button()
        sql = "select status from t_goods_type where goods_type = 1 and goods_name = '终端机'"
        result = self.obb.check_database(sql)
        self.assertEqual(self.status['关'],result[0])


    def test_modifystatus_open(self):
        """修改状态为打开"""
        self.obb.click_open_button()
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(u'终端机')
        self.obb.select_goodsstatus(u'关')
        self.obb.click_query_button()
        self.obb.click_operation_button()
        sql = "select status from t_goods_type where goods_type = 1 and goods_name = '终端机'"
        result = self.obb.check_database(sql)
        self.assertEqual(self.status['开'],result[0])


    def test_check_terminalinfo(self):
        """检查设备查看详情"""
        #查出最近创建的设备记录的名称、单位、是否标配、是否回收、备注
        sql = """SELECT a.* FROM (SELECT goods_name,device_unit,
CASE
	
	WHEN IS_STANDARD = 1 THEN
	'是' 
	WHEN IS_STANDARD = 2 THEN
	'否' ELSE NULL 
	END CASE,
CASE
	
	WHEN IS_RECOVERY = 1 THEN
	'是' 
	WHEN IS_RECOVERY = 2 THEN
	'否' ELSE NULL 
	END CASE1,
	REMARK FROM T_GOODS_TYPE WHERE goods_type = 1 ORDER BY create_time ) a WHERE ROWNUM =1"""
        result = self.obb.check_database(sql)
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(result[0])
        self.obb.click_query_button()
        self.obb.click_See_button()
        info = self.obb.check_details()
        #对比数据库和页面的数据
        self.assertListEqual(result,info)


    def test_check_partsinfo(self):
        """检查配件查看详情"""
        # 查出最近创建的配件记录的名称、单位、是否回收、备注
        sql = """SELECT a.* FROM (SELECT goods_name,device_unit,
CASE

    WHEN IS_RECOVERY = 1 THEN
    '是' 
    WHEN IS_RECOVERY = 2 THEN
    '否' ELSE NULL 
    END CASE1,
    REMARK FROM T_GOODS_TYPE WHERE goods_type = 2 ORDER BY create_time ) a WHERE ROWNUM =1"""
        result = self.obb.check_database(sql)
        self.obb.select_goodstype(u'配件')
        self.obb.select_goodsname(result[0])
        self.obb.click_query_button()
        self.obb.click_See_button()
        info = self.obb.check_details()
        # 对比数据库和页面的数据
        for i in range(len(info)):
            self.assertEqual(result[i],info[i])


    def test_check_haocaiinfo(self):
        """检查耗材查看详情"""
        # 查出最近创建的耗材记录的名称、编号、单价、单位、供应商、备注
        sql = """SELECT a.* FROM (SELECT goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK
         FROM T_GOODS_TYPE WHERE goods_type = 3 ORDER BY create_time ) a WHERE ROWNUM =1"""
        result = self.obb.check_database(sql)
        self.obb.select_goodstype(u'耗材')
        self.obb.select_goodsname(result[0])
        self.obb.click_query_button()
        self.obb.click_See_button()
        info = self.obb.check_details()
        # 对比数据库和页面的数据
        for i in range(len(info)):
            if i !=2:
                self.assertEqual(result[i], info[i])
            else:
                self.assertEqual(str(result[i]), info[i])


    def test_check_sheshiinfo(self):
        """检查设施查看详情"""
        # 查出最近创建的设施记录的名称、编号、单价、单位、供应商、备注
        sql = """SELECT a.* FROM (SELECT goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK
         FROM T_GOODS_TYPE WHERE goods_type = 4 ORDER BY create_time ) a WHERE ROWNUM =1"""
        result = self.obb.check_database(sql)
        self.obb.select_goodstype(u'设施')
        self.obb.select_goodsname(result[0])
        self.obb.click_query_button()
        self.obb.click_See_button()
        info = self.obb.check_details()
        # 对比数据库和页面的数据
        for i in range(len(info)):
            if i !=2:
                self.assertEqual(result[i], info[i])
            else:
                self.assertEqual(str(result[i]), info[i])


    def test_modifyterminal(self):
        """修改设备页面"""
        f = GetDataFile_P(modify_path)
        lst = f['test_modifyterminal_success_01']
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(u'自动化设备')
        self.obb.click_query_button()
        bu = self.obb.check_buttonstatus()
        if bu == '开':
            self.obb.click_operation_button()
        self.obb.click_modify_button()
        lst[1] = lst[1]+str(random.randint(0,10000))
        self.obc.input_tername(lst[1])
        self.obc.input_terunit(lst[2])
        self.obc.select_standard(lst[3])
        self.obc.select_recycled(lst[4])
        self.obc.input_Remarks(lst[5])
        self.obc.click_keep_button()
        sql = "select device_type,goods_name,device_unit,IS_STANDARD,IS_RECOVERY,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'" % lst[1]
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res)):
            self.assertEqual(lst[i], res[i])


    def test_modifyparts(self):
        """修改配件页面"""
        f = GetDataFile_P(modify_path)
        lst = f['test_modifyparts_success_02']
        self.obb.select_goodstype(u'配件')
        self.obb.select_goodsname(u'自动化配件')
        self.obb.click_query_button()
        bu = self.obb.check_buttonstatus()
        if bu == '开':
            self.obb.click_operation_button()
        self.obb.click_modify_button()
        lst[1] = lst[1]+str(random.randint(0,10000))
        self.obc.input_partsname(lst[1])
        self.obc.input_partsunit(lst[2])
        self.obc.select_recycled(lst[3])
        self.obc.input_Remarks(lst[4])
        self.obc.click_keep_button()
        sql = "select goods_type,goods_name,device_unit,IS_RECOVERY,REMARK " \
              "from T_GOODS_TYPE where goods_name = '%s'" % lst[1]
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res)):
            self.assertEqual(lst[i], res[i])


    def test_modifyhaocai(self):
        """修改耗材页面"""
        f = GetDataFile_P(modify_path)
        lst = f['test_modifyConsumables_success_03']
        self.obb.select_goodstype(u'耗材')
        self.obb.select_goodsname(u'自动化耗材')
        self.obb.click_query_button()
        bu = self.obb.check_buttonstatus()
        if bu == '开':
            self.obb.click_operation_button()
        self.obb.click_modify_button()
        lst[1] = lst[1] + str(random.randint(0, 10000))
        self.obc.input_Consumablesname(lst[1])
        self.obc.input_Consumablesnum(lst[2])
        self.obc.input_ConsumablesunitPrice(lst[3])
        self.obc.input_Consumablesunit(lst[4])
        self.obc.input_Supplier(lst[5])
        self.obc.input_factory(lst[6])
        self.obc.input_Remarks(lst[7])
        self.obc.delete_picture()
        self.obc.upload_picture(path1)
        self.oba.click_keep_button()
        sql = "select CONSUMABLES_TYPE,goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK,FILES " \
              "from T_GOODS_TYPE where goods_name = '%s'" % lst[1]
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res)-1):
            if i != 3:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))
        #验证图片是否修改
        # self.assertIn('dog',res[-1])

    def test_modifysheshi(self):
        """修改设施页面"""
        f = GetDataFile_P(modify_path)
        lst = f['test_modifyfacilities_success_04']
        self.obb.select_goodstype(u'设施')
        self.obb.select_goodsname(u'自动化设施')
        self.obb.click_query_button()
        bu = self.obb.check_buttonstatus()
        if bu == '开':
            self.obb.click_operation_button()
        self.obb.click_modify_button()
        lst[1] = lst[1] + str(random.randint(0, 10000))
        self.obc.input_facilitiesname(lst[1])
        self.obc.input_facilitiesnum(lst[2])
        self.obc.input_facilitiesunitPrice(lst[3])
        self.obc.input_facilitiesunit(lst[4])
        self.obc.input_Supplier(lst[5])
        self.obc.input_factory(lst[6])
        self.obc.input_Remarks(lst[7])
        self.obc.delete_picture()
        self.obc.upload_picture(path1)
        self.oba.click_keep_button()
        sql = "select goods_type,goods_name,CODE,(UNIT_PRICE/100),device_unit,PROVIDER,MANUFACTOR_INFO,REMARK,FILES " \
              "from T_GOODS_TYPE where goods_name = '%s'" % lst[1]
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res)-1):
            if i != 3:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))
        #验证图片是否修改
        # self.assertIn(u'dog',res[-1])



    def tearDown(self):
        wait(2)
        self.obb.close_browser()

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main()