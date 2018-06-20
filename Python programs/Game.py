# Author: Coadiey Bryan
# CLID: C00039405
# Course/Section: CMPS 150 – Section 003
# Assignment: Game Extra Credit
#
# Description: 
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
import random
def rndNum():
    return random.randrange(0,100)
def location(userInput):
    #dic = {userInput: }
    pass
class Character():
    def __init__(self,location = (0,0), name = 'Enemy', race = 'Evil Race', health = 100, attack = rndNum(), defense = rndNum(), gold = 0, armorStatTotal = 0, armorStatNumber = 0, weaponStatTotal = 0, weaponStatNumber = 0):
        self.__location = location
        self.__name = name
        self.__race = race
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        self.__gold = gold
        self.__armorStatTotal = armorStatTotal
        self.__armorStatNumber = armorStatNumber
        self.__weaponStatTotal = weaponStatTotal
        self.__weaponStatNumber = weaponStatNumber
        self.__movedDirection = (0,0)
    def getLocation(self):
        return self.__location
    def getName(self):
        return self.__name
    def getRace(self):
        return self.__race
    def getHealth(self):
        return self.__health
    def getAttack(self):
        return self.__attack
    def getDefense(self):
        return self.__defense
    def getGold(self):
        return self.__gold
    def getArmorStatTotal(self):
        return self.__armorStatTotal
    def getArmorStatNumber(self):
        return self.__armorStatNumber
    def getWeaponStatTotal(self):
        return self.__weaponStatTotal
    def getWeaponStatNumber(self):
        return self.__weaponStatNumber

    def setHealth(self,health):
        self.__health = health
    def setAttack(self,attack):
        self.__attack = attack
    def setDefense(self,defense):
        self.__defense = defense
    def setGold(self,gold):
        self.__gold = gold
    def setArmorStatTotal(self,armorStatTotal):
        self.__armorStatTotal = armorStatTotal
    def setArmorStatNumber(self,armorStatNumber):
        self.__armorStatNumber = armorStatNumber
    def setWeaponStatTotal(self,weaponStatTotal):
        self.__weaponStatTotal = weaponStatTotal
    def setWeaponStatNumber(self,weaponStatNumber):
        self.__weaponStatNumber = weaponStatNumber
    def combat(self,other):
        if random.getrandbits(1) == 0:
            attacker,defender = self,other 
        else:
            attacker, defender = other,self           

        while attacker.__health > 0 and defender.__health > 0:
            attack = attacker.__attack * round(random.random())
            defend = defender.__defense * round(random.random()) 
            defenseResult = defend - attack
            if defenseResult <= 0: 
                result = defender.__health + defenseResult
                defender.__health = result
                defender, attacker = attacker, defender 
                print(" {0}  health is at {1} after that attack".format(attacker.__name, attacker.__health))
            else: 
                defender, attacker = attacker, defender
                print(" {0}  defense is at {1} after that attack".format(attacker.__name, defenseResult))
            
    def moveBy(self,dx,dy):
        x,y = self.getLocation()                #x,y = other.getLocation()
        self.__location = (x+dx,y+dy)                                  #other.setLocation(x+dx,y+dy)
        self.__movedDirection = (dx,dy)                                  #self.__moveDirection = (dx,dy)
    def movedDirection(self):
        return self.__movedDirection

    def doYourThing(self,other):
        self.__movedDirection = (0,0)
        stopLoop = True
        choice = str(input('Do you want to fight, bribe, or run? '))
        while choice.lower() != 'q' and stopLoop:
            lis = [1,-1,0]
            dx = random.choice(lis)
            dy = random.choice(lis)
            #if any movement, trigger flag with (dx,dy)
            if choice.lower() == 'run':
              self.moveBy(dx,dy) 
              stopLoop = False
              #x,y = other.getLocation()
              #other.setLocation(x+dx,y+dy)
              #self.__moveDirection = (dx,dy)
            elif choice.lower() == 'bribe':
                    bribe = int(input('How much do you want to bribe? '))
                    if other.__gold > 0:
                        while bribe > other.__gold:
                            bribe = int(input('How much do you want to bribe, and CAN bribe? '))
                    else:
                        print("You don't have any gold to bribe with...")
                        choice = str(input('Do you want to fight, bribe, or run? '))
                        continue
                    if bribe > random.randrange(1,100):
                        other.__gold - bribe
                        self.moveBy(dx,dy)
                        #self.location += dx,dy
                        stopLoop = False
                    else:
                        print('You think you can just pay me off?..Pff?! Think again buddy!')
                        stopLoop = True
            elif choice.lower() == 'fight':
                self.__movedDirection = (0,0)
                other.combat(self)
                stopLoop = False
            else:
                choice = str(input('Do you want to FIGHT, BRIBE, or RUN? '))
                
                
class Chest():
    def __init__(self, health = bool(random.getrandbits(1)), armor = bool(random.getrandbits(1)), gold = bool(random.getrandbits(1)), weapon = bool(random.getrandbits(1))):
        self.__health = health
        self.__armor = armor
        self.__gold = gold
        self.__weapon = weapon
    def getHealth(self):
        if self.__health == True:
            return rndNum()
    def getArmor(self):
        if self.__armor == True:
            return rndNum()
    def getGold(self):
        if self.__gold == True:
            return rndNum()
    def getWeapon(self):
        if self.__weapon == True:
            return rndNum()
    def movedDirection(self):
        return (0,0)
    def doYourThing(self,mainCharacter):
        chestInteraction = str(input("Do you want to open the chest? "))
        if chestInteraction.lower() == 'yes':
            if self.__armor:
                armorPrevStatNum = mainCharacter.getArmorStatNumber()
                armorStatNum = 1 + armorPrevStatNum
                mainCharacter.setArmorStatNumber(armorStatNum)
                armorPrevStatTot = mainCharacter.getArmorStatTotal()
                armorStatTot = self.__armor + armorPrevStatTot
                mainCharacter.setArmorStatTotal(armorStatTot)
                Chest(health = 0, armor = 0, gold = 0, weapon = 0)
                mainCharacter.moveBy(0,0)
            elif self.__gold:
                prevGold = mainCharacter.getGold()
                goldNow = prevGold + self.__gold
                mainCharacter.setGold(goldNow)
                Chest(health = 0, armor = 0, gold = 0, weapon = 0)
                mainCharacter.moveBy(0,0)
            elif self.__health:
                prevHealthStat = mainCharacter.getHealth()
                healthStat = prevHealthStat + self.__health
                mainCharacter.setHealth(healthStat)
                Chest(health = 0, armor = 0, gold = 0, weapon = 0)
                mainCharacter.moveBy(0,0)
            elif self.__weapon:
                weaponPrevStatNum = mainCharacter.getWeaponStatNumber()
                weaponStatNum = 1 + weaponPrevStatNum
                mainCharacter.setWeaponStatNumber(weaponStatNum)
                weaponPrevStatTot = mainCharacter.getWeaponStatTotal()
                weaponStatTot = self.__weapon + weaponPrevStatTot
                mainCharacter.setWeaponStatTotal(weaponStatTot)
                Chest(health = 0, armor = 0, gold = 0, weapon = 0)
                mainCharacter.moveBy(0,0)
class Nothing:
    def __init__(self):
        pass
    def doYourThing(self,mainCharacter):
        Character(mainCharacter.moveBy(0,0))
    def movedDirection(self):
        return (0,0)
    def getLocation(self):
        return (0,0)
    
def main():
    mainDirection = 'none'
    mainRace = ""
    while mainDirection.lower() != 'q' and mainRace.lower() != 'q':
        f = False
        dirDic = {'nw':(1,-1),'ne':(1,1),'sw':(-1,-1),'se':(-1,1),'n':(1,0),'s':(-1,0),'w':(0,-1),'e':(0,1)}
        gameBoard = {(0,0):Nothing()}
        mainName = str(input("What would you like to name your Character? "))
        mainRace = str(input("Hello "+ mainName+ " are you an Elf or a Nord? "))
        raceDic = {'elf':'elf','nord':'nord'}
        if mainRace.lower() == 'q':
            print("GoodBye!")
        else:
            while mainRace.lower() not in raceDic:
                mainRace = str(input("Here you can be either Elf or Nord! Which are you? "))
                if mainRace =='q':
                    exit()
            mainCharacter = Character(name = mainName, race = mainRace)
            print(mainCharacter.getName() + ' the ' + mainCharacter.getRace())
            print("Your attack strength is: ", mainCharacter.getAttack())
            print("Your defensive strength is: ", mainCharacter.getDefense())
            print("Your health is: ", mainCharacter.getHealth())
            print("Your gold is: ", mainCharacter.getGold())
            mainDirection = str(input("Which direction do you want to go? "))
            while mainCharacter.getHealth() > 0:
                if mainDirection.lower() == 'x':
                    print(mainCharacter.getName() + ' the ' + mainCharacter.getRace())
                    print("Your attack strength is: ", mainCharacter.getAttack())
                    print("Your defensive strength is: ", mainCharacter.getDefense())
                    print("Your health is: ", mainCharacter.getHealth())
                    print("Your gold is: ", mainCharacter.getGold())
                    mainDirection = str(input("Which direction do you want to go? "))
                    continue
                if mainDirection.lower() in dirDic:
                    x,y = mainCharacter.getLocation()
                    dx,dy = dirDic[mainDirection.lower()]
                    mainCharacter.moveBy(dx,dy)
                    print(mainCharacter.getName() + ' the ' + mainCharacter.getRace() + ' moves '+ mainDirection.lower() +', now at ({0},{1})'.format(x+dx,y+dy))
                    print("Your attack strength is: ", mainCharacter.getAttack())
                    print("Your defensive strength is: ", mainCharacter.getDefense())
                    print("Your health is: ", mainCharacter.getHealth())
                    print("Your gold is: ", mainCharacter.getGold())
                    #stuff happens
                    if mainCharacter.getLocation() in gameBoard:
                        thing = gameBoard[mainCharacter.getLocation()]
                        print("There is %s here" % gameBoard[mainCharacter.getLocation()])
                        #if thing doesn't already exist
                    else:   
                        listSpaceOptions = [Nothing, Character, Chest]
                        Thing = random.choice(listSpaceOptions)
                        thing = Thing()
                        gameBoard[mainCharacter.getLocation()] = thing
                        print()
                        print("There is %s at this location" % gameBoard[mainCharacter.getLocation()])
                        thing.doYourThing(mainCharacter)
                        #if thing moved -> update board
                        if thing.movedDirection() != (0,0):
                            gameBoard[thing.getLocation()] = thing
                            gameBoard[mainCharacter.getLocation()] = Nothing()
    
                    #print(thing.whateverNeededToBePrinted())
                    if mainCharacter.movedDirection() == (0,0):
                        mainDirection = str(input("Which direction do you want to go? "))
                        f = True
                    else:
                       for dire,loca in dirDic.items():
                           if loca == mainCharacter.movedDirection():
                               mainDirection = dire
                               f = True
                        
                else:
                   print("To move, type the abbreviation of the direction.")
                   print("nw    n    ne")
                   print("w     x    e           x means display stats")
                   print("sw    s    se")
                   mainDirection = str(input("Which direction do you want to go? "))
                   f = True
    if f:
        mainDirection = 'none'
        


                    

                    
            
            
                
            
            
           
if __name__=='__main__':
    main()