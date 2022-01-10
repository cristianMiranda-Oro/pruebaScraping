# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:25:02 2022

@author: CRISTIANMIRANDA
"""
import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

class confi:

    def __init__(self, password, username, driver, usuario):
        self.password = password
        self.username = username
        self.browser = webdriver.Chrome(driver)
        self.usuario = usuario
    
    def iniciar_seccion(self):
        self.browser.get('https://www.linkedin.com/login/')
        
        self.elementID = self.browser.find_element_by_id('username')
        self.elementID.send_keys(self.username)
        
        self.elementID = self.browser.find_element_by_id('password')
        self.elementID.send_keys(self.password)
        self.elementID.submit()
        
    def informacion_perfil(self):
        self.browser.get("https://www.linkedin.com"+self.usuario)
        soup = BeautifulSoup(self.browser.page_source)
        nombrePerfil = soup.find('h1', {'class' : 'text-heading-xlarge inline t-24 v-align-middle break-words'})
        print("Nombre del perfil: ", nombrePerfil.get_text().strip)
        
        