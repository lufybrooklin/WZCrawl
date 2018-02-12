#coding=utf-8
'''
Created on 2018骞�1鏈�3鏃�

@author: leonlee
'''

import conf
from utility.crawl_helper import CrawlHelper
import json

class BridgeCrawl(object):
    '''
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.__helper = CrawlHelper();
    
    def crawl_data(self,crawl_type,start_time,end_time):
        """
            @param crawl_type: 爬取的类型
            @param start_time: 开始时间
            @param end_time:  结束时间
            @return: 爬取的数据
        """
        data =  self.__helper.crawl_data(
                        start_time  = start_time,
                         end_time = end_time,
                         sensorIds = conf.sensorsId_dict[crawl_type])
        data_dict = json.loads(data)
        
        return data_dict
        
        
    def crawl_tilt(self,start_time,end_time):
        """
            @param start_time: 开始时间
            @param end_time:  结束时间
            @return: 爬取的数据
        """
        return self.crawl_data("tilt", start_time, end_time) 
        
        
    def crawl_crack(self,start_time,end_time):
        """
            @param start_time: 开始时间
            @param end_time:  结束时间
            @return: 爬取的数据
        """
        return self.crawl_data("crack", start_time, end_time)
        
    def crawl_fastness(self,start_time,end_time):
        """
            @param start_time: 开始时间
            @param end_time:  结束时间
            @return: 爬取的数据
        """
        return self.crawl_data("fastness", start_time, end_time)
           
    def crawl_completed(self,start_time,end_time):
        """
            @param start_time: 开始时间
            @param end_time:  结束时间
            @return: 爬取的数据
        """
        return self.crawl_data("completed", start_time, end_time)
    
    def crawl_strain(self,start_time,end_time):
        """
            @param start_time: 开始时间
            @param end_time:  结束时间
            @return: 爬取的数据
        """
        #TODO
        strain_list = conf.sensorsId_dict["strain"]
        
        #总数据
        total_data = []
        #步数
        step = 5
        for i in range(step,len(strain_list),step):
            data = self.__helper.crawl_data(
                           start_time = start_time, 
                           end_time = end_time, 
                           sensorIds = strain_list[i - step:i])
            data_dict = json.loads(data)
            total_data.extend(data_dict)
            
        return data_dict
        