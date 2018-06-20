# Author: Coadiey Bryan
# CLID: C00039405
# Course/Section: CMPS 150 – Section 003
# Assignment: PA9
# Date Assigned: Friday, November 17, 2017
# Date/Time Due: Wednesday, November 22, 2017 –- 11:55 pm
#Description: This program is just a simple class setup that changes the output into a string based on the input using dictionaries
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
import random
class Card():
    def __init__(self,suit,rank):
        self.__rank = rank
        self.__suit = suit
    def getModSuit(self):
        suit = self.__suit
        dictionary = {0:"Hearts",1:"Spades",2:"Diamonds",3:"Clubs"}
        if suit in dictionary:
            return dictionary[suit]
        else:
            return "ERROR"
    def getModRank(self):
        rank = self.__rank
        dictionary = {1:"Ace",2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',12:'Queen',13:'King',14:'Ace'}
        if rank in dictionary:
            return dictionary[rank]
        else:
            return "ERROR"
    def getSuit(self):
        return self.__suit
    def getRank(self):
        return self.__rank
    def setSuit(self,suit):
        self.__suit = suit
    def setRank(self,rank):
        self.__rank = rank
def main():  
        file = input("Enter the filename: ")
        infile = open(file,'r')
        suit = int(infile.readline())
        rank = int(infile.readline())
        print("Cards: ")
        highestCard = 0
        while suit != -1 and rank != -1:
            card = Card(suit,rank) 
            aceDict = {1:14,14:'Ace'}
            if rank in aceDict:
                rank = 14
                highestSuit = suit
            if rank > highestCard:
                highestCard = rank
                highestSuit = suit
            rank = str(card.getModRank())
            suit = str(card.getModSuit())
            print("%s of %s" % (rank,suit))
            
            suit = int(infile.readline())
            rank = int(infile.readline())
        if highestCard in aceDict:
            highestCard = aceDict[highestCard]  
        dictionary = {1:"Ace",2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',12:'Queen',13:'King',14:'Ace'}
        if highestCard in dictionary:
            highestCard = dictionary[highestCard]
        dictionary = {0:"Hearts",1:"Spades",2:"Diamonds",3:"Clubs"}
        if highestSuit in dictionary:
            highestSuit = dictionary[highestSuit]
        else:
            highestSuit = "ERROR"
        print()
        print("High card: {0} of {1}".format(highestCard,highestSuit))
'''
        highestCard = rankgiver

            highestCard = rankgiver
        elif rankgiver2 in aceDict:
            rankgiver2 = 14
            highestCard = rankgiver2
        elif rankgiver3 in aceDict:
            rankgiver3 = 14
            highestCard = rankgiver3
        if rankgiver2 > highestCard:
            highestCard = rankgiver2
        if rankgiver3 > highestCard:
            highestCard = rankgiver3
        if highestCard == rankgiver:
            highs = str(1)
            ranks = rank
            suits = suit
        elif highestCard == rankgiver2:
            highs = str(2)
            ranks = rank2
            suits = suit2
        elif highestCard == rankgiver3:
            highs = str(3)
            ranks = rank3
            suits = suit3    
        
'''
if __name__ =='__main__':
    main()