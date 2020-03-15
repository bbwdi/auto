# coding:utf-8
import cx_Oracle

conn=cx_Oracle.connect('U_VLT_BMS/123456@10.6.0.202/ORCL')

cr = conn.cursor()

sql="select * from t_device"

recr = cr.execute(sql)

results = recr.fetchall()
#print results
for re in results:
    print re

conn.close()