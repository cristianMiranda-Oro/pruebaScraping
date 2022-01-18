# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:22:26 2022

@author: CRISTIANMIRANDA
"""

import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By


class Perfil():
    
    def __init__(self, browser, usuario):
        self.usuario = usuario
        self.browser = browser
        
        
    def obtener_informacion(self):
        
        self.browser.get("https://www.linkedin.com"+self.usuario)
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        
        #link del perfil
        perfil = []
        linkperfil = "https://www.linkedin.com"+self.usuario
        print("Link del perfil: ", linkperfil)
        perfil.append(linkperfil)

        #nombre del perfil
        nombrePerfil = soup.find('h1', {'class' : 'text-heading-xlarge inline t-24 v-align-middle break-words'})
        print("Nombre del perfil: ", nombrePerfil.get_text().strip())
        perfil.append(nombrePerfil.get_text().strip())

        #informacion del perfil
        informacionPerfil = soup.find('div', {'class' : 'text-body-medium break-words'})
        print("Informacion del perfil: ", informacionPerfil.get_text().strip())
        perfil.append(informacionPerfil.get_text().strip())

        #Ubicacion
        ubicacionPerfil = soup.find('span', {'class' : 'text-body-small inline t-black--light break-words'})
        print("Ubicacion del perfil: ", ubicacionPerfil.get_text().strip())
        perfil.append(ubicacionPerfil.get_text().strip())

        educaEmple = soup.findAll('div', {'style' : "line-height:2rem;max-height:4rem;-webkit-line-clamp:2;"})
        #Obtener el ultimo empleo
        print("Ultimo empleo: ", educaEmple[0].get_text().strip())
        perfil.append(educaEmple[0].get_text().strip())
        
        #Obtener el ultima educacion
        print("Ultima Educacion: ", educaEmple[1].get_text().strip())
        perfil.append(educaEmple[1].get_text().strip())
        
        
        return perfil
    