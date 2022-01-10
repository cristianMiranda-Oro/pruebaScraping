# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:54:35 2022

@author: CRISTIANMIRANDA
"""


import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
sys.path.append(".")

from configuracion import confi
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    # Inicializar el objeto de configuracion
    file = open('config.txt')
    lines = file.readlines()
    username = lines[0]
    password = lines[1]
    file.close()

    config = confi(password, username, "driver/chromedriver.exe", '/in/catarinasantosbotelho/')
    config.iniciar_seccion()
    

browser = webdriver.Chrome("driver/chromedriver.exe")

browser.get('https://www.linkedin.com/login/')

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

browser.get("https://www.linkedin.com"+'/in/catarinasantosbotelho/')
soup = BeautifulSoup(browser.page_source, 'lxml')

############################Perfil############################################
#link del perfil
perfil = []
linkperfil = "https://www.linkedin.com"+'/in/catarinasantosbotelho/'
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

##########################Historial Academico##################################

############Expandir Section education
#boton = soup.find('button', {'class' : 'pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle artdeco-button artdeco-button--tertiary artdeco-button--muted'})
#print("Button del perfil: ", boton.get_text().strip())


historyAcademic = []
browser.find_element(By.CSS_SELECTOR, ".pv-profile-section__see-more-inline").click()


#mirar si es expandido buble while
soup = BeautifulSoup(browser.page_source, 'lxml')

estado = soup.find('button', {'class' : 'pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle artdeco-button artdeco-button--tertiary artdeco-button--muted'})

if estado != None:
    print("No esta expandido")
else:
    print("Esta expandido")
    

#Obtener la informacion

educacion = soup.findAll('li', {'class': 'pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view'})

for x in educacion:
    edu = []
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
    
    try:
        titulacion = x.findAll('span', {'class':'pv-entity__comma-item'})
        print("Titulacion: ", titulacion[0].get_text().strip())
        #historyAcademic.append(titulacion[0].get_text().strip())
        edu.append(titulacion[0].get_text().strip())
        try:
            print("Academia: ", titulacion[1].get_text().strip())
            #historyAcademic.append(titulacion[1].get_text().strip())
            edu.append(titulacion[1].get_text().strip())
        except:
            print("Academia: No encontrado")
            #historyAcademic.append("Academia: No encontrada")
            edu.append("Academia: No encontrada")
    except:
        print("Titulacion: No encontrada")
        #historyAcademic.append("Titulacion: No encontrada")
        #historyAcademic.append("Academia: No encontrada")
        edu.append("Titulacion: No encontrada")
        edu.append("Academia: No encontrada")
        
    try:
        anios = x.findAll('time')
        print("Tiempo: " + anios[0].get_text().strip()+"-"+anios[1].get_text().strip())
        #historyAcademic.append(anios[0].get_text().strip()+"-"+anios[1].get_text().strip())
        edu.append(anios[0].get_text().strip()+"-"+anios[1].get_text().strip())
    except:
        print("Tiempo: No encontrado")
        #historyAcademic.append("Tiempo: No encontrado")
        edu.append("Tiempo: No encontrado")
        
    print("******************************************")
    historyAcademic.append(edu)
    
#############################Intereses##########################################

#Desplegar el modal

try:
    
    browser.get("https://www.linkedin.com" + '/in/catarinasantosbotelho/detail/interests/')
    soup = BeautifulSoup(browser.page_source, 'lxml')
    
    
    menuNav = soup.findAll('ul', {'class' : 'display-flex justify-flex-start list-style-none mt3'})
    menu = BeautifulSoup(str(menuNav), 'lxml')
    tagli = menu.findAll('a')
    
    
    links= []
    nombres = []
    for x in tagli:
        links.append(x.get('href'))
        nombres.append(x.get_text().strip())
        
    intereses = []
    
    
    #Obtnemos los intereses
    for link in links:        
        inter = []
        browser.get("https://www.linkedin.com"+link)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        
        items = soup.findAll('span', {'class':'pv-entity__summary-title-text'})
        
        try:
            for x in items:
                print("----: ", x.get_text().strip())
                inter.append(x.get_text().strip())
        except:
            inter.append("No found")
            print("----: No found")
        
        intereses.append(inter)
        
        print("******************************")
    
    
except:
    print("Error No configuration")




