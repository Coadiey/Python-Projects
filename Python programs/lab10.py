# Author:       Coadiey Bryan
# CLID/Section: C00039405/Sec.003
# lab10.py 
# use functions as much as possible !!!!!!
def deposits(d,bal):
    if d >= 0:
        new = bal + d
        return new
def withdrawals(w,bal):
    if w < bal:
        new = bal - w
        return new
    else:
        return bal
def balanceInquiry(b):
    return b
def typeOfNewBalance(forTheBrokeAmongUs,oldBalance,typ):
    if forTheBrokeAmongUs == oldBalance and typ == 0:
        x = "<denied>"
        return x
    else:
        x = format(forTheBrokeAmongUs,'10.2f')
        return x
def main():
    print()
    balance = float(input("Enter beginning balance: "))
    print()
    infile = open("lab10_data.py","r")
    # priming read to get first set of data from the file
    trans = infile.readline().strip()
    amount = float(infile.readline())
        # process data just read from the file
    while (trans != 'X'):     # **********  sentinel-controlled loop  ***********
        if trans == 'D':
            newBalance = deposits(amount,balance)
            typ = 0
            print(" Deposit        {0:8.2f}    {1}".format(amount,typeOfNewBalance(newBalance,balance,typ)))
        elif trans == 'W':
            newBalance = withdrawals(amount,balance)
            typ = 0
            print(" Withdrawal     {0:8.2f}    {1}".format(amount,typeOfNewBalance(newBalance,balance,typ)))
        elif trans == 'B':
            newBalance = balanceInquiry(balance)
            typ = 1
            print(" Balance Inquiry{0:7s}    {1}".format("",typeOfNewBalance(newBalance,balance,typ)))
        # get next set of data from the file
        balance = newBalance
        trans = infile.readline().strip()
        amount = float(infile.readline())
    print()
    print("That's All Folks!")
main()

