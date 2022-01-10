# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:25:02 2022

@author: CRISTIANMIRANDA
"""
import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By

class Confi:

    def __init__(self, password, username, driver):
        self.password = password
        self.username = username
        self.browser = webdriver.Chrome(driver)
    
    def iniciar_seccion(self):
        self.browser.get('https://www.linkedin.com/login/')
        
        self.elementID = self.browser.find_element_by_id('username')
        self.elementID.send_keys(self.username)
        
        self.elementID = self.browser.find_element_by_id('password')
        self.elementID.send_keys(self.password)
        self.elementID.submit()
        
        return self.browser
        
    
        
        
        