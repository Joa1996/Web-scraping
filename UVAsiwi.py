'''
La idea de este webscraper es obtener el valor UVA de todos los meses de esta pagina 
https://ikiwi.net.ar/valor-uva
by: Ing.Joaquin Gallardo
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree

url="https://ikiwi.net.ar/valor-uva"
r=requests.get(url)
soup=BeautifulSoup(r.content, "html.parser")

dom = etree.HTML(str(soup))
table=dom.xpath('//div[@class="expando"]/table') #de esta manera estamos obteniendo todas las tablas en la cual cada tabla representa el mes de todos los años con el correspondiente valor de UVA
listatablas=[]#creamos una lista donde almacenaremos los respectivos meses con el valor UVA de Cada Mes 

for i in range(int(len(table))): #Como el objeto recolecta la cantidad correspondiente a todos los meses con el valor de UVA procedemos a recorrer todos esos meses para posterior almacenarlo en un dataframe
    id=table[i].get("id") #Obtenemos todos los id de todas las tablas para despues pasarselo a pandas y este pueda rastrear todas las tablas
    tabla=pd.read_html(r.text,attrs={'id':id})
    listatablas.append(tabla) #Almacenamos cada tabla en una lista
    df=pd.DataFrame(listatablas) #lo cargamos es un data frame

df.to_csv('C:/Users/joaqu/Downloads/tablas.csv') #Almacenamos todas las tablas que contienen los valores UVA de cada año en un CSV
print("Done")




'''for i  in range(2):
    url="https://ikiwi.net.ar/valor-uva/#Expando7{}".format(i)
    r=requests.get(url)


    tabla=pd.read_html(r.text,attrs={'class':'tablepress tablepress-id-408'})
   
    df=tabla[0]
    #UVAprimerdia=int(df['UVA'].iloc[0:1])
    #print(UVAprimerdia)
    print(df)
'''
