def random():
    import random
    #y = random.randint(1,31), random.randint(1,31), random.randint(1,31), random.randint(1,31), random.randint(1,31), random.randint(1,31), random.randint(1,31)
    randoms = [random.randint(1,30) for _ in range(7)]
    print(randoms)
    return randoms
    #while x[0] > 30 or x[0]<1 or x[1]>30  or x[1]<1 or x[2]>30 or x[2]<1 or x[3]>30 or x[3]<1 or x[4]>30 or x[4]<1 or x[5]>30 or x[5]<1 or x[6]>30 or x[6]<1:
def count(x,y):
    result = [(1 if (x[i] in y) else 0) for i in range(7)]
    print(sum(result))
    return sum(result)
#thats ^ called a ternay or conditional operator
    #c = 0
    #if x[0]==y[0]:
        #c = c+1
    #if x[1]==y[1]:
        #c = c+1
    #if x[2]==y[2]:
        #c=c+1
    #if x[3]==y[3]:
        #c=c+1
    #if x[4]==y[4]:
        #c=c+1
    #if x[5]==y[5]:
        #c=c+1
    #if x[6]==y[6]:
        #c=c+1
        #return c
def lottery(f,g):
    right = count(f,g)
    if right==7:
        #print("You Win!")
        return "You win!"
    if right==0:
        #print("You really suck :(")
        return "You really suck :("
        #print("You kinda suck you got" + right)
        return "You kinda suck you got " + str(right)
    
def getInput():
    return list(map(int, input("Please enter 7 Lottery numbers (1-30) with commas in-between each number : ").split(",")))
    
if __name__ == "__main__":
    users = getInput()
    while len(users) != 7 or any([i < 1 or i > 30 for i in users]):
        print("That wasn't between 1 and 30 idiot")
        users  = getInput()
    randoms = random()
    print(lottery(users,randoms))


    
    
    
    
    





