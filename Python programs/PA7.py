# Author: Coadiey Bryan
# CLID: C00039405
# Course/Section: CMPS 150 – Section 003
# Assignment: PA7
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
        dictionary = {1:"Ace",2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',12:'Queen',13:'King'}
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
        card1 = Card(2,12) # this will create a card that is a Queen of Diamonds
        rank = str(card1.getModRank())
        suit = str(card1.getModSuit())
        print("Card #1: %s of %s" % (rank,suit))
        
        suitgiver = random.randint(0,3) # these 3 lines will create a “random” card from the deck
        rankgiver = random.randint(1,13)
        card2 = Card(suitgiver,rankgiver)
        rank2 = card2.getModRank()
        suit2 = card2.getModSuit()
        print("Card #2: %s of %s" % (rank2, suit2))
        
        suitgiver2 = random.randint(0,3) # these 3 lines will create a “random” card from the deck
        rankgiver2 = random.randint(1,13)
        card3 = Card(suitgiver2,rankgiver2)
        rank3 = card3.getModRank()
        suit3 = card3.getModSuit()
        print("Card #2: %s of %s" % (rank3, suit3))
if __name__ =='__main__':
    main()