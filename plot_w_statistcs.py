#!/usr/bin/python3

import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt 
import sys,os
df = pd.read_excel('data.xlsx')

data_top = df.head()
#print (data_top)
currentDir = os.getcwd()

pd.to_datetime(df['Date'])
# find different areas
area_frame = df['Area'].unique()
print (area_frame)
colors ={'yes':'red', 'no':'blue', 'Yes': 'red','No':'blue'}
start = dt.date(2022, 3,1)
end= dt.date(2023,7,1)


columnnamelist = ["Water Temperature (degrees C)","Salinity (ppt)", "O2 (mg/L)", "pH","NO3 (PPM)","PO4 (PPM)"]
temp = columnnamelist[0]
for anarea in area_frame:
    if anarea =='Other':
        print ("Other, break")
        continue
    for col in columnnamelist:
    
        areaframe = df[df['Area']==anarea]
        if areaframe.dropna().empty:
            print ("Empty frame "+ str(anarea))
            continue
        
        areaframe.set_index('Date',drop=False, inplace=True)
        red_tide_yes = areaframe[areaframe["Red tide ?"]=='Yes']
        print (red_tide_yes)
        
        gr = pd.Grouper(freq="1M")
        means = areaframe[col].groupby(gr).mean()
        vars =  areaframe[col].groupby(gr).std()
        print (vars)
        #print (anarea)
        
        print (means)
        
        
        print (gr)
        print (type(means))
        print (len(means))
        
        #print (areaframe)
        #print ( areaframe['Water Temperature (degrees C)'])
        titleString = "Area: " + anarea
        plt.title (titleString)
        ax = means.plot(yerr = vars, legend =False)     
        means.plot(style='s', label ='mean')
        areaframe[col].plot(style='+', label ='data points', color= areaframe["Red tide ?"].map(colors))
        try:
            red_tide_yes[col].plot(style='+', color = 'r',markersize = 15, label='Red tide')
        except:
            print ("No Red tide")
        #plt.scatter(areaframe["Date"], areaframe["Water Temperature (degrees C)"], c=areaframe["Red tide ?"].map(colors), label ='Water temperature')
        plt.xlabel("Date/Time")
        plt.gca().set_xbound(start,end)
        plt.ylabel(col)
        plt.legend()
#        plt.show()
        fileName = "Plot"+anarea.replace(" ", "")+"_"+col.replace(" ", "").replace("\\","").replace("/","")+".png"
        filePath = os.path.join(currentDir, fileName)
        print ("Saving to ")
        print (filePath)
        plt.savefig(filePath)
        plt.clf()
             
    






