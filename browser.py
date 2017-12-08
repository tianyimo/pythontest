# -*- coding: utf-8 -*-
'''
Created on 20171103

@author: ojil
'''
from selenium import webdriver
import driver
import unittest
#   启动浏览器输入网址 ַ
class browser(object):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':
    unittest.main()
       
        