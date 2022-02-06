'''
by: Ing.Joaquin Gallardo
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree

url="https://ikiwi.net.ar/valor-uva"
r=requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
VALOR_INI=float(97.58)#almacenamos en una constante el valor iniicial del UVA al dia 1/1/22

valorfin1=soup.find_all('div',attrs={'class':'col-md-12'}) #traemos todos los elementos que contiene el <div class="col-md-12"> <center><strong style="color:#006644; font-size:45px">$ 101.16</strong><br><em>Actualizada al 06/02/2022</em></center> </div> 
for i in valorfin1:# como del paso anterior obtenemos una lista lo que procedemos hacer es recorrerla y extraer solamente el objeto strong que es quien almacena el valor de UVA a dia actual
    vf=i.find('strong').text #Obtenemos el texto y lo almacenamos en una variable que usaremos posteriormente para la formula 

result=((float(vf[1:8])-VALOR_INI)/VALOR_INI)*100 
print("El valor porcentual del UVA en el año es={}%".format(result))