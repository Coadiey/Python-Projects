'''
# Author:       Coadiey
# CLID/Section: C00039405/sec.003
# Lab #7
inFile = open("fuel.py", mode="r")
p = inFile.readlines()
stripped = []
stripped = [p[i].strip('\n') for i in p]
print(stripped)


def letterFile(i, x):
    description= str("a")
    ppg = 0
    price = 0
    while x != 30:
        for p in range(30):
            x == x+1
            counts = x%2
            if counts == 0:
                output = i
            else:
                price = eval(i)
            if output == str("S"):
                    ppg= price/2.62
                    description= str("Super Unleaded")
            elif output == str("P"):
                    ppg = price/2.36
                    description= str("Unleaded Plus")
            elif output == str("R"):
                    ppg = price/2.12
                    description= str("Regular Unleaded")
            elif output == str("D"):
                    ppg = price/2.35
                    description = str("Diesel")
            print(format(description,'20s'),format(ppg,'7.2f'),format(price,'8.2f'))
        return x

if __name__ =="__main__":
inFile = open("fuel.py", mode="r")
p = inFile.readlines(30).strip('\n')
print(p)
    count = letterFile(count, p)
    print()
    print("    Fuel Type        Gallons     Bill")
    print("-------------------------------------")  
    inFile.close()


# this is a count-controlled loop
              

    # read and process data 
 
 

    # print each line of output
'''
infile = open("fuel.py",'r')

print()
print("    Fuel Type        Gallons     Bill")
print("-------------------------------------")  

for i in range(15):

   fuelType = infile.readline().strip()
   gallons = eval(infile.readline())
  
   if fuelType == 'S':
        word = "Super Unleaded"
        bill = gallons * 2.62
   elif fuelType == 'P':
      word = "Unleaded Plus"
      bill = gallons * 2.36
   elif fuelType == 'R':
      word = "Regular Unleaded"
      bill = gallons * 2.12
   else:
      word = "Diesel"
      bill = gallons * 2.35

   print(format(word,'20s'),format(gallons,'7.2f'),format(bill,'8.2f'))

   
infile.close()




