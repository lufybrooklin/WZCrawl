#coding=utf-8
'''
Created on 2018骞�1鏈�4鏃�

@author: leonlee
'''

from utility import mongodb_helper
import conf
from utility import time_helper
import datetime

class BridgeDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__helper = mongodb_helper.MongoDBHelper()
    
    def insert(self,type_name,data):
        """
            娣诲姞鏁版嵁
            @param type_name: 绫诲瀷 
        """
        return self.__helper.insest(type_name, data)
        
    def insert_tilt(self,data):
        """
            娣诲姞鍊炬枩鏁版嵁
            @param data:  
        """
        return self.__helper.insest("tilt", data);
    
    def insert_crack(self,data):
        """
            娣诲姞瑁傜紳鏁版嵁
            @param data:  
        """
        return self.__helper.insest("crack", data);
    
    def insert_fastness(self,data):
        """
            娣诲姞鎹炲害鏁版嵁
            @param data:  
        """
        return self.__helper.insest("fastness", data);
    
    def insert_strain(self,data):
        """
            娣诲姞搴斿彉鏁版嵁
            @param data:  
        """
        return self.__helper.insest("strain", data);
    
    def insert_completed(self,data):
        """
            娣诲姞绱㈠姏鏁版嵁
            @param data:  
        """
        return self.__helper.insest("completed", data);
    
    def find_completed(self):
        """
            通过类型名获取数据
            @param type_name:    类型名
            @param start_time:    开始时间
            @param end_time:    结束时间
        """
        completeds = self.__helper.find("completed");
        print(1)
#         print(len(completeds))
#         for completed in completeds:
#             location = completed["location"]
#             for data in completed["data"]:
#                 t = data["acquisitiontime"]
#                 t = time_helper.parse_time(t)
#                 print(t)
#                 print(data["value"])
                
            
        

    