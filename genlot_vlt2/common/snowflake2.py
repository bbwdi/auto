# coding:utf-8

import snowflake.client
import binascii

def crc32(v):
    #return '0x%x' % (binascii.crc32(v) & 0xffffffff) #取crc32的八位数据 %x返回16进制
    return binascii.crc32(v) & 0xffffffff
def getDataBaseIndex(key,db_num,tb_num):
    routeKey = crc32(key)
    print routeKey
    index = routeKey % tb_num % db_num
    return index
def getTableIndex(key,db_num,tb_num):
    routeKey = crc32(key)
    print routeKey
    index = routeKey % tb_num % db_num
    return index
host = '127.0.0.1'
port = 30001
snowflake.client.setup(host, port)
#获取ID
id = snowflake.client.get_guid()
print id
#print snowflake.client.get_stats()
#输出哈希值
print getDataBaseIndex(str(id),2,6)
print getTableIndex(str(id),2,6)