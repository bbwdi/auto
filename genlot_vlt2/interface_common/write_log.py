#coding=utf-8
import  logging
import xlwt
import xlrd
from xlutils.copy import copy
import time

def saveToLogFile(filename,filemode):
    logging.basicConfig(level=logging.WARN,#日志级别
                        filename = '%s'%filename, #保存文件路径
                        filemode = '%s'%filemode,#保存方式，有 w 和 a 模式，默认不写为追加 a 模式
                        # format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' #日志格式
                        format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式

    )
    # logging.info('info级别，正常输出信息，一般用来打印一些正常的操作')


# def wirte_excel(round,levle,span,cashamount,diamond,bonus,gamebonus):
def wirte_excel(a):
    # 创建一个workbook 设置编码
    # workbook = xlwt.Workbook(encoding='utf-8')
    # workbook=xlwt.Workbook(r'E:\auto_web\Vlt\app_interface\common\sum.xlsx')
    # 创建一个worksheet
    r_xls=xlrd.open_workbook(r'E:\auto_web\Vlt\app_interface\common\sum.xlsx')
    row = r_xls.sheets()[0].nrows
    excel = copy(r_xls)  # 将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 获取要操作的sheet
    # worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
    for i in range(len(a)):
            for j in range(8):
                # t=int(i)-1
                table.write(i+1, j, a[i][j])
    # 保存
    cc=time.time()
    excel.save(r'E:\auto_web\Vlt\app_interface\common\sum'+'%s'%cc+'.xlsx')

a=[[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1]]
wirte_excel(a)