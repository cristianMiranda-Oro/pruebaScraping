# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:24:25 2022

@author: CRISTIANMIRANDA
"""

import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By

class Interes():
    
    def __init__(self, browser, usuario):
        self.usuario = usuario
        self.browser = browser
        
        
    def obtener_intereses(self):
        
        #Desplegar el modal
        nombres = []
        intereses = []
        try:
            
            self.browser.get("https://www.linkedin.com" + self.usuario+'detail/interests/')
            soup = BeautifulSoup(self.browser.page_source, 'lxml')
            
            
            menuNav = soup.findAll('ul', {'class' : 'display-flex justify-flex-start list-style-none mt3'})
            menu = BeautifulSoup(str(menuNav), 'lxml')
            tagli = menu.findAll('a')
            
            
            links= []
            
            for x in tagli:
                links.append(x.get('href'))
                nombres.append(x.get_text().strip())
                
           
            
            
            #Obtnemos los intereses
            i=0
            for link in links:        
                inter = []
                self.browser.get("https://www.linkedin.com"+link)
                soup = BeautifulSoup(self.browser.page_source, 'lxml')
                
                items = soup.findAll('span', {'class':'pv-entity__summary-title-text'})
                
                try:
                    print("**************"+nombres[i]+"***************")
                    for x in items:
                        print("----: ", x.get_text().strip())
                        inter.append(x.get_text().strip())
                    i = i + 1
                except:
                    inter.append("No found")
                    print("----: No found")
                
                intereses.append(inter)
                
                print("******************************")
            
        except:
            print("Error No configuration")
            
        return nombres, intereses
    