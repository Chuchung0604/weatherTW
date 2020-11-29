# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:30:12 2020

@author: user
"""
# 2,33,61,92,122,152,183,214,245,275,306,336,366

def sumRange(rainList):
# return sum value of input list    
    rainSum = 0
    for r in rainList:
        if float(r) == -99.9:
            return -99.9
            break        
        else:
            dayRain = float(r)
        rainSum += dayRain
        
    return round(rainSum,3)



def sumMonth(day):
# monthly sumary, originally ued for precipitation
    jan = sumRange(day[2:33])
    feb = sumRange(day[33:61])
    mar = sumRange(day[62:92])
    apr = sumRange(day[92:122])
    may = sumRange(day[122:152])
    jun = sumRange(day[152:183])
    jul = sumRange(day[183:214])
    aug = sumRange(day[214:245])
    sep = sumRange(day[245:275])
    octo = sumRange(day[275:306])
    nov = sumRange(day[306:336])
    dec = sumRange(day[336:367])
    
    return [day[0],day[1],jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov,dec]

def avgRange(daylist):
    # return average value of input list
    Tsum = 0
    number= 0
    for d in daylist:
        # remove the value - 99
        if float(d) < 0:
            dayTemp = -99.9
        else:
            dayTemp = float(d)
        Tsum += dayTemp
        number += 1
    return Tsum/number


def avgMonth(day):

    jan = avgRange(day[2:33])
    feb = avgRange(day[33:61])
    mar = avgRange(day[61:92])
    apr = avgRange(day[92:122])
    may = avgRange(day[122:152])
    jun = avgRange(day[152:183])
    jul = avgRange(day[183:214])
    aug = avgRange(day[214:245])
    sep = avgRange(day[245:275])
    octo = avgRange(day[275:306])
    nov = avgRange(day[306:336])
    dec = avgRange(day[336:367])
    return [day[0],day[1],jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]

# 2,33,61,92,122,152,183,214,245,275,306,336,366
def Monthfreq(day):
    jan = heavyRainSum(day[2:33])
    feb = heavyRainSum(day[33:61])
    mar = heavyRainSum(day[61:92])
    apr = heavyRainSum(day[92:122])
    may = heavyRainSum(day[122:152])
    jun = heavyRainSum(day[152:183])
    jul = heavyRainSum(day[183:214])
    aug = heavyRainSum(day[214:245])
    sep = heavyRainSum(day[245:275])
    octo = heavyRainSum(day[275:306])
    nov = heavyRainSum(day[306:336])
    dec = heavyRainSum(day[336:367])
    
    return [day[0],day[1],jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]


def heavyRain(row):
    # if the precipitation of certain day >= 80 the day become 1
    # return a heavy rain list
    # the definition of heavy rain is daily precipitatin more than 80 mm
    threashold = 80
    heavy = 0
    returnlist = [row[0],row[1]] # lon, lat

    daylist = row[2:367] # all the year
    for i in daylist:
        if float(i) == -99.9:
            heavy = -99.9
        elif float(i) > threashold:
            heavy = 1
        else:
            heavy = 0
        returnlist.append(heavy)
      
    return returnlist

def heavyRainSum(row):
    # add number of days in a range of day that precipitation move than threashold
    # return numbers of heavy rain days in a grid
    threashold = 80
    dayno = 0
    for r in row:
        if float(r) == -99.9:
            return -99.9
            break

        elif float(r) >= threashold:
            dayno += 1
    return dayno
        
    

def addTwoYear(y1,y2):
    # add the day value of day list of each year
    returnList = [y1[0],y2[1]]
    for d in range(2,367):
        day = float(y1[d]) + float(y2[d])
        returnList.append(day)
    return returnList

def addTwoMonthly(m1,m2):
    returnList = [m1[0],m2[1]]
    for d in range(2,14):
        day = float(m1[d]) + float(m2[d])
        returnList.append(day)
    return returnList