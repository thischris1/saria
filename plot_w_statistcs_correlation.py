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
red_tide_yes = df[df["Red tide ?"]=='Yes']

print(np.nanmean(df['PO4 (PPM)'].to_numpy()))
print ("Mean P04")

plt.title("All areas")
plt.plot(df['NO3 (PPM)'].to_numpy(), df['PO4 (PPM)'].to_numpy(),'o')
plt.plot(red_tide_yes['NO3 (PPM)'].to_numpy(), red_tide_yes['PO4 (PPM)'].to_numpy(),'o',color = 'Red', label ='Red tide')
plt.axhline(y=np.nanmean(df['PO4 (PPM)'].to_numpy()), ls='--', label ='PO4 mean')
plt.axvline(x= np.nanmean(df['NO3 (PPM)'].to_numpy()), ls='--',label ='NO3 mean')
plt.xlabel("NO3 (PPM)")
plt.ylabel("PO4 (PPM)")
plt.legend()
plt.show()

col='po4_over_no3'
fileName = "Plot_alldata"+"_"+col.replace(" ", "").replace("\\","").replace("/","")+".png"
filePath = os.path.join(currentDir, fileName)
print ("Saving to ")
print (filePath)
plt.savefig(filePath)
plt.cla()
red_tide_yes = df[df["Red tide ?"]=='Yes']
plt.title("All areas")
o2mean = np.nanmean(df['O2 (mg/L)'].to_numpy())

phmean = np.nanmean(df['pH'].to_numpy())
print (o2mean, phmean)
plt.plot(df['O2 (mg/L)'].to_numpy(), df['pH'].to_numpy(),'o')
plt.plot(red_tide_yes['O2 (mg/L)'].to_numpy(), red_tide_yes['pH'].to_numpy(),'o',color = 'Red', label ='Red tide')
plt.axvline(x=o2mean, ls='--', label = 'Mean O2')
plt.axhline(y=phmean, ls='-.',label='mean pH' )
plt.xlabel("O2 (mg/L)")
plt.ylabel("pH")
plt.legend()
plt.show()
col='ph_over_o2'
fileName = "Plot_allData_"+col.replace(" ", "").replace("\\","").replace("/","")+".png"
filePath = os.path.join(currentDir, fileName)
print ("Saving to ")
print (filePath)
plt.savefig(filePath)
plt.cla()
colors ={'yes':'red', 'no':'blue', 'Yes': 'red','No':'blue'}
start = "2019-09-08"
end= "2023-07-01"
columnnamelist = ["Water Temperature (degrees C)","Salinity (ppt)", "O2 (mg/L)", "pH","NO3 (PPM)","PO4 (PPM)"]
temp = columnnamelist[0]
col = columnnamelist[5]
for anarea in area_frame:
     
    areaframe = df[df['Area']==anarea]
    
        
    areaframe.set_index('Date',drop=False, inplace=True)
    red_tide_yes = areaframe[areaframe["Red tide ?"]=='Yes']
    print (red_tide_yes)
    
    gr = pd.Grouper(freq="1M")
   # means = areaframe[col].groupby(gr).mean()
   # vars =  areaframe[col].groupby(gr).std()
   # print (vars)
        
    #print (anarea)
        
   # print (means)
        
        
   # print (gr)
   # print (type(means))
   # print (len(means))
    oxygen = areaframe['O2 (mg/L)']
    phosphat = areaframe['PO4 (PPM)']
    nitrat = areaframe['NO3 (PPM)']
    pH =  areaframe['pH']
    oxredtide =  red_tide_yes['O2 (mg/L)']
    phredtide =  red_tide_yes['PO4 (PPM)']
    niredtide =  red_tide_yes['NO3 (PPM)']
    phredtide =  red_tide_yes['pH']
        
    #print (areaframe)
    #print ( areaframe['Water Temperature (degrees C)'])
    titleString = "Area: " + anarea
    plt.title (titleString)
    plt.plot(nitrat.to_numpy(), phosphat.to_numpy(),'o')
    plt.plot(niredtide.to_numpy(),phredtide.to_numpy(),'o', color = 'Red', label='Red tide') 
    plt.axhline(y=np.nanmean(phosphat.to_numpy()), ls='--', label ='PO4 mean')
    plt.axvline(x= np.nanmean(nitrat.to_numpy()) , ls='-.',label ='NO3 mean')
    plt.xlabel("NO3 (PPM)")
    plt.ylabel("PO4 (PPM)")
    plt.legend()
  #  plt.show()
    col='no3_over_po4'
    fileName = "Plot"+anarea.replace(" ", "")+"_"+col.replace(" ", "").replace("\\","").replace("/","")+".png"
    filePath = os.path.join(currentDir, fileName)
    print ("Saving to ")
    print (filePath)
    plt.savefig(filePath)
    plt.clf()
    plt.cla()
    titleString = "Area: " + anarea
    plt.title (titleString)
    plt.plot(oxygen.to_numpy(), pH.to_numpy(),'o')
    plt.plot(oxredtide.to_numpy(), phredtide.to_numpy(),'o', color='Red', label='Red tide')
    plt.axvline(x=np.nanmean(oxygen), ls='--', label = 'Mean O2')
    plt.axhline(y=np.nanmean(pH), ls='-.',label='mean pH' )
    plt.xlabel("O2 (mg/L)")
    plt.ylabel("pH")
    plt.legend()
   # plt.show()
    col='ph_over_o2'
    fileName = "Plot"+anarea.replace(" ", "")+"_"+col.replace(" ", "").replace("\\","").replace("/","")+".png"
    filePath = os.path.join(currentDir, fileName)
    print ("Saving to ")
    print (filePath)
    plt.savefig(filePath)
    plt.clf()
    plt.cla()
    continue


sys.exit()
fileName = "Plot"+anarea.replace(" ", "")+"_"+col.replace(" ", "").replace("\\","").replace("/","")+".png"
filePath = os.path.join(currentDir, fileName)
print ("Saving to ")
print (filePath)
plt.savefig(filePath)
plt.clf()
             
    






