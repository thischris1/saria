#!/usr/bin/python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import sys,os
df = pd.read_excel('data.xlsx')

data_top = df.head()
#print (data_top)


# find different areas
area_frame = df['Area'].unique()

colors ={'yes':'red', 'no':'blue', 'Yes': 'red','No':'blue'}

for anarea in area_frame:
    print (anarea)
    areaframe = df[df['Area']==anarea]
    print (areaframe)
    print ( areaframe['Water Temperature (degrees C)'])
    titleString = "Area: " + anarea
    plt.title (titleString)
    plt.scatter(areaframe["Date"], areaframe["Water Temperature (degrees C)"], c=areaframe["Red tide ?"].map(colors), label ='Water temperature')
    plt.xlabel("Date/Time")
    plt.ylabel("T [C]")
    #plt.show()
    fileName = anarea+"_temperature.png"
    plt.legend()
    plt.savefig(fileName)
    plt.clf()
    plt.title (titleString)
    plt.scatter(areaframe["Date"], areaframe["Salinity (ppt)"],c=areaframe["Red tide ?"].map(colors),label = "Salinity (ppt)")
    plt.ylabel("Salinity (ppt)")
    plt.xlabel("Date/Time")
    #plt.show()
    plt.legend()
    fileName = anarea+"_Salinity.png"
    plt.savefig(fileName)
    plt.clf()
    plt.title (titleString)
    plt.scatter(areaframe["Date"], areaframe["O2 (mg/L)"],c=areaframe["Red tide ?"].map(colors), label = "O2 (mg/L)")
    plt.ylabel("O2 (mg/L)")
    plt.xlabel("Date/Time")
    plt.legend()
    #plt.show()
    fileName = anarea+"_oxygen.png"
    plt.savefig(fileName)
    plt.clf()
             
    


sys.exit()

datum = df["Date"]
red_tide = df["Red tide ?"]
print (red_tide)
stickstoff = df["NO3 (PPM)"]

red_tide_yes = df[df["Red tide ?"]=='Yes']

print (len(red_tide_yes))
red_tide_no = df[df["Red tide ?"]=='No']
print (len(red_tide_no))


plt.title ("O2 (mg/L) over time")
plt.plot(red_tide_yes["Date"],red_tide_yes["O2 (mg/L)"],'o', color='Red', label ='Red Tide')
plt.plot(red_tide_no["Date"], red_tide_no["O2 (mg/L)"], 's',color='Blue', label ='No Red Tide')
plt.ylabel("O2 (mg/L)")
plt.xlabel("Date")
plt.legend()
plt.show()


plt.title ("NO3 over time")
plt.plot(red_tide_yes["Date"],red_tide_yes["NO3 (PPM)"],'o', color='Red', label ='Red Tide')
plt.plot(red_tide_no["Date"], red_tide_no["NO3 (PPM)"], 's',color='Blue', label ='No Red Tide')
plt.ylabel("NO3 (PPM)")
plt.xlabel("Date")
plt.legend()
plt.show()

plt.title ("PO4 (PPM) over time")
plt.plot(red_tide_yes["Date"],red_tide_yes["PO4 (PPM)"],'o', color='Red', label ='Red Tide')
plt.plot(red_tide_no["Date"], red_tide_no["PO4 (PPM)"], 's',color='Blue', label ='No Red Tide')
plt.ylabel("PO4 (PPM)")
plt.xlabel("Date")
plt.legend()
plt.show()


plt.title ("PO4 (PPM) vs NO3 over time")
plt.plot(red_tide_yes["NO3 (PPM)"],red_tide_yes["PO4 (PPM)"],'o', color='Red', label ='Red Tide')
plt.plot(red_tide_no["NO3 (PPM)"], red_tide_no["PO4 (PPM)"], 's',color='Blue', label ='No Red Tide')
plt.ylabel("PO4 (PPM)")
plt.xlabel("NO3 (PPM)")
plt.legend()
plt.show()


plt.title ("Salinity over time")
plt.plot(red_tide_yes["Date"],red_tide_yes["Salinity (ppt)"],'o', color='Red', label ='Red Tide')
plt.plot(red_tide_no["Date"], red_tide_no["Salinity (ppt)"], 's',color='Blue', label ='No Red Tide')
plt.ylabel("Salinity [ppt]")
plt.xlabel("Date")
plt.legend()
plt.show()

