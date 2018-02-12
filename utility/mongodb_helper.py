#coding=utf-8
'''
Created on 2018年1月3日

@author: leonlee
'''

import conf
from pymongo import MongoClient

class MongoDBHelper(object):
    """
        MongoDB
    """
    def __init__(self):
        self.__con_dict = conf.db_conn_dict
        self.__db_name = conf.db_name
        
        self.__conn = None
    
    def insest(self,collection_name,data):
        """
            添加
            @param collection_name:   集合名
            @param data:  数据,要求dict类型 
        """
        #获取连接
        conn = self.__get_conn__()
        db = conn[self.__db_name]
        collection = db[collection_name]
        collection.insert(data)
        
    def find(self,collection_name,query = {},projection = {}):
        """
                        根据条件查询数据
            @param collection_name:  集合名
            @param query:   条件  
            @return:    查询的数据
        """
        conn = self.__get_conn__();
        db = conn[self.__db_name]
        collection = db[collection_name]
        
        #获取游标
        cursor = collection.find(query)
        
#         print(cursor)
#         print(cursor.count())
#         for i in cursor:
#             yield i;
        return cursor
        
        
    def __get_conn__(self):
        """
            返回连接 
        """
        if self.__conn is None:
            self.__conn = MongoClient(**self.__con_dict)
        return self.__conn
    
    def close(self):
        """
            关闭连接
        """
        if self.__conn is not None:
            self.__conn.close()
            