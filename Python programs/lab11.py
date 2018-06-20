# Author:       Coadiy Bryan 
# ID/Section:   C00039405/Sec.003
# Lab #11
import random
class Car():
    def __init__(self, symbolIn):
        self.location = 0
        self.symbol = symbolIn
    def MoveCar(self):
        self.location = self.location + random.randint(1,5)  
    def DisplayCar(self):
        if (self.location > 0):
            for i in range(self.location):
                print('*',end="")
            print(self.symbol)
        else:
            print(self.symbol)
    def GetLocation(self):
        return self.location
    def GetSymbol(self):
        return self.symbol
def main():
    #  This main function will create two cars 
    #  Then it will “race” them by moving them 5 times 
    myCar = Car("Nona")
    yourCar = Car("Coadiey")
    for i in range(5):
        # move and display the first car created
        print()
        myCar.MoveCar()
        yourCar.MoveCar()
        myCar.DisplayCar()
        yourCar.DisplayCar()
    print()
    if yourCar.GetLocation() > myCar.GetLocation():
        print("Coadiey Wins!")
    elif myCar.GetLocation() > yourCar.GetLocation():
        print("Nona Wins!")
    elif myCar.GetLocation() == yourCar.GetLocation():
        print("It's a Tie!")
    # determine which car “moved” farthest (location data member is larger)
    # and declare/print that is the “winner”
main()  
