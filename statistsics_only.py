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

colors ={'yes':'red', 'no':'blue', 'Yes': 'red','No':'blue'}
start = "2019-09-08"
end= "2023-07-01"
columnnamelist = ["Water Temperature (degrees C)","Salinity (ppt)", "O2 (mg/L)", "pH","NO3 (PPM)","PO4 (PPM)"]
meanDict={}
varDict ={}

areaframe = df
for col in columnnamelist:
    print ("Calculating mean and var of " + col)
    tempMean = df[col].mean()
    tempVar = df[col].var()
    print (col + ": ALL Values Mean "+ str(tempMean)+"  Variance = " + str(tempVar))
   
    
    
    areaframe.set_index('Date',drop=False, inplace=True)
    red_tide_yes = areaframe[areaframe["Red tide ?"]=='Yes']
    red_tide_no = areaframe[areaframe["Red tide ?"]!='Yes']
    #print (red_tide_yes)
		
    gr = pd.Grouper(freq="1M")
    means = red_tide_yes[col].mean()
    vars =  red_tide_yes[col].std()
    print (col + ":  RED TIDE Mean "+ str(means)+"  Variance = " + str(vars))
	    
    means = red_tide_no[col].mean()
    vars =  red_tide_no[col].std()
    print (col + ":  NO RED TIDE Mean "+ str(means)+"  Variance = " + str(vars))  
	     
	    	
	  


