#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import pandas as pd 
from lxml import etree
import mail

if __name__ == "__main__":
    
    url="https://dolarhoy.com/"
    r=requests.get(url)

    soup=BeautifulSoup(r.content, "html.parser")

    if r.status_code==200:
        dom = etree.HTML(str(soup))
        dolarblueCom = dom.xpath('//div[@class="tile is-parent is-5"]/div/div/div[@class="compra"]/div[2]')
        dolarblueCom=dolarblueCom[0].text
        dolarblueVen = dom.xpath('//div[@class="tile is-parent is-5"]/div/div/div[@class="venta"]/div[2]')
        dolarblueVen=dolarblueVen[0].text
        doficom=dom.xpath('//div[@class="tile is-child only-desktop"]/div/div[@class="compra"]/div[2]')
        doficom=doficom[0].text
        dofiven=dom.xpath('//div[@class="tile is-child only-desktop"]/div/div[@class="venta"]/div[2]')
        dofiven=dofiven[0].text
        dobolsacom=dom.xpath('//div[@class="tile is-parent is-7 is-vertical"]/div[3]/div/div[@class="compra"]/div[2]')
        dobolsacom=dobolsacom[0].text
        dobolsaven=dom.xpath('//div[@class="tile is-parent is-7 is-vertical"]/div[3]/div/div[@class="venta"]/div[2]')
        dobolsaven=dobolsaven[0].text
        doliquicom=dom.xpath('//div[@class="tile is-parent is-7 is-vertical"]/div[4]/div/div[@class="compra"]/div[2]')
        doliquicom=doliquicom[0].text
        doliquiven=dom.xpath('//div[@class="tile is-parent is-7 is-vertical"]/div[4]/div/div[@class="venta"]/div[2]')
        doliquiven=doliquiven[0].text
        dolarsoli=dom.xpath('//div[@class="tile is-parent is-7 is-vertical"]/div[5]/div/div[@class="venta"]/div[2]')
        dolarsoli=dolarsoli[0].text


        dateuptd=dom.xpath('//div[@class="tile is-parent is-5"]/div/div[2]/span')
        dateuptd=dateuptd[0].text
    else:
        print("error")

    #print(dolarblueCom,dolarblueVen,doficom,dofiven,dobolsacom,dobolsaven,doliquicom,doliquiven,dolarsoli,dateuptd.split(" ")[2])
    df=pd.DataFrame({'Compra':[dolarblueCom,doficom,dobolsacom,doliquicom,0]
                    ,'Venta':[dolarblueVen,dofiven,dobolsaven,doliquiven,dolarsoli]
                    ,'Fecha Actualizacion':[dateuptd.split(" ")[2],dateuptd.split(" ")[2],dateuptd.split(" ")[2], dateuptd.split(" ")[2],dateuptd.split(" ")[2]]
                    }
                    ,
                    index=['DolarBlue','DolarOficial','DolarBolsa','Contado con Liqui','Dolar Solidario'])
    print(df)


     


