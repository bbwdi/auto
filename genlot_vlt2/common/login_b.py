# coding:utf-8
import unittest
from pages.loginpage import system_login
import time


user = "gavin-aa"
password = "123456"

def Login_B(user='gavin-aa',password='123456'):
    a=system_login()
    a.open()
    a.user_path(user)
    a.passwd_path(password)
    a.click_path()
    time.sleep(2)
    return a.b


