#coding=utf-8
'''
Created on 2018年1月3日

@author: leonlee
'''
import requests
import conf
import time
import json

class CrawlHelper(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__login_data = conf.login_data
        self.__login_url = conf.login_url
        
        response = self.__login__(
            conf.login_url,**self.__login_data)[1]     
        self.__login_cookie = json.loads(response.text)

    def __login__(self,url,**form_data):
        """
            表单登录
            @param url:
            @param form_data: 表单数据
            @return 登录的session,响应数据
        """
        session = requests.session()
        response = session.post(url,data = form_data,
                                allow_redirects = True)
        return session,response

    def crawl_data(
            self,
            start_time,
            end_time,
            sensorIds ):
        """
            获取倾斜数据
            @param param: cookie参数 
            @param start_time: 开始时间
            @param end_time:  结束时间
            @param sensorIds:  传感器ID,默认获取所有传感器
            @return:    服务器返回的json格式
        """
        #url
        url = conf.base_url
        #登录时获取的coookie
        cookies = self.__login_cookie
        
        #转换成字符串
        start_time = time.strftime("%Y-%m-%d %H:%M:%S",start_time)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S",end_time)
        sensorIds_str = str(sensorIds)[1:-1].replace(" ","")
        
        data = {
            r"path" : u"/sensor/" + sensorIds_str 
                        + "/data/" + start_time + "/" + 
                        end_time + "?",
            r"sensor" : sensorIds_str
        }
        response = requests.get(url = url  + "?"
                         + "path="+data["path"] + 
                         "&" + "sensor="+data["sensor"],params = cookies)
        #TODO 此种方式请求不成功
        #response = s.get(url = url,params = d)
        return response.text
