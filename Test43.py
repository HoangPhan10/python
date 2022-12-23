import random
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

def binhPhuongCoLap(a,k,n):
    b=1
    if k==0 :
        return b
    A =a
    binK = list(bin(k)[::-1].split('b0')[0])

    if int(binK[0])==1:
        b=a
    for i in range(1,len(binK)):
        A = pow(A,2)%n
        if int(binK[i])==1 :
            b=(A*b)%n
    return b

def main():
    while True:
        n = int(input())
        if n>0 and n<1000 :
            break
    while True:
        p = random.randint(1,100)
        if isPrime(p):
            break
    print(n,p)
    for i in range(1,n):
        if isPrime(binhPhuongCoLap(i,p,n)):
            print(i)

        


if __name__ == '__main__':
    main()