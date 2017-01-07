# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:18:26 2017

@author: lucifer
"""

import requests
from bs4 import BeautifulSoup
import time

urls=['http://cs.fang.lianjia.com/loupan/pg{}/'.format(str(i)) for i in range(1,5)]
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_attractions(url,data=None):
    
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')
    time.sleep(0.1)
    titles=soup.select('div.col-1 > h2 > a')
    wheres=soup.select('span.region')
    areas=soup.select('div.area > span')
    types=soup.select('div.type')
    prices=soup.select('span.num')


    if data == None:
        for title,where,area,hometype,price in zip(titles,wheres,areas,types,prices):
            data={
                  'title':title.get_text(),
                  'where':where.get_text(),
                  'area':area.get_text(),
                  'hometype':list(hometype.stripped_strings),
                  'price':price.get_text(),
                  }
            print(data)
for single_url in urls:
    get_attractions(single_url)