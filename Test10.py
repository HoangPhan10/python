import math
def analyticPrime(n):
    sum = 1
    for i in range(2,n):
        dem=0
        while n%i==0:
            n/=i
            dem+=1
        sum*=dem+1
        if n==1 :
            return sum
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
    sum = 0
    for i in range(l,r+1):
        if isPrime(i): 
            sum += i
    return sum
def main():
    n = int(input())
    print("So uoc ",analyticPrime(n))
    print("So uoc nguyen to ",sang(1,n))

if __name__ == '__main__':
    main()