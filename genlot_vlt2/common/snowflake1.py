__author__ = 'qwer'
# coding:utf-8

import time
class MySnow:
    def __init__(self,dataID):
        self.start = int(time.mktime(time.strptime('2018-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")))
        self.last = int(time.time())
        self.countID = 0
        self.dataID = dataID

    def get_id(self):

        now = int(time.time())
        temp = now-self.start
        if len(str(temp)) < 9:
            length = len(str(temp))
            s = "0" * (9-length)
            temp = s + str(temp)
        if now == self.last:
            self.countID += 1
        else:
            self.countID = 0
            self.last = now



        if self.countID == 99999:
            time.sleep(1)

        id = str(temp) + str(self.dataID)
        return id


snow = MySnow(dataID="00")
print(snow.get_id())




