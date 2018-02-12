#coding=utf-8
'''
Created on 2018年1月4日

@author: leonlee
'''
import time
import datetime
import re

time_format = "%Y-%m-%d"

def next_day(arg_time):
    """
        返回明天的time的struct形式
    """
    arg_time = datetime.datetime.fromtimestamp(time.mktime(arg_time))
    step = datetime.timedelta(days = 1)
    arg_time += step
    return arg_time.timetuple()
    
def parse_time(arg_time):
    """
            解析时间,将类似/Date(1496260217113+0800)/
            解析成 %Y-%m-%d %H:%M:%S的形式
        @param arg_time:    
        @return: 
    """
    #正则表达式截取时间戳
    tmp = re.findall("\((.*?)\+", arg_time, re.S)[0]
    #获取时间戳
    ticks = eval(tmp) / 1000
    #获取毫秒
    millised = eval(tmp) % 1000
    
    time_format = "%Y-%m-%d %H:%M:%S"
    t = time.localtime(ticks)
    #获取时间的字符串形式
    time_str = time.strftime(time_format,t)
    
    return time_str + "." + str(millised)
    