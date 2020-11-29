# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:06:13 2020

@author: Chuchung
"""
import csv
import weather 
import numpy as np

# for file name
location = ["北部","中部","南部","東部"]
yearList = range(1961,2019) 
#filename = 'tccip/觀測_日資料_東部_降雨量_1960.csv'
#oldYearList = [0]*2
thisY = []
header = ["lon","lat","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# write yearly average
def yearly():
    
    for y in yearList:
        writename = "History/觀測_日資料_降雨量_%d.csv" %(y)
        with open(writename, 'w', newline='') as csvwrite:
            writer = csv.writer(csvwrite, delimiter=',')
            writer.writerows([header])
            
            for l in location:
                filename = "tccip/觀測_日資料_%s_降雨量_%d.csv " %(l,y)
                with open(filename,newline='') as csvfile:
                    wea = csv.reader(csvfile,delimiter=',')
                    next(wea) #skip header
                    for row in wea:
                            thisgrid = weather.sumMonth(row)
                            writer.writerows([thisgrid])
                            csvfile.close()
        print("write %d done" %y)


# write 
def heavyRainMonth():
    for y in yearList:
        writename = "大雨/觀測_日資料_大雨_%d.csv" %(y)
        print("read year=",y)
        with open(writename, 'w',newline='') as csvwrite:
            writer = csv.writer(csvwrite, delimiter=',')
            writer.writerow(header)
            for l in location:
                filename = "tccip/觀測_日資料_%s_降雨量_%d.csv " %(l,y)
                with open(filename,newline='') as csvfile:
                    wea = csv.reader(csvfile,delimiter=',')
                    next(wea) #skip header
                    for row in wea:
                        thisgrid = weather.Monthfreq(row)
                        writer.writerows([thisgrid])
                csvfile.close()

def medianrain():
    
    yearjan, yearfeb, yearmar, yearapr, yearmay, yearjun = ([] for i in range(6))
    yearjul, yearaug, yearsep, yearocto, yearnov, yeardec = ([] for i in range(6))

    yearcounter = 0
    for y in yearList:
        filename = "History/觀測_日資料_降雨量_%d.csv" %y
        
        with open(filename, newline='') as csvread:
            wea = csv.reader(csvread, delimiter=',')
            next(wea) # skip header

            gridcounter = 0
            lon,lat= ([] for i in range(2))
            jan,feb,mar,apr,may,jun = ([] for i in range(6))
            jul,aug,sep,octo,nov,dec = ([] for i in range(6))
            for row in wea:
                #把每一個grid append在list裡面
                lon.append(row[0])
                lat.append(row[1])
                jan.append(row[2])
                feb.append(row[3])
                mar.append(row[4])
                apr.append(row[5])
                may.append(row[6])
                jun.append(row[7])
                jul.append(row[8])
                aug.append(row[9])
                sep.append(row[10])
                octo.append(row[11])
                nov.append(row[12])
                dec.append(row[13])                
                gridcounter += 1
                
        yearjan.append(jan)
        yearfeb.append(feb)
        yearmar.append(mar)
        yearapr.append(apr)
        yearmay.append(may)
        yearjun.append(jun)
        yearjul.append(jul)
        yearaug.append(aug)
        yearsep.append(sep)
        yearocto.append(octo)
        yearnov.append(nov)
        yeardec.append(dec)
        yearcounter += 1
        

      #  print(y)
        # read done
        csvread.close()
    with open("Precip_median.csv", 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter=',')
        writer.writerow(header)
        for g in range(gridcounter):
            janAllYear, febAllYear, marAllYear = ([] for i in range(3))
            aprAllYear, mayAllYear, junAllYear = ([] for i in range(3))
            julAllYear, augAllYear, sepAllYear = ([] for i in range(3))
            octAllYear, novAllYear, decAllYear = ([] for i in range(3))
            for y in range(yearcounter):
             #   print("year =", y)
                janAllYear.append(float(yearjan[y][g]))
                febAllYear.append(float(yearfeb[y][g]))
                marAllYear.append(float(yearmar[y][g]))
                aprAllYear.append(float(yearapr[y][g]))
                mayAllYear.append(float(yearmay[y][g]))
                junAllYear.append(float(yearjun[y][g]))
                julAllYear.append(float(yearjul[y][g]))
                augAllYear.append(float(yearaug[y][g]))
                sepAllYear.append(float(yearsep[y][g]))
                octAllYear.append(float(yearocto[y][g]))
                novAllYear.append(float(yearnov[y][g]))
                decAllYear.append(float(yeardec[y][g]))
                
                
  
            jan = round(np.median(janAllYear),3)
            feb = round(np.median(febAllYear),3)
            mar = round(np.median(marAllYear),3)
            apr = round(np.median(aprAllYear),3)
            may = round(np.median(mayAllYear),3)
            jun = round(np.median(junAllYear),3)
            jul = round(np.median(julAllYear),3)
            aug = round(np.median(augAllYear),3)
            sep = round(np.median(sepAllYear),3)
            octo = round(np.median(octAllYear),3)
            nov = round(np.median(novAllYear),3)
            dec = round(np.median(decAllYear),3)
                
            writer.writerow([lon[g],lat[g],jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec])

def medianHeavyRain():
    
    yearjan, yearfeb, yearmar, yearapr, yearmay, yearjun = ([] for i in range(6))
    yearjul, yearaug, yearsep, yearocto, yearnov, yeardec = ([] for i in range(6))

    yearcounter = 0
    for y in yearList:
        filename = "大雨/觀測_日資料_大雨_%d.csv" %y
        print("Read Year ",y)
        
        with open(filename, newline='') as csvread:
            wea = csv.reader(csvread, delimiter=',')
            next(wea) # skip header

            gridcounter = 0
            lon,lat= ([] for i in range(2))
            jan,feb,mar,apr,may,jun = ([] for i in range(6))
            jul,aug,sep,octo,nov,dec = ([] for i in range(6))
            for row in wea:
                #把每一個grid append在list裡面
                lon.append(row[0])
                lat.append(row[1])
                jan.append(row[2])
                feb.append(row[3])
                mar.append(row[4])
                apr.append(row[5])
                may.append(row[6])
                jun.append(row[7])
                jul.append(row[8])
                aug.append(row[9])
                sep.append(row[10])
                octo.append(row[11])
                nov.append(row[12])
                dec.append(row[13])                
                gridcounter += 1
                
        yearjan.append(jan)
        yearfeb.append(feb)
        yearmar.append(mar)
        yearapr.append(apr)
        yearmay.append(may)
        yearjun.append(jun)
        yearjul.append(jul)
        yearaug.append(aug)
        yearsep.append(sep)
        yearocto.append(octo)
        yearnov.append(nov)
        yeardec.append(dec)
        yearcounter += 1
        
        # read done
        csvread.close()
    with open("Heavy Rain median.csv", 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter=',')
        writer.writerow(header)
        for g in range(gridcounter):
            janAllYear, febAllYear, marAllYear = ([] for i in range(3))
            aprAllYear, mayAllYear, junAllYear = ([] for i in range(3))
            julAllYear, augAllYear, sepAllYear = ([] for i in range(3))
            octAllYear, novAllYear, decAllYear = ([] for i in range(3))
            for y in range(yearcounter):
                janAllYear.append(float(yearjan[y][g]))
                febAllYear.append(float(yearfeb[y][g]))
                marAllYear.append(float(yearmar[y][g]))
                aprAllYear.append(float(yearapr[y][g]))
                mayAllYear.append(float(yearmay[y][g]))
                junAllYear.append(float(yearjun[y][g]))
                julAllYear.append(float(yearjul[y][g]))
                augAllYear.append(float(yearaug[y][g]))
                sepAllYear.append(float(yearsep[y][g]))
                octAllYear.append(float(yearocto[y][g]))
                novAllYear.append(float(yearnov[y][g]))
                decAllYear.append(float(yeardec[y][g]))
                
            jan = round(np.median(janAllYear),3)
            feb = round(np.median(febAllYear),3)
            mar = round(np.median(marAllYear),3)
            apr = round(np.median(aprAllYear),3)
            may = round(np.median(mayAllYear),3)
            jun = round(np.median(junAllYear),3)
            jul = round(np.median(julAllYear),3)
            aug = round(np.median(augAllYear),3)
            sep = round(np.median(sepAllYear),3)
            octo = round(np.median(octAllYear),3)
            nov = round(np.median(novAllYear),3)
            dec = round(np.median(decAllYear),3) 
            writer.writerow([lon[g],lat[g],jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec])
            # end of this function


def QuantileHeavyRain(qvalue):
    # 還要修改outputname
    writename = "Heavy Rain_%f.csv" %qvalue
    yearjan, yearfeb, yearmar, yearapr, yearmay, yearjun = ([] for i in range(6))
    yearjul, yearaug, yearsep, yearocto, yearnov, yeardec = ([] for i in range(6))

    yearcounter = 0
    for y in yearList:
        filename = "大雨/觀測_日資料_大雨_%d.csv" %y
        print("Read Year ",y)
        
        with open(filename, newline='') as csvread:
            wea = csv.reader(csvread, delimiter=',')
            next(wea) # skip header

            gridcounter = 0
            lon,lat= ([] for i in range(2))
            jan,feb,mar,apr,may,jun = ([] for i in range(6))
            jul,aug,sep,octo,nov,dec = ([] for i in range(6))
            for row in wea:
                #把每一個grid append在list裡面
                lon.append(row[0])
                lat.append(row[1])
                jan.append(row[2])
                feb.append(row[3])
                mar.append(row[4])
                apr.append(row[5])
                may.append(row[6])
                jun.append(row[7])
                jul.append(row[8])
                aug.append(row[9])
                sep.append(row[10])
                octo.append(row[11])
                nov.append(row[12])
                dec.append(row[13])                
                gridcounter += 1
                
        yearjan.append(jan)
        yearfeb.append(feb)
        yearmar.append(mar)
        yearapr.append(apr)
        yearmay.append(may)
        yearjun.append(jun)
        yearjul.append(jul)
        yearaug.append(aug)
        yearsep.append(sep)
        yearocto.append(octo)
        yearnov.append(nov)
        yeardec.append(dec)
        yearcounter += 1
        
        # read done
        csvread.close()
    with open(writename, 'w', newline='') as csvwrite:
        writer = csv.writer(csvwrite, delimiter=',')
        writer.writerow(header)
        for g in range(gridcounter):
            janAllYear, febAllYear, marAllYear = ([] for i in range(3))
            aprAllYear, mayAllYear, junAllYear = ([] for i in range(3))
            julAllYear, augAllYear, sepAllYear = ([] for i in range(3))
            octAllYear, novAllYear, decAllYear = ([] for i in range(3))
            for y in range(yearcounter):
                janAllYear.append(float(yearjan[y][g]))
                febAllYear.append(float(yearfeb[y][g]))
                marAllYear.append(float(yearmar[y][g]))
                aprAllYear.append(float(yearapr[y][g]))
                mayAllYear.append(float(yearmay[y][g]))
                junAllYear.append(float(yearjun[y][g]))
                julAllYear.append(float(yearjul[y][g]))
                augAllYear.append(float(yearaug[y][g]))
                sepAllYear.append(float(yearsep[y][g]))
                octAllYear.append(float(yearocto[y][g]))
                novAllYear.append(float(yearnov[y][g]))
                decAllYear.append(float(yeardec[y][g]))
                
            jan = round(np.quantile(janAllYear,qvalue),3)
            feb = round(np.quantile(febAllYear,qvalue),3)
            mar = round(np.quantile(marAllYear,qvalue),3)
            apr = round(np.quantile(aprAllYear,qvalue),3)
            may = round(np.quantile(mayAllYear,qvalue),3)
            jun = round(np.quantile(junAllYear,qvalue),3)
            jul = round(np.quantile(julAllYear,qvalue),3)
            aug = round(np.quantile(augAllYear,qvalue),3)
            sep = round(np.quantile(sepAllYear,qvalue),3)
            octo = round(np.quantile(octAllYear,qvalue),3)
            nov = round(np.quantile(novAllYear,qvalue),3)
            dec = round(np.quantile(decAllYear,qvalue),3) 
            writer.writerow([lon[g],lat[g],jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec])
            # end of this function
            
QuantileHeavyRain(.90)