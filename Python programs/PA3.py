# Author: Coadiey Bryan
# CLID: C00039405
# Course/Section: CMPS 150 – Section 003
# Assignment: pa4
# Date Assigned: Friday, September 29, 2017
# Date/Time Due: Friday, October 6, 2017 –- 11:55 pm
#
# Description: This program uses selection structures to determine cost of
# babysitting fees.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
#
#I know it was unnecessary to compute the minutes and not just hours but i wanted to challenge myself
#
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
''' 
   def __init__(self, defaultColor):
       self.myColor = defaultColor
'''
def getTotal(clockin, clockout):
    h1, m1 = clockin.split(':')
    h2, m2 = clockout.split(':')
    total=(int(h2) * 3600 + int(m2) * 60) - (int(h1) * 3600 + int(m1) * 60)
    return total 

def getTime(clockin, clockout):
    totaltime= getTotal(clockin, clockout)
    totalHours, secremain = divmod(totaltime, 3600)
    totalMinutes, seconds= divmod(secremain, 60)
    totalTimeForm = totalHours, totalMinutes
    return totalTimeForm  

def getAnswer(clockin, clockout):
    try:  
    #if they want the minutes and hours
        print()
        #time = getTime(clockin,clockout)
        #print("Total Time Clocked in Equals", time[0], time[1], sep=':')
        goodLookingTime = ":".join(["{:02d}".format(x) for x in getTime(clockin, clockout)])
        #print("Total Time Clocked In Equals", *getTime(clockin,clockout),sep=':')
        print("Total Time Clocked In Equals", goodLookingTime, sep=':')
        totalSec= getTotal(clockin,clockout)
        totalForWage= (totalSec/60)/60
        hours1, minutes1 = clockin.split(':')
        hours2,minutes2=clockout.split(':')
        nighthours = int(hours2)-21 if int(hours2) >= 21 else 0
        dayhours= (int(hours2)-int(hours1))-nighthours
        wageHoursOnly = nighthours* 5.00 + dayhours * 7.50
        wageMinutesOnly= totalForWage-(nighthours+ dayhours)
        wageNightMinutesOnly = int(minutes2)/ 60 if int(hours2) >=21 else 0
        wageMinutesOnly_=0
        wageMinutesOnly_ = wageMinutesOnly-wageNightMinutesOnly 
        afterHoursTimePay= nighthours*5.00 + wageNightMinutesOnly *5.00
        regularTimePay= dayhours*7.50 + wageMinutesOnly_*7.50
        if int(hours2) >=21 and int(hours1) >= 21:
            wage= totalForWage*5.00
        elif int (hours2) <21 and int(hours1) <21:
            wage= totalForWage*7.50
        else:
            wage = wageMinutesOnly_* 7.50 + wageHoursOnly + wageNightMinutesOnly*5.00
        reg=round(regularTimePay,2)
        after=round(afterHoursTimePay,2)
        wa=round(wage,2)
        print()
        if regularTimePay > 0.00:
            print("Regular Pay:       $", ( '{0:.2f}'.format(reg)))
        if afterHoursTimePay > 0.00:
            print("After Hours Pay:   $", ( '{0:.2f}'.format(after)))
        print("-------------------------------------------")
        print("Total Wage Earned: $", ( '{0:.2f}'.format(wa)))
    except ValueError:
    #if they dont want the money from their minutes on the clock
        hourOnlynighthours = int(clockout)-21 if int(clockout) > 21 else 0
        hourOnlydayhours= (int(clockout)-int(clockin))-hourOnlynighthours
        hours = int(clockout) - int(clockin)
        hourOnlydayandnightWage = hourOnlynighthours* 5.00 + hourOnlydayhours*7.50
        regularPay = hourOnlydayhours *7.50
        afterHoursPay = hourOnlynighthours * 5.00
        if int(clockout) >=21 and int(clockin) >= 21:
            hourOnlyWage= hours*5.00
        elif int (clockout) <21 and int(clockin) <21:
            hourOnlyWage= hours *7.50
        else:
            hourOnlyWage = hourOnlydayandnightWage
        print()
        print("Total Hours clocked In: ",hours, "hours")
        print()
        if regularPay >0:
            print("Regular Pay:       $",( '{0:.2f}'.format(regularPay)))
        if afterHoursPay > 0:    
            print("After Hours Pay:   $",( '{0:.2f}'.format(afterHoursPay)))
        print("-------------------------------------------")
        print("Total Wage Earned: $", ( '{0:.2f}'.format(hourOnlyWage)))
        print()
        print(color.DARKCYAN , "Try inputing exact time with hours AND minutes this time? Like so: '00:00' Now you try!", color.END)
if __name__ == "__main__":
    clockin =input("Enter starting time(24 hour clock): ")
    clockout = input("Enter end time(24 hour clock):      ")
    getAnswer(clockin, clockout)


