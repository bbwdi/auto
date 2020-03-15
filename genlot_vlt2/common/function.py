# coding:utf-8
import logging
import os,re
import csv
import time
import yaml
import time


def save_screenshot(driver, file_name):
    file_path = "F:\\genlot\\static\\images\\" + file_name + ".png"
    driver.get_screenshot_as_file(file_path)


def get_current_dir():
    file_catalog = str(os.getcwd())
    a = re.compile(r'\S*vlt')
    current_path = str(a.findall(file_catalog)[0])

    return current_path


def get_csv_data(filename):
    data = "F:\\genlot\\static\\data\\"+str(filename)+".csv"
    fo = open(data, 'r')
    reader = csv.reader(fo)
    next(reader)
    rows = []
    for row in reader:
        if row[0] == '√':
            rows.append(row[1:])
    return rows


def wait(seconds):
    time.sleep(seconds)

# 定义日志函数


def init_log():
    logger = None
    logger = logging.getLogger()
    datefmt = "%Y-%m-%d %H:%M:%S"
    format_str = "[%(asctime)s]: %(levelname)s - %(message)s"
    formatter = logging.Formatter(format_str,datefmt)
    stream_handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return [logger,stream_handler]


def log_info(err_msg, level=logging.INFO):
    logger,stream_handler = init_log()
    logger.info(err_msg)
    stream_handler.flush()  # 确保所有的日志输出已经被刷新
    logger.removeHandler( stream_handler)  # 去掉log继承

def GetDataFile_P(filepath):
    #获取yaml文件对应节点条目数据
    with open(filepath) as f:
        r = yaml.safe_load(f.read())
    return r

def regex(patton,str):
    try:
        a=re.search(patton,str)
        tt=a.group()
        return  tt
    except Exception as e:
        print e


if __name__ == '__main__':
    pass