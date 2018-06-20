import random
#def rndAlpha(numAlpha):
#   return []
#def rndDigits(numDigits):
#    return[5,6,7]
#def rndNonAlpha(numNonAlpha):
#    return []
def rndJoin(a,d,n):
    result = []
    k = a + d + n
    while k:
        c = random.choice(k)
        k.remove(c)
        result.append(c)
    return result

def rndAlpha(numAlpha):
    options = list(range(65,91))+list(range(97,123))
    options = list(map(chr, options))
    result= []
    for _ in range(numAlpha):
        c = random.choice(options)
        result.append(c)
    return result
def rndNonAlpha(numNonAlpha):
    options = ["@","!","?","*"]
    result = []
    for _ in range(numNonAlpha):
        c = random.choice(options)
        result.append(c)
    return result
def rndDigits(numDigits):
    result = []
    for _ in range(2, numDigits+1, 2):
        c = random.randint(10,99)
        result.append(c)
    return result
def password(numAlpha, numDigits, numNonAlpha, rndAlpha = rndAlpha, rndDigits=rndDigits, rndNonAlpha=rndNonAlpha):
    total = numAlpha + numDigits + numNonAlpha
    if total >= 100 or total < 8 or numDigits <0 or numAlpha <0 or numNonAlpha <0:
        return "#ReallyBadStupidTryAgainClient"
    return "".join(map(str,rndJoin(rndAlpha(numAlpha),rndDigits(numDigits),rndNonAlpha(numNonAlpha))))
if __name__ == "__main__":
    x = input("Please tell us how many of what you'd like in your new password in the form Letters, Digits, Symbols: ")
    a,b,c = x.split(',')
    print(password(int(a),int(b) ,int(c)))
    #password(int(x),int(y),int(z))