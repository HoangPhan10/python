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

def main ():
    n = int(input())
    listPrime = sang(1,n)
    for i in range(0,len(listPrime)-3):
        sum =0
        result = []
        for j in range(i,i+4):
            sum += listPrime[j]
            result.append(listPrime[j])
        if sum > n:
            return
        print(result[0],result[1],result[2],result[3]) 


if __name__ == '__main__':
    main()