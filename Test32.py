import math
import random
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

def nghichDao(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u!=1 :
        q = int(v/u)
        r = v-q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1

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

def timUocChungLonNhat(a,b):
    if a>b:
        tmp =a
        a=b
        b=tmp
    while b>0 :
        r = a%b
        a=b
        b=r
    return a

def main():
    while True:
        p = random.randint(101,499)
        q = random.randint(101,499)
        if isPrime(p) and isPrime(q):
            break
    n = p*q
    phiN = (p-1)*(q-1)
    while True:
        e = random.randint(2,phiN-1)
        if timUocChungLonNhat(e,phiN)==1:
            break
    d = nghichDao(e,phiN)
    if d<0:
        d+=phiN
    m = 247 + 123
    c = binhPhuongCoLap(m,e,n)
    # kq = binhPhuongCoLap(c,d,n)
    print("p = ",p)
    print("q = ",q)
    print("e = ",e)
    print("m = ",m)
    print("c = ",c)
    
if __name__ == '__main__':
    main()