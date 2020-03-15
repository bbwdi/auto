#coding:utf-8
import random
import time


def regiun():
    '''生成身份证前六位'''
    #列表里面的都是一些地区的前六位号码
    first_list = ['360881','360802','120101','130102','440881','110100','110101','110102','110103','110104','110105','110106','110107','110108','110109','110111']
    first = random.choice(first_list)
    return first

def year():
    '''生成年份'''
    now = time.strftime('%Y')
    #1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
    second = random.randint(1948,int(now)-18)
    age = int(now) - second
    return second


def month():
    '''生成月份'''
    three = random.randint(1,12)
    #月份小于10以下，前面加上0填充
    if three < 10:
        three = '0' + str(three)
        return three
    else:
        return three


def day():
    '''生成日期'''
    four = random.randint(1,28)
    #日期小于10以下，前面加上0填充
    if four < 10:
        four = '0' + str(four)
        return four
    else:
        return four


def id_card1():
    '''生成身份证后四位'''
    #后面序号低于相应位数，前面加上0填充
    five = random.randint(100,999)
    first = regiun()
    second = year()
    three = month()
    four = day()

    temp = str(first)+str(second)+str(three)+str(four)+str(five)
    temp_list = []
    for i in temp:
        temp_list.append(i)

    power = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

    refNumber = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]

    result = 0
    for i in range(len(power)):
        result += power[i] *  int(temp_list[i])
    id_card = temp +  refNumber[(result%11)]
    return id_card
    #print id_card



