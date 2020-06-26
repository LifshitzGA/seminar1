#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:19:28 2020

@author: georgij
"""

import pandas as pd
import requests
import openpyxl
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="введите номер страниц", type=int)
args = parser.parse_args()
print(args.n)

url = 'https://bessmertnybarak.ru/books/abc/?a=е&number='

list_name = []
list_link = []
list_dateDraft = []
list_dateExecution = []
list_place = []

for i in range(1, args.n +1):
    newURL = url + str(i)
    print(newURL)
    
    r = requests.get(newURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    ppl = soup.find_all("div", class_="itemPerson") # array of all people

    for p in ppl:
        name = p.find("div", class_="namePerson").a.string
    
        if name[0] != "Ё":
            continue
        
        link = p.find("div", class_="namePerson").a['href']
    
        txtPerson = p.find("div", class_="txtPerson").contents[0].lower()
        
    
        
        dataStr = ""
        dateDraft = txtPerson.split("приговорен")
        if len(dateDraft) > 1: 
            dataStr = dateDraft[1]
            t = dataStr.split()
            if len(t[0]) == 2:
                dataStr=t[0]+" "+t[1]+" "+t[2]
            elif len(t[0]) == 4 or len(t[0]) == 10:
                dataStr=t[0]
            else :
                dataStr = "N/A"
        else:
            dateDraft = txtPerson.split("осужден")
            if len(dateDraft) > 1: 
                dataStr = dateDraft[1]
                t = dataStr.split()
                if len(t[0]) == 2:
                    dataStr=t[0]+" "+t[1]+" "+t[2]
                elif len(t[0]) == 4 or len(t[0]) == 10:
                    dataStr=t[0]
                else:
                    dataStr = "N/A"
            else:
                dateDraft = txtPerson.split("приговор вынесен")
                if len(dateDraft) > 1: 
                    dataStr = dateDraft[1]
                    t = dataStr.split()
                    if len(t[0]) == 2:
                        dataStr=t[0]+" "+t[1]+" "+t[2]
                    elif len(t[0]) == 4 or len(t[0]) == 10:
                        dataStr=t[0]
                    else :
                        dataStr = "N/A"
                else:
                    dataStr = "N/A"
    
        dataX = ""
        place = ""
        d = ""
        dateEx = txtPerson.split("расстрелян")
        if len(dateEx) > 1: 
            dataX = dateEx [1]
            t = dataX.split()
            if len(t[0]) == 2:
                dataX=t[0]+" "+t[1]+" "+t[2]
            elif len(t[0]) == 4 or len(t[0]) == 10:
                dataX=t[0]
            else :
                dataX = "N/A"    
            d = dateEx [1] 
            a = d.split ("в городе")
            if len(a) > 1: 
                placeEx = a.split ()
                place = placeEx[0]
            else:    
                a = d.split ("в г.")
                if len(a) > 1: 
                    placeEx = a.split ()
                    place = placeEx[0]
                else:
                    place = "N/A"
        else:
            dateEx = txtPerson.split("приговор приведен в исполнение")
            if len(dateDraft) > 1: 
                dataX = dateEx[1]
                t = dataX.split()
                if len(t[0]) == 2:
                    dataX=t[0]+" "+t[1]+" "+t[2]
                elif len(t[0]) == 4 or len(t[0]) == 10:
                    dataX=t[0]
                else :
                    dataX = "N/A"
                d = dateEx [1] 
                a = d.split ("в городе")
                if len(a) > 1: 
                   placeEx = a.split ()
                   place = placeEx[0]
                else:    
                    a = d.split ("в г.")
                    if len(a) > 1: 
                        placeEx = a.split ()
                        place = placeEx[0]
                    else:
                        place = "N/A"  
            else:
                dataX = "N/A"
                d = dateEx [0] 
                a = d.split ("в городе")
                if len(a) > 1: 
                    placeEx = a.split ()
                    place = placeEx[0]
                else:    
                    a = d.split ("в г.")
                    if len(a) > 1: 
                        placeEx = a.split ()
                        place = placeEx[0]
                    else:
                        place = "N/A"  
                            
        list_name.append(name)   
        list_link.append("https://bessmertnybarak.ru"+link)
        list_dateDraft.append(dataStr)
        list_dateExecution.append(dataX)
        list_place.append(place)


d = {'ФИО': list_name, 'Ссылка': list_link, 'Дата приговора': list_dateDraft, "Дата исполнения приговора": list_dateExecution, "Место исполнения приговора":  list_place}
df = pd.DataFrame(data=d)
print (df)        
print (place)
df.to_excel('list of repressions.xlsx')
