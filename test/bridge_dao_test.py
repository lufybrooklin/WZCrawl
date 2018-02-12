#coding=utf8
'''
Created on 2018年1月15日

@author: Administrator
'''
import unittest
from module.bridge_dao import BridgeDAO

class TestBridgeDAO(unittest.TestCase):
    def setUp(self):
        self.__dao = BridgeDAO();
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_find_completed(self):
        self.__dao.find_completed()
        
        
        
if __name__ == "__main__":
    unittest.main()