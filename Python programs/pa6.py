# Author: Coadiey Bryan
# CLID: C00039405
# Course/Section: CMPS 150 – Section 003
# Assignment: pa6
# Date Assigned: Wendsday, November 8, 2017
# Date/Time Due: Saturday, November 11, 2017 –- 11:55 pm
#
# Description: This program uses functions to perform multiple operations and process different types of files in different ways
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
def summer(file):
    read = int(file.readline())
    tot = 0
    while read != 0:
        tot = read + tot
        read = int(file.readline())
    print("Sum of numbers within file : ", tot)
    #return tot
def maxMin(file):
    #filename = input("Enter the name of your input file: ")
    #file = open(filename,'r')
    readArray = int(file.readline())
    ma = readArray
    mi = readArray
    while readArray != 0:
        if readArray > ma:
            ma = readArray
        if readArray < mi:
            mi = readArray
        readArray= int(file.readline())
    print("Maximum in file: ", ma)
    print("Minimum in file: ", mi)
def vowels(file):
#shortened way thanks to dictionaries
    readLine = str(file.read(1))
    letters = {"a":0,"e":0,"i":0,"o":0,"u":0}
    Go = 0
    while Go < 3:
        if readLine.lower() in letters:
            letters[readLine.lower()] += 1
        elif readLine == "#":
            Go += 1
        readLine = str(file.read(1))
    for k,v in letters.items():
        print(k,"=",v,end=" ")
    '''
#regular long way to complete function   
    summ = 0
    stop = 0
    A = 0
    a = 0
    E = 0
    e = 0
    I = 0
    i = 0
    O = 0
    o = 0
    U = 0
    u = 0
    while stop < 3:
        if readLine == "A":
            A += 1
            summ += 1
        elif readLine == "a":
            a += 1
            summ += 1
        elif readLine == "E" :
            E += 1
            summ += 1
        elif readLine == "e" :
            e += 1
            summ += 1
        elif readLine == "I" :
            I += 1
            summ += 1
        elif readLine == "i":
            i += 1
            summ += 1
        elif readLine == "O" :
            O += 1
            summ += 1
        elif readLine == "o" :
            o += 1
            summ += 1
        elif readLine == "U":
            U += 1
            summ += 1
        elif readLine == "u":
            u += 1
            summ += 1
        elif readLine == "#":
            stop = stop + 1
        else:
            summ += 0
        readLine = str(file.read(1).strip('\n'))
    existence("A",A),existence("a",a),existence("E",E),existence("e",e),existence("I",I),existence("i",i),existence("O",O),existence("o",o),existence("U",U),existence("u",u)
    print()
    #print("A = {0} a = {1} E = {2} e = {3} I = {4} i = {5} O = {5} o = {6} U = {7} u = {8}".format(A,a,E,e,I,i,O,o,U,u))
def existence(v,i):
    if i >= 1:
        print("{0} = {1}".format(v,i), end = " ")
      '''  
def evenOrOdd(file):
    evenSum = 0
    oddSum = 0
    #filename = input("Enter the name of your input file: ")
    #file = open(filename,'r')
    read = int(file.readline())
    while read != 0:     
        if read % 2 == 0:
            even = 1
            evenSum += even
        else:
            odd = 1
            oddSum += odd
        read = int(file.readline()) 
    print("Number of Even Numbers In the File: ", evenSum)
    print("Number of Odd Numbers In the File:  ", oddSum)
def main():
#using a dictionary
    option = input("1. Sum Numbers In A File\n2. Find Max/Min In A File\n3. Count Vowels In A File\n4. Count Even/Odd Numbers In A File\n5. Quit\n\nPlease enter file type: ") 
    bigDictionary = {'1':summer,'2':maxMin,'3':vowels,'4':evenOrOdd}
    if int(option) < 5 and int(option) > 0:
        filename = input("Enter the name of your input file: ")
        infile = open(filename,'r')
        go = int(option)
        while go < 5 or go > 0:
            if option in bigDictionary:
                bigDictionary[option](infile)
            elif go == 5:
                break
            else:
                print("Not a file type")
                break
            infile.close()
            option = input("1. Sum Numbers In A File\n2. Find Max/Min In A File\n3. Count Vowels In A File\n4. Count Even/Odd Numbers In A File\n5. Quit\n\nPlease enter file type: ")
            go = int(option)        
            filename = input("Enter the name of your input file: ")
            infile = open(filename,'r')     
        print("GoodBye!")
    elif int(option) > 5 or int(option) <= 0:
        print("Not a file type")
    else:
        print("Well Alright Then? GoodBye!")
#regular way to complete assignment
    '''
        if option == '1':
            filename = input("Enter the name of your input file: ")
            infile = open(filename,'r')
            print("Sum of numbers within file : ", summer(infile))
        elif option == "2":
            maxMin()
        elif option == "3":
            filename = input("Enter the name of your input file: ")
            infile = open(filename,'r')
            vowels(infile)
        elif option == "4":
            evenOrOdd()
        elif option == "5":
            print("GoodBye!")
            Go = False
            break
        else:
            print("Input Error try again")
        option = input("1. Sum Numbers In A File\n2. Find Max/Min In A File\n3. Count Vowels In A File\n4. Count Even/Odd Numbers In A File\n5. Quit\n\nPlease enter file type: ") 
'''
if __name__ == '__main__':
    main()
