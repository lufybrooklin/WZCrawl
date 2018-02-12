#coding=utf-8
'''
Created on 2018年1月3日

@author: leonlee
'''
from module import bridge_operate

    
def main():
    operater = bridge_operate.OperateBridge();
    operater.crawl_save_all()

    
if __name__ == '__main__':
    main()