#coding=utf8
'''
Created on 2018年1月15日

@author: Administrator
'''

import unittest
from module import bridge_operate
import conf

class TestOperateBridge(unittest.TestCase):
    
    def test_crawl_csv(self):
        a = self.__bridge_operator.crawl_csv()
        for k,v in a.items():
            print(k,len(v))
    
    def setUp(self):
        self.__bridge_operator = bridge_operate.OperateBridge()
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
