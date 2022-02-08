#!/usr/bin/env python
# coding: utf-8
'''
La idea de este script es recorrer todas las paginas de ebay por producto y obtener la URL, el precio y el nombre del producto
'''
# In[38]:


import time
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


# In[39]:


driver=webdriver.Chrome("C:\WebDrivers\chromedriver.exe")   
driver.get('https://www.ebay.com/')


# In[40]:


driver.find_element_by_xpath('//input[@class="gh-tb ui-autocomplete-input"]').send_keys('Iphone 8')
time.sleep(2) 
driver.find_element_by_xpath('//input[@class="btn btn-prim gh-spr"]').click()
time.sleep(2) 


# In[62]:





# In[41]:


listanombres= []
listaprecios= []
listaurl= []


# In[42]:


for i in range(4):
    #Si ponemos solamente element sin s al final trae el primer elemento web, en cambio si colocamos con s al final, traera todos los elementos que necesitamos
    names=driver.find_elements_by_xpath('//ul[@class="srp-results srp-list clearfix"]/li//h3[@class="s-item__title"]')
    names=[i.text for i in names]
    precio= driver.find_elements_by_xpath('//ul[@class="srp-results srp-list clearfix"]/li//div[@class="s-item__info clearfix"]//div[1]/span[@class="s-item__price"]')
    precio=[i.text for i in precio]
    url=driver.find_elements_by_xpath('//ul[@class="srp-results srp-list clearfix"]/li//a[@class="s-item__link"]')
    url = [i.get_attribute('href') for i in url]
#En este caso debi buscar todo el xpath    ya que si seleccionaba solamente el objeto,pues este no me lo encontraba 
    listanombres.extend(names)
    listaprecios.extend(precio)
    listaurl.extend(url)
    
    try:
        driver.find_element_by_xpath('//a[@class="pagination__next icon-link"]').click()
    except:
        break


# In[43]:


df=pd.DataFrame({'Producto':listanombres,'Precio':listaprecios,'URL':listaurl})
df.to_csv('Scrapingebay.csv') #Almacenamos el resultado en un CSV


# In[ ]:




