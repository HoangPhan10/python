import math
def isPrime(x):
    if x<=1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    for i in range(5,int(math.sqrt(x))+1,6):
        if x%i==0 or x%(i+2)==0 :
            return False
    return True
def sang(l,r):
    result = []
    for i in range(l,r+1):
        if isPrime(i): 
            result.append(i)
    return result
def main():
    listPrime = sang(pow(10,2),pow(10,3))
    for i in range(0,len(listPrime)):
        v = int(str(listPrime[i])[::-1])
        x = round(pow(v,1/3))
        if pow(x,3)==v:
            print(listPrime[i])

if __name__ == '__main__':
    main()