class Book():
    def __init__(self, title, author, isbn, bookNumbers, price, expectedPercent):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__bookNumbers = bookNumbers
        self.__price = price
        self.__expectedPercent = expectedPercent
        def setSales(self,amount):
            self.__sales = amount
        def isGreaterThan(self,other):
            
def fileToBooks(infile):
    books  = []
    #make a while loop that stops when it gets to ***
    #in the while loop, #read each line that corresponds to the 6 data pieces
    book
    book = Book(title, author, isbn, booksNumbers, priece, expectedPercent)
    
def main():
    #part 1
    #open the file inventory.txt
    arrivals = fileToBooks(infile) #part 1
    arrivalSales = modifyBooksWithSales(arrivals) #Part2
    performers = goodBooks(arrivalSales) #part3 
    performer = topPerformer(performers) #part4
    totalSales = grossSales(arrivalSales) #part 5
    
    print(totalSales)
    print(performer)
    