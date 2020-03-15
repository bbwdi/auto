# coding=utf-8
import unittest, random
from common.login_b import Login_B
from pages.home1_page import Home_Page
from pages.Business_management.Basic_Infomanagement.Model_Management import model_page
from pages.Business_management.Basic_Infomanagement.AddModel_Page import addmodel_page
from pages.Business_management.Basic_Infomanagement.Modifymodel_Page import modifymodel_page
from common.function import wait, log_info, GetDataFile_P,get_current_dir

path3 = get_current_dir()+'\\pages\\Business_management\\Basic_Infomanagement\\upload\\uploadFile.exe'
path4 = get_current_dir()+'\\pages\\Business_management\\Basic_Infomanagement\\upload\\uploadFile2.exe'
addmodel_path = get_current_dir()+'\\static\\data\\addmodel.yaml'
modifymodel_path = get_current_dir()+'\\static\\data\\modifymodel.yaml'

class basic_type(unittest.TestCase):
    def setUp(self):
        # 进入类型管理
        b = Login_B()
        obj = Home_Page(b)
        obj.jumpBusinessmanagement()
        self.obb = model_page(b)
        self.oba = addmodel_page(b)
        self.obc = modifymodel_page(b)
        self.obb.skip()
        self.status = {"开": 1, "关": 2}  # 状态

    def test_addbutton_success(self):
        """新增按钮成功跳转"""
        self.obb.click_add_button()
        msg = self.oba.check_addmsg()
        self.assertEqual(u'新增型号管理', msg)

    def test_addtermodel_success(self):
        """新增设备型号成功"""
        f = GetDataFile_P(addmodel_path)
        lst = f['test_addtermodel_success_01']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        lst[1] = self.oba.select_terminalname(lst[1])
        lst[2] = lst[2] + str(random.randint(0, 10000))
        self.oba.input_termodel(lst[2])
        self.oba.input_terPrice(lst[3])
        self.oba.input_Supplier(lst[4])
        self.oba.input_factory(lst[5])
        self.oba.input_Remarks(lst[6])
        self.oba.upload_picture(path3)
        self.oba.click_keep_button()
        sql = "select a.GOODS_TYPE,a.GOODS_NAME,b.DEVICE_MODEL,(b.UNIT_PRICE/100),b.PROVIDER,b.MANUFACTOR_INFO,b.REMARK,b.FILES" \
              " from T_GOODS_TYPE a join T_GOODS_MODEL b on a.id = b.GOODS_ID where a.goods_name = '%s' and b.DEVICE_MODEL = '%s'" % (lst[1],lst[2])
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res) - 1):
            if i != 3:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))
        # 验证图片是否修改
        # self.assertIn(u'f_center_03', res[-1])

    def test_addpartsmodel_success(self):
        """新增配件型号成功"""
        f = GetDataFile_P(addmodel_path)
        lst = f['test_addpartsmodel_success_02']
        self.obb.click_add_button()
        self.oba.select_goodstype(lst[0])
        lst[1] = self.oba.select_partsname(lst[1])
        lst[2] = lst[2] + str(random.randint(0, 10000))
        self.oba.input_partsmodel(lst[2])
        self.oba.input_partsPrice(lst[3])
        self.oba.input_Supplier(lst[4])
        self.oba.input_factory(lst[5])
        self.oba.input_Remarks(lst[6])
        self.oba.select_terminal(lst[7])
        self.oba.upload_picture(path3)
        self.oba.click_keep_button()
        sql = "select a.GOODS_TYPE,a.GOODS_NAME,b.DEVICE_MODEL,(b.UNIT_PRICE/100),b.PROVIDER,b.MANUFACTOR_INFO,b.REMARK,b.FILES" \
              " from T_GOODS_TYPE a join T_GOODS_MODEL b on a.id = b.GOODS_ID where a.goods_name = '%s' and b.DEVICE_MODEL = '%s'" % (lst[1],lst[2])
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res) - 1):
            if i != 3:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))
        # 验证图片是否一致
        # self.assertIn(u'f_center_03', res[-1])

    def test_modifystatus_close(self):
        """修改状态为关闭"""
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(u'自动化设备')
        mo = self.obb.select_goodsmodel()
        self.obb.select_goodsstatus(u'开')
        self.obb.click_query_button()
        self.obb.click_operation_button()
        sql = "select status from t_goods_model where  DEVICE_MODEL = '%s'"%mo
        result = self.obb.check_database(sql)
        self.assertEqual(self.status['关'], result[0])

    def test_modifystatus_open(self):
        """修改状态为打开"""
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(u'自动化设备')
        mo = self.obb.select_goodsmodel()
        self.obb.select_goodsstatus(u'关')
        self.obb.click_query_button()
        self.obb.click_operation_button()
        sql = "select status from t_goods_model where  DEVICE_MODEL = '%s'"%mo
        result = self.obb.check_database(sql)
        self.assertEqual(self.status['开'], result[0])

    def test_check_terminalinfo(self):
        """检查设备查看详情"""
        # 查出型号管理设备查看信息
        sql = """select d.* from (select a.GOODS_NAME,a.DEVICE_UNIT,case when a.IS_STANDARD =1 then '是' when a.IS_STANDARD =2 
        then '否' ELSE NULL end case,case when a.IS_RECOVERY =1 then '是' when a.IS_RECOVERY =2 then '否' ELSE NULL 
        end case2,a.REMARK as remake1,b.DEVICE_MODEL,(b.UNIT_PRICE/100),b.PROVIDER,b.MANUFACTOR_INFO,b.REMARK,b.FILES 
        from T_GOODS_TYPE a join T_GOODS_MODEL b on a.id = b.GOODS_ID where a.goods_type = 1 order by b.CREATE_TIME desc)d 
        where rownum =1"""
        result = self.obb.check_database(sql)
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(result[0])
        self.obb.select_goodsmodel(result[5])
        self.obb.click_query_button()
        self.obb.click_See_button()
        info = self.obb.check_details()
        img = self.obb.Return_img()
        # 对比数据库和页面的数据
        for i in range (len(info)):
            if i !=6:
                self.assertEqual(result[i], info[i])
            else:
                self.assertEqual(str(result[i]), info[i])
        #验证对比图片
        # for i in  img:
        #     self.assertIn(i,result[-1])

    def test_check_partsinfo(self):
        """检查配件查看详情"""
        # 查出型号管理设备查看信息
        sql = """select d.* from (select a.GOODS_NAME,a.DEVICE_UNIT,case when a.IS_RECOVERY =1 then '是' when a.IS_RECOVERY =2 then '否' ELSE NULL 
        end case2,a.REMARK as remake1,b.DEVICE_MODEL,(b.UNIT_PRICE/100),b.PROVIDER,b.MANUFACTOR_INFO,b.REMARK,b.FILES 
        from T_GOODS_TYPE a join T_GOODS_MODEL b on a.id = b.GOODS_ID where a.goods_type = 2 order by b.CREATE_TIME desc)d 
        where rownum =1"""
        result = self.obb.check_database(sql)
        sql2 = """select to_char(rownum),d.GOODS_NAME,c.DEVICE_MODEL,to_char(a.CREATE_TIME ,'yyyy-mm-dd hh24:mi:ss'),b.USER_NAME from T_MODEL_AVAILABLE a 
        left join T_USER_INFO b on b.user_id = a.create_by left join T_GOODS_MODEL c on a.MODEL_ID = c.id 
        left join T_GOODS_TYPE d on c.GOODS_ID = d.id where a.parts_id = (select id from T_GOODS_MODEL  
        where  DEVICE_MODEL = '%s')"""%result[4]
        result2 = self.obb.check_database(sql2)
        self.obb.select_goodstype(u'配件')
        self.obb.select_goodsname(result[0])
        self.obb.select_goodsmodel(result[4])
        self.obb.click_query_button()
        self.obb.click_See_button()
        info = self.obb.check_details()
        # 对比数据库和页面的数据
        for i in range (len(info)):
            if i !=5:
                self.assertEqual(result[i], info[i])
            else:
                self.assertEqual(str(result[i]), info[i])
        #验证对比图片
        # try:
        #     img = self.obb.Return_img()
        #     for i in img:
        #         self.assertIn(i,result[-1])
        # except BaseException as E:
        #     print E
        #验证机型信息
        p =self.obb.search_info()
        self.assertListEqual(result2,p)


    def test_modifyterminal(self):
        """修改设备型号页面"""
        f = GetDataFile_P(modifymodel_path)
        lst = f['test_modifyterminal_success_01']
        self.obb.select_goodstype(u'设备')
        self.obb.select_goodsname(u'自动化设备')
        self.obb.click_query_button()
        bu = self.obb.check_buttonstatus()
        if bu == '开':
            self.obb.click_operation_button()
        self.obb.click_modify_button()
        lst[0] = self.obc.select_terminalname(lst[0])
        lst[1] = lst[1]+str(random.randint(10,10000))
        self.obc.input_termodel(lst[1])
        self.obc.input_terPrice(lst[2])
        self.obc.input_Supplier(lst[3])
        self.obc.input_factory(lst[4])
        self.obc.delete_picture()
        self.obc.upload_picture(path4)
        self.obc.input_Remarks(lst[5])
        self.obc.click_keep_button()
        sql = "select a.GOODS_NAME,b.DEVICE_MODEL,(b.UNIT_PRICE/100),b.PROVIDER,b.MANUFACTOR_INFO,b.REMARK,b.FILES" \
              " from T_GOODS_TYPE a join T_GOODS_MODEL b on a.id = b.GOODS_ID where a.goods_name = '%s' and b.DEVICE_MODEL = '%s'" % (lst[0],lst[1])
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res) - 1):
            if i != 2:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))
        # 验证图片是否修改
        # self.assertIn(u'dog', res[-1])

    def test_modifyparts(self):
        """修改配件型号页面"""
        f = GetDataFile_P(modifymodel_path)
        lst = f['test_modifyparts_success_02']
        self.obb.select_goodstype(u'配件')
        self.obb.select_goodsname(u'自动化配件')
        self.obb.click_query_button()
        bu = self.obb.check_buttonstatus()
        if bu == '开':
            self.obb.click_operation_button()
        self.obb.click_modify_button()
        lst[0] = self.obc.select_partsname(lst[0])
        lst[1] = lst[1]+str(random.randint(10,10000))
        self.obc.input_partsmodel(lst[1])
        self.obc.input_partsPrice(lst[2])
        self.obc.input_Supplier(lst[3])
        self.obc.click_del_button()
        self.obc.click_add_button()
        #tern,term为新增的机型设备名称和型号
        tername ,termodel = self.obc.select_terminal(lst[6])
        self.obc.delete_picture()
        self.obc.upload_picture(path4)
        self.obc.input_factory(lst[4])
        self.obc.input_Remarks(lst[5])
        self.obc.click_keep_button()
        sql = "select a.GOODS_NAME,b.DEVICE_MODEL,(b.UNIT_PRICE/100),b.PROVIDER,b.MANUFACTOR_INFO,b.REMARK,b.FILES" \
              " from T_GOODS_TYPE a join T_GOODS_MODEL b on a.id = b.GOODS_ID where a.goods_name = '%s' and b.DEVICE_MODEL = '%s'" % (lst[0],lst[1])
        res = self.oba.check_database(sql)
        # 断言数据库保存数据是否正确
        for i in range(len(res) - 1):
            if i != 2:
                self.assertEqual(lst[i], res[i])
            else:
                self.assertEqual(lst[i], str(res[i]))
        # 验证图片是否修改
        # self.assertIn(u'dog', res[-1])
        #对比数据库验证新增可用机型
        sql2 = """select d.GOODS_NAME,c.DEVICE_MODEL from T_MODEL_AVAILABLE a 
        left join T_USER_INFO b on b.user_id = a.create_by left join T_GOODS_MODEL c on a.MODEL_ID = c.id 
        left join T_GOODS_TYPE d on c.GOODS_ID = d.id where a.parts_id = (select id from T_GOODS_MODEL  
        where  DEVICE_MODEL = '%s')"""%lst[1]
        #查询到新增的机型设备名称和型号
        result2 = self.obc.check_database(sql2)
        self.assertIn(tername,result2)
        self.assertIn(termodel, result2)


    def tearDown(self):
        wait(2)
        self.obb.close_browser()


if __name__ == '__main__':
    unittest.main(verbosity=2)