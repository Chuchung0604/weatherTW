# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:06:13 2020

@author: Chuchung
"""
import csv
import rain

# for file name
location = ["北部","中部","南部","東部"]
template = 'tccip/觀測_日資料_東部_降雨量_'
t2 = '.csv'
filename = 'tccip/觀測_日資料_東部_降雨量_1960.csv'
oldYearList = []
thisY = []

with open(filename, newline='') as csvfile:

  wea = csv.reader(csvfile,delimiter=',')
  next(wea) # skip title
  for row in wea:
      # oldYearList.append(rain.heavyRain(row))
      oldYearList.append(rain.Monthfreq(row))
      
#filename = 'tccip/觀測_日資料_中部_降雨量_1961.csv'
yearList = range(1961,2018)

for y in yearList:
    filename = template + str(y) + t2
    
    with open(filename, newline='') as csvfile:

        wea = csv.reader(csvfile,delimiter=',')
        next(wea) # skip title
        counter = 0
        for row in wea:
            oldYear = oldYearList[counter]
            #thisY = rain.heavyRain(row)
            thisY = rain.Monthfreq(row)
            oldYear = rain.addTwoMonth(oldYear,thisY)
            #print(oldYear)
            oldYearList[counter] = oldYear
            counter += 1
            
# for row in oldYearList:
#     print(row)


with open("east.csv",'w',newline='') as csvwrite:
    writer = csv.writer(csvwrite, delimiter = ',')

    for r in oldYearList:
        writer.writerow(r)