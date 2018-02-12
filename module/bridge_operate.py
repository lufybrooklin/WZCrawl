#coding=utf-8
'''
Created on 2018年1月11日

@author: Administrator
'''

import time
from module.bridge_crawl import BridgeCrawl
from module.bridge_dao import BridgeDAO
import threading
import conf
from utility import time_helper
from conf import start_time
from module import bridge_dao

class OperateBridge(object):
    '''
        操作桥梁数据
    '''


    def __init__(self):
        #爬取器和存储器
        self.__crawl = BridgeCrawl();
        self.__bridge_dao = bridge_dao.BridgeDAO()
        
        #线程锁，每个种类一个线程，主线程必须等子线程把当天
        #的数据抓取完了才能抓取到第二天
        self.__lock_dict = {}
        for name in conf.name_dict.keys():
            self.__lock_dict[name] = threading.Lock()
        
    def crawl_save(self,
                   type_name,
                   start_time = conf.start_time,
                   end_time = conf.end_time):
        """
                根据爬取的类型爬取并存储数据
            @param type_name:   类型名
            @param start_time:  爬取的开始的时间   
            @param end_time:   结束时间 
        """
        print("正在爬取{0}的{2}数据...".\
              format(
                  time.strftime(time_helper.time_format,start_time),
                   time.strftime(time_helper.time_format,end_time),
                   conf.name_dict[type_name]
                  ))
        self.__lock_dict[type_name].acquire()
        try:
            if type_name == "strain":
                data = self.__crawl.crawl_strain(start_time, end_time)
            else:
                data = self.__crawl.crawl_data(type_name, start_time, end_time)
            self.__bridge_dao.insert(type_name, data)
        except Exception as e:
            print(e)
        finally: 
            self.__lock_dict[type_name].release()
        print("{0}的{2}数据爬取完成".\
              format(
                  time.strftime(time_helper.time_format,start_time),
                  time.strftime(time_helper.time_format,end_time),
                  conf.name_dict[type_name]
                  ))    
        
    def crawl_save_all(self,
                       start_time = conf.start_time,
                       end_time = conf.end_time):
        """
                爬取并保持所有类型的桥梁数据
        @param start_time:    开始时间
        @param end_time:    结束时间
        """
        #抓取的开始时间和结束时间
        start_time = conf.start_time
        end_time = conf.end_time
        crawl_time = start_time
       
        while crawl_time < end_time:
            crawl_end = time_helper.next_day(crawl_time)
            
            #创建子线程，抓取的一个种类一个线程(比如
            #抓取斜度类型是一个线程，捞度数据是一个线程)
            print("正在爬取{0}的数据...".\
              format(
                  time.strftime(time_helper.time_format,crawl_time)
                  ))
            for type_name in conf.sensorsId_dict.keys():
                t = threading.Thread(target = self.crawl_save,
                                     args = (type_name,crawl_time,crawl_end),
                                     name = type_name)
                t.start()
                #t.join()
          
            #此线程锁是让所有的子线程和主线程同步的
            for i in self.__lock_dict.values(): i.acquire();        
            
            
            print("{0}的数据爬取完成".\
              format(
                  time.strftime(time_helper.time_format,crawl_time)
                  )) 
            crawl_time = time_helper.next_day(crawl_time)
            for i in self.__lock_dict.values(): i.release()
            
            
    def crawl_csv(self,
                  start_time = conf.start_time,
                  end_time = conf.end_time):
        """
        """
        a = time.strptime("2017-1-13 0:0:0","%Y-%m-%d %H:%M:%S")
        b = time.strptime("2017-1-14 0:0:0","%Y-%m-%d %H:%M:%S")
        data = self.__crawl.crawl_data("completed",a,b)
        
#         for i in data:
#             for k,v in i.items():
#                 print(k,v)
        data_dict = {}
        for i in data:
            location = i["location"]
#             print(location)
#             print(i["sensorid"])
            data_dict[location] = []
            for each_data in i["data"]:
                value = each_data["value"][-1]
                data_dict[location].append(value)
        return data_dict
        
        