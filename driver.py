# -*- coding: utf-8 -*-
'''
Created on 20171103

@author: ojil
'''
#     公用 启动浏览器
from selenium import webdriver
def browser():
    driver = webdriver.Firefox()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://console-bgw.369cloud.com/auth/login/?next=/project/cdn/')
    dr.quit()