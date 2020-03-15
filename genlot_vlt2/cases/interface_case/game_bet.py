#coding=utf-8
from interface_common import commonfunc
from interface_common.request import Request
import json
import logging
from cases.interface_case.member_login import  MemberLogin

class Game_bet(Request):
    def bet(self,str,num):
        '''将投注校验剥离，做成公用函数'''
        result = commonfunc.read_excel_row(str,num)  # 获取投注也签 第一行数据
        testurl = result[1]
        testmsg = result[3]
        postdata = result[2]
        '''初始数据：gameId=1&round=1&level=3&spin=2&amount=500&bets=2'''
        patton = "\d+"  # 匹配原则,只匹配数字
        patton1="level"# 匹配原则,只匹配level
        patton2="spin"# 匹配原则,只匹配spin

        tt = commonfunc.refind(result[2], patton)  # 从原始数据中提取数据
        tt1 = commonfunc.refind(result[2], patton1)  # 从原始数据中提取数据,level为空
        tt2= commonfunc.refind(result[2], patton2)  # 从原始数据中提取数据,spin为空
        #正常情况下是6个参数，当关拍为空时，另外把关拍的值设为0，方便后面校验
        if len(tt)==6:
            gameid = tt[0]
            round = tt[1]
            level = tt[2]
            spin = tt[3]
            amount = tt[4]
            bets = tt[5]
        else :
            if tt1==[]:
                gameid = tt[0]
                round = tt[1]
                level = 0
                spin = tt[2]
                amount = tt[3]
                bets = tt[4]
            elif tt2==[]:
                gameid = tt[0]
                round = tt[1]
                level = tt[2]
                spin = 0
                amount = tt[3]
                bets = tt[4]

        a = MemberLogin()
        token = a.MemberLoginbypublic(1)  # 调用彩民登陆，拿token
        Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s" % token}  # 头文件
        # 获取接口返回结果
        returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
        returnresult = json.loads(returnresult)  # 将返回结果变成字典
        trannum = returnresult["data"]["transactionID"]  # 接口返回transactionID
        sql = "select t.*, t.rowid from U_PRODUCT_TRADE.T_GAME_DEAL_ORDER t  \
                          WHERE t.TRANSACTION_ID='%s'" % trannum
        logging.info(sql)
        sqlresult = commonfunc.orcal_query(sql)  # 调用数据库查询数据
        logging.info(sqlresult)
        logging.info(tt)
        logging.info(returnresult)
        self.assertEquals(returnresult["msg"], testmsg)  # 校验msg内容是否成功
        self.assertEquals(sqlresult[0][0], trannum)  # 校验数据库是否有插入数据
        self.assertEquals(int(sqlresult[0][1]), int(gameid))  # 校验数据库中插入的gameid值
        self.assertEquals(int(sqlresult[0][2]), int(round))  # 校验数据库中插入的round值
        self.assertEquals(int(sqlresult[0][3]), int(level))  # 校验数据库中插入的level值
        self.assertEquals(int(sqlresult[0][4]), int(spin))  # 校验数据库中插入的spin值
        self.assertEquals(int(sqlresult[0][15]), int(amount))  # 校验数据库中插入的amount值
        self.assertEquals(int(sqlresult[0][18]), int(bets))  # 校验数据库中插入的bets值
        self.assertEquals(int(sqlresult[0][2]), returnresult["data"]["round"])  # 校验数据库round值和接口返回值对比
        self.assertEquals(int(sqlresult[0][3]), returnresult["data"]["level"])  # 校验数据库level值和接口返回值对比
        self.assertEquals(int(sqlresult[0][4]), returnresult["data"]["spin"])  # 校验数据库spin值和接口返回值对比
        self.assertEquals(int(sqlresult[0][15]), returnresult["data"]["bet"]["amount"])  # 校验数据库amount值和接口返回值对比
        self.assertEquals(int(sqlresult[0][18]), returnresult["data"]["bet"]["bets"])  # 校验数据库bets值和接口返回值对比


    def bet_error(self,str,num):
        '''将投注校验剥离，做成公用函数'''
        result = commonfunc.read_excel_row(str,num)  # 获取投注也签 第一行数据
        testurl = result[1]
        testmsg = result[3]
        postdata = result[2]

        a = MemberLogin()
        token = a.MemberLoginbypublic(1)  # 调用彩民登陆，拿token
        Headers = {"Content-Type": "application/x-www-form-urlencoded", "token": "%s" % token}  # 头文件
        '''初始数据：gameId=1&round=1&level=3&spin=2&amount=500&bets=2'''
        patton = "\d+"  # 匹配原则,只匹配数字
        patton1="gameId"# 匹配原则,只匹配gameId
        patton2="round"# 匹配原则,只匹配round
        patton3 = "level"  # 匹配原则,只匹配level
        patton4 = "spin"  # 匹配原则,只匹配spin
        patton5 = "amount"  # 匹配原则,只匹配amount
        patton6 = "bets"  # 匹配原则,只匹配bets

        msg="参数[round]类型不正确"

        tt = commonfunc.refind(result[2], patton)  # 从原始数据中提取数据
        tt1 = commonfunc.refind(result[2], patton1)  # 从原始数据中提取数据,gameid为空
        tt2= commonfunc.refind(result[2], patton2)  # 从原始数据中提取数据,round为空
        tt3=commonfunc.refind(result[2], patton3)  # 从原始数据中提取数据,level为空
        tt4=commonfunc.refind(result[2], patton4)  # 从原始数据中提取数据,spin为空
        tt5=commonfunc.refind(result[2], patton5)  # 从原始数据中提取数据,amount为空
        tt6=commonfunc.refind(result[2], patton6)  # 从原始数据中提取数据,bets为空

        # 获取接口返回结果
        returnresult = self.sendMsg_POST(url=testurl, postData=result[2], headers=Headers)
        returnresult = json.loads(returnresult)  # 将返回结果变成字典
        #正常情况下是6个参数，判断gameid的值是否为1以及判断该6个字段是否为正整数
        if len(tt)==6:
            gameid = tt[0]
            round = tt[1]
            level = tt[2]
            spin = tt[3]
            amount = tt[4]
            bets = tt[5]
            try:
                if gameid != 1:
                    self.assertEquals(testmsg,returnresult["msg"])
                elif int(round) <= 0:
                    self.assertEquals(testmsg, returnresult["msg"])
                elif int(level) <= 0:
                    self.assertEquals(testmsg, returnresult["msg"])
                elif int(spin) <= 0:
                    self.assertEquals(testmsg, returnresult["msg"])
                elif int(amount) <= 0:
                    self.assertEquals(testmsg, returnresult["msg"])
                elif int(bets) <= 0:
                    self.assertEquals(testmsg, returnresult["msg"])
            except Exception as e:
                logging.error(e)
        elif len(tt)==5:
            pass


    def test_bet001(self):
        '''正常投注所有都填写gameId=1&round=1&level=3&spin=2&amount=50&bets=2'''
        aa=Game_bet().bet("投注", 1)

    def test_bet002(self):
        '''正常投注所有都填写gameId=1&round=1&level=2&spin=1&amount=100&bets=4'''
        aa = Game_bet().bet("投注",2)

    def test_bet003(self):
        '''正常投注所有都填写gameId=1&round=10&level=1&spin=50&amount=200&bets=5'''
        aa = Game_bet().bet("投注",3)

    def test_bet004(self):
        '''正常投注所有都填写gameId=1&round=100&level=1&spin=100&amount=10&bets=3'''
        aa = Game_bet().bet("投注",4)

    def test_bet005(self):
        '''正常投注level为空，gameId=1&round=10&spin=10&amount=10&bets=1'''
        aa = Game_bet().bet("投注",5)

    def test_bet006(self):
        '''正常投注spin为空，gameId=1&round=100&level=1&amount=10&bets=3'''
        aa = Game_bet().bet("投注",6)

    def test_bet007(self):
        '''正常投注spin为空，gameId=1&round=100&level=1&amount=10&bets=3'''
        aa = Game_bet().bet_error("投注",7)









    def runTest(self):
        pass