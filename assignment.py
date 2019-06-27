#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:59:03 2019

@author: manzar
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = 'https://www.avk-tv.de/companies.php?page='
file = open('assignment.csv', 'w')
header = 'Company Name, Email, Tel, Fax, Website\n'
file.write(header)
for i in range(9):
    url = urls + str(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    panels = soup.findAll('div', {'class': 'panel panel-default'})
    for panel in panels:
        name = panel.h3.text
        #print(name)
        body = panel.findAll('address')
        body = body[1].contents
        email = ''
        web = ''
        number = []
        tel = ''
        fax = ''
        for x in body:
            try:
                if('http' in x.attrs['href']):
                    web = x.attrs['href']
            except:
                pass
            
            try:
                if('@' in x):
                    email = x.split('\u2003\u2003')[1]
            except:
                pass
            
            try:
                if(not any(c.isalpha() for c in x.split('\u2003\u2003')[1])):
                    number.append(x.split('\u2003\u2003')[1])
            except:
                pass
                
                
                
                
        if(len(email) < 5):
            email = 'NaN'
        if(len(web) < 5):
            web = 'NaN'
        #print(web, email)
        #print(len(number))
        count = 0
        for num in number:
            if(num == ''):
                number.pop(count)
            count += 1
        #print(number)
        if(len(number) == 0):
            tel = 'NaN'
            fax = 'NaN'
        elif(len(number) == 1):
            tel = number[0]
            fax = 'Nan'
        elif(len(number) == 2):
            tel = number[0]
            fax = number[1]
        #print(tel, fax)
        file.write(name.replace(',', '') + ', ' + email + ', ' + tel + ', ' + fax + ', ' + web + '\n')
file.close()
file = pd.read_csv('assignment.csv')
                
    