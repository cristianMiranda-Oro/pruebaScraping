# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:54:35 2022

@author: CRISTIANMIRANDA
"""


import os, random, sys, time
import pandas as pd
import re
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
sys.path.append(".")

from configuracion import Confi #Clase Confi -> iniciar el Navegador
from perfil import Perfil #Clase Perfil para obtener informacion del perfil
from history_academic import Academic #Clase para obtener informacion academica
from intereses import Interes #Clase para obtener los intereses del perfil

from selenium.webdriver.common.by import By

if __name__ == "__main__":
    
    # Leemos las credenciasles de linkedin
    file = open('config.txt')
    lines = file.readlines()
    username = lines[0]
    password = lines[1]
    file.close()

    usuario = '/in/catarinasantosbotelho/'
    
    #Iniciamos la configuracion del browser
    config = Confi(password, username, "driver/chromedriver.exe")
    browser = config.iniciar_seccion()
    
    #Obtenemos la informacion del perfil
    perfil = Perfil(browser, usuario)
    perfiList = perfil.obtener_informacion()
    
    #Obtenemos la informacion academica
    historyAcademic = Academic(browser, usuario)
    historyAcademicList = historyAcademic.obtener_educacion()
    
    #Obtenemos la informacion de intereses
    intereses = Interes(browser, usuario)
    nombresList, interesList = intereses.obtener_intereses()
    
    ##################Guardamos la informacion#################################
    
    #perfil
    dataPerfil = {}
    
    dataPerfil['link'] = perfiList[0]
    dataPerfil['FullName'] = perfiList[1]
    dataPerfil['information'] = perfiList[2]
    dataPerfil['ubication'] = perfiList[3]
    
    #creamos dataframe
    df = pd.DataFrame(dataPerfil, index=[...])
    #guardamos como archivos CSV
    df.to_csv("output/"+re.sub(r"\s+", "", perfiList[1])+'_perfil.csv', index=False)
    
    #educacion
    dataEducation = {}

    dataTitulo = []
    dataTitulacion = []
    dataAcademia = []
    dataTiempo = []

    for x in historyAcademicList:
        dataTitulo.append(x[0])
        dataTitulacion.append(x[1])
        dataAcademia.append(x[2])
        dataTiempo.append(x[3])
        
    dataEducation['title'] = dataTitulo
    dataEducation['titulation'] = dataTitulacion
    dataEducation['academic'] = dataAcademia
    dataEducation['time'] = dataTiempo

    #creamos dataframe
    df = pd.DataFrame(dataEducation)
    #Guardamos como archivo csv
    df.to_csv("output/"+re.sub(r"\s+", "", perfiList[1])+'_education.csv', index=False)

    #Interes
    
    txt = ""
    count = 0
    
    for inte in interesList:
        txt = txt+nombresList[count]+": "
        count = count + 1
        for x in inte:
            txt = txt+x+"***"
        txt = txt+"\n"
    
    #Lo guradmos como archivo txt
    with open("output/"+re.sub(r"\s+", "", perfiList[1]) +"_interes.txt", 'w') as file:
        file.write(txt)










