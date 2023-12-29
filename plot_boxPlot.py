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
for col in columnnamelist:
    print ("Calculating mean and var of " + col)
    tempMean = df[col].mean()
    tempVar = df[col].var()
    print (col, tempMean, tempVar)
    meanDict[col]=[tempMean, tempVar]

print (meanDict)
#sys.exit()

temp = columnnamelist[0]

areaframe = df
for col in columnnamelist:
    
    for red in ['Yes','No']:
    
        
	    areaframe.set_index('Date',drop=False, inplace=True)
	    red_tide_yes = areaframe[areaframe["Red tide ?"]=='Yes']
	    red_tide_no = areaframe[areaframe["Red tide ?"]!='Yes']
	    #print (red_tide_yes)
		
	    gr = pd.Grouper(freq="1M")
	    means = areaframe[col].groupby(gr).mean()
	    vars =  areaframe[col].groupby(gr).std()
	    print (vars)
	    #print (anarea)

	    print (col)
	    print ("Mean")
	    print (means)
		
		
	    print (gr)
	    print (type(means))
	    print (len(means))
		
	    #print (areaframe)
	    #print ( areaframe['Water Temperature (degrees C)'])
	    colName = col.replace(" ","")
	    colName = colName.replace("(","-")
	    colName = colName.replace(")","")
	    colName= colName.replace("/","")
	    if red =='Yes':
	    	titleString = "Data - Red Tide " + col
	    	red_tide_yes.boxplot(column=[col])
	    	fileName = "BoxPlot_redTide_YES_"+colName+".png"
	    	
	    else:
	    	titleString =" Data No Red Tide " + col
	    	red_tide_no.boxplot(column=[col]) 
	    	fileName = "BoxPlot_redTide_NO_"+colName+".png"
	  
	    plt.title (titleString)
	    
	    filePath = os.path.join(currentDir, fileName)
	    print(filePath)
	    #plt.show()
	    plt.savefig(filePath)
	    
	    plt.clf()
             
    






