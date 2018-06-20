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
from PA3 import color
'''
b = color(color.BLUE)
c = color(color.CYAN)


print(b.myColor)
print(c.myColor)
print(d.myColor)
'''
name1 = (color.END+color.UNDERLINE +"Maddison's Market"+color.END+color.DARKCYAN)
name2 = (color.END+"Everything You Need"+color.DARKCYAN)
print(color.DARKCYAN+"+----------------------------------------+")
print("+                                        +")
print("+           {0}            +".format(name1))
print("+          {0}           +".format(name2))
print("+                                        +")
print("+            October 15, 2017            +")
print("+                                        +")
print("+----------------------------------------+",color.END)

file = open("fuel.py",'r')

typeSet=file.readline().strip('\n')

def looper(typeSet):
    return typeSet != 'X'
produce=0
totalC =0
totalH =0
totalO =0
totalT =0
nonTaxC =0
nonTaxH =0
nonTaxO =0
nonTax =0
produceTax =0
while looper(typeSet):
    numberSet= eval(file.readline())  
    if typeSet == 'C':
        item = "Clothes"
        tax = numberSet*.085
        nonTaxC +=tax
        price = numberSet+tax
        totalC += numberSet
    elif typeSet == 'P':
        item = "Produce"
        foodTax = numberSet*.085
        produceTax +=foodTax
        price = numberSet+foodTax
        produce += numberSet
    elif typeSet == 'H':
        item = "Hardware"
        tax = numberSet*.085
        nonTaxH +=tax
        price = numberSet+tax
        totalH += numberSet
    elif typeSet == 'O':
        item = "Other"
        tax = numberSet*.085
        nonTaxO +=tax
        price = numberSet+tax
        totalO += numberSet
    else:
        item = "try"
        price = numberSet
        totalT +=price
    
    print("     {0:20s}".format(item), format(price, '7.2f'))
    typeSet=file.readline().strip('\n')
nonTotal = totalT +totalO + totalC +totalH
nonTax= nonTaxO + nonTaxH + nonTaxC
total = produce + nonTotal + produceTax + nonTax
print("+----------------------------------------+")
print("     Subtotal (food){0:5s}".format(""), format(produce, '7.2f'))
print("     Subtotal (non-food){0:2s}".format(""), format(nonTotal, '7.2f'))
print("     Tax (food){0:9s}".format(""), format(produceTax, '7.2f'))
print("     Tax (non-food){0:5s}".format(""), format(nonTax, '7.2f'))
print("+----------------------------------------+")
print("     Total{0:16s}".format(""), format(total, '7.2f'))
file.close()      

    