# coding:utf-8
import os

RECERVIE = [
# 'henglin.wu@genlot.com',
#               'liangzhang.lin@genlot.com',
#               'mingli.li@genlot.com',
#               'ou.gong@genlot.com',
#               'dan.deng@genlot.com',
#               'zhong.zhang@genlot.com'
#               'xiong.wang@genlot.com'
'baoming.zheng@genlot.com'
        ]
#数据库连接
connetion_info = "U_VLT_BMS/123456@10.6.0.202/ORCL"

#站点信息
station_id = '41010101'
#登录用户
username1= u'中心负责人2'
username2= 'chenxiaoming'
tt = os.path.abspath(os.path.join(os.getcwd(), "."))
# download_path=u'C:/Users/Go/Downloads/'
download_path='''C:/Users/Bn/Downloads/'''
# case_path=u'D:/zxl_project/VLT/genlot_vlt_all/cases/'
# html_report=u'D:/zxl_project/VLT/genlot_vlt_all/static/report/'
print(tt)
case_path= tt + '''\\cases\\'''
html_report= tt + '''\\static\\report\\'''

role_number_file=tt + '\\static\\data\\role_number.csv'
game_path=tt + u'D:/game_package/'
upload_path=tt + u'\\static\\upload\\'
plan_number_file=tt + u'\\static\\data\\plan_number.csv'
config_number_file=tt + u'\\static\\data\\config_number.csv'
name_number_file=tt + u'\\static\\data\\game_name_number.csv'
game_name_file=tt + u'\\static\\data\\game_name.csv'