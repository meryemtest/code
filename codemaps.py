import time
import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#initialisation du navigateur
driver=webdriver.Chrome()
#accéder a la page google maps
driver.get("https://www.google.com/maps")

#effectuer une recherche
search=driver.find_element(By.ID, "searchboxinput")  
time.sleep(5)
search.send_keys("café")   #envoyer les mots clés de recherche
time.sleep(5)
search.send_keys(Keys.ENTER)
time.sleep(5)
results = driver.find_elements(By.CLASS_NAME,"hfpxzc")
names=[]
for i in results:
    i.click()
    time.sleep(5)
    page_source=driver.page_source     #obtenir le code HTML
    soup=BeautifulSoup(page_source, 'html.parser')
    time.sleep(5)
    café_names=soup.find_all("h1", {"class", "DUwDvf lfPIob"})
    time.sleep(5)
    for name in café_names:
        print(name.text)