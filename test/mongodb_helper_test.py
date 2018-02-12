#coding=utf8
'''
Created on 2018年1月15日

@author: Administrator
'''
import unittest
from utility.mongodb_helper import MongoDBHelper

class TestMongoDBHelper(unittest.TestCase):
    
    def test_find(self):
        r = self.__helper.find("completed")
        c = 1;
        for i in r:
            print(c)
            c += 1
            print(i["location"])
        print(r.count())
    
    def setUp(self):
        print('setUp...')
        self.__helper = MongoDBHelper()

    def tearDown(self):
        print('tearDown...')

    