# Author: Coadiey Bryan
# CLID: C00039405
# Course/Section: CMPS 150 – Section 003
# Assignment: pa5
# Date Assigned: Monday, October 23, 2017
# Date/Time Due: Saturday, October 28, 2017 –- 11:55 pm
#
# Description: This program uses functions to read and process a input file;
#Hospital data
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
try:
    def roomCost(days,privateOrNot):
        return days*privateOrNot
    def roomType(typeSet,days):
        if typeSet == 'S':
            return roomCost(days,495)
        elif typeSet == 'P':
            return roomCost(days,750)    
    def cableCost(typeSet,days):
        if typeSet == 'Y':
            if 7.25*days >= 200:
                return 200
            else:
                return 7.50*days
        elif typeSet == 'N':
            return  0.00  
    def hospitalityCost(typeSet,days,roomtyp):
        if typeSet == 'Y' and roomtyp != 'P':
            if 6.00*days >=200:
                return 200
            else:
                return 6.00*days
        elif typeSet == 'N' or roomtyp == 'P':
            return  0.00  
    def headingVoidFunction(x,roomtyp,printStuff,stuff2,stuff3,stuff4):
        if x <= 1 and x != 0:
            print(" Name           Room Type       Cost       Cable  Hospitality Rm")
            print("------------------------------------------------------------------")
        elif x == 0:
            print("------------------------------------------------------------------")
            print("{0:31s}".format(printStuff),format(stuff2,'8.2f'),format(stuff3,'7.2f'),format(stuff4,'10.2f'))
        else:
            if roomtyp == 'P':
                private="Private"
            elif roomtyp =='S':
                private="Semi-Private"
            print("{0:15s}".format(printStuff),"{0:15s}".format(private), format(stuff2, '8.2f'),format(stuff3,'7.2f'),format(stuff4,'10.2f'))
    def main():
        file = open("hospitalData.py",'r')
        typ = file.readline().strip('\n')
        totalCost=0
        totalCable=0
        totalHospice=0
        x=1
        headingVoidFunction(x,1,1,1,1,1)
        while str(typ) != "END":   
            days = int(file.readline())
            roomtyp = str(file.readline().strip('\n'))
            cable = file.readline().strip('\n')
            hospice = file.readline().strip('\n')
            totalCost += roomType(roomtyp,days)
            totalCable += cableCost(cable,days)
            totalHospice += hospitalityCost(hospice,days,roomtyp)
            x +=x+1
            headingVoidFunction(x,roomtyp,typ,roomType(roomtyp,days),cableCost(cable,days),hospitalityCost(hospice,days,roomtyp))
            typ = file.readline().strip('\n')
        x=0
        empty=""
        totals= "Totals"
        headingVoidFunction(x,empty,totals,totalCost,totalCable,totalHospice)
        file.close()
    if __name__ == "__main__":
        main()
except ValueError:
    print("Invalid value for number of days in Hospital")