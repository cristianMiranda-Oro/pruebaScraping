# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:23:29 2022

@author: CRISTIANMIRANDA
"""
import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By


class Academic():
    
    def __init__(self, browser, usuario):
        self.usuario = usuario
        self.browser = browser
        
    
    def obtener_educacion(self):
        
        historyAcademic = []
        
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".pv-profile-section__see-more-inline").click()
            
            
            #mirar si es expandido buble while
            soup = BeautifulSoup(self.browser.page_source, 'lxml')
            
            estado = soup.find('button', {'class' : 'pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle artdeco-button artdeco-button--tertiary artdeco-button--muted'})
            
            if estado != None:
                pass
                #print("No esta expandido")
            else:
                pass
                #print("Esta expandido")
        except:
            soup = BeautifulSoup(self.browser.page_source, 'lxml')
            
        
        #Obtener tag educacion
        
        educacion = soup.findAll('li', {'class': 'pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view'})
        
        for x in educacion:
            edu = []
            
            #Obtenemos el titulo de la academia
            try:
                titulo = x.find('h3', {'class' : 'pv-entity__school-name t-16 t-black t-bold'})
                print("titulo: ", titulo.get_text().strip())
                #historyAcademic.append(titulo.get_text().strip())
                edu.append(titulo.get_text().strip())
            except:
                print("Titulo: No encontrado")
                #historyAcademic.append("No Encontrado")
                edu.append("No Encontrado")
            print()
            
            #Obtenemos otros datos relacionados con la academia
            try:
                #Obtenemos titulo
                titulacion = x.findAll('span', {'class':'pv-entity__comma-item'})
                print("Titulacion: ", titulacion[0].get_text().strip())
                #historyAcademic.append(titulacion[0].get_text().strip())
                edu.append(titulacion[0].get_text().strip())
                try:
                    #Obtenemos la academia 
                    print("Academia: ", titulacion[1].get_text().strip())
                    #historyAcademic.append(titulacion[1].get_text().strip())
                    edu.append(titulacion[1].get_text().strip())
                except:
                    #si no llega existir el dato
                    print("Academia: No encontrado")
                    #historyAcademic.append("Academia: No encontrada")
                    edu.append("Academia: No encontrada")
            except:
                #si no llega existir informacion del titulo
                print("Titulacion: No encontrada")
                #historyAcademic.append("Titulacion: No encontrada")
                #historyAcademic.append("Academia: No encontrada")
                edu.append("Titulacion: No encontrada")
                edu.append("Academia: No encontrada")
                
            try:
                #Obtenemos el tiempo de estudio
                anios = x.findAll('time')
                print("Tiempo: " + anios[0].get_text().strip()+"-"+anios[1].get_text().strip())
                #historyAcademic.append(anios[0].get_text().strip()+"-"+anios[1].get_text().strip())
                edu.append(anios[0].get_text().strip()+"-"+anios[1].get_text().strip())
            except:
                #Por si no llega a existir
                print("Tiempo: No encontrado")
                #historyAcademic.append("Tiempo: No encontrado")
                edu.append("Tiempo: No encontrado")
                
            print("******************************************")
            historyAcademic.append(edu)
            
        return historyAcademic
