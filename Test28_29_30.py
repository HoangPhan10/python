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
def isCarmichael(n):
    if isPrime(n):
        return False
    b = 2
    while b<n:
        if timUocChungLonNhat(b,n)==1 :
            u = binhPhuongCoLap(b,n-1,n)
            if u !=1:
                return False
        b+=1
    return True

def main():
    while True:
        n = int(input())
        if n>=0 and n<=10000 :
            break
    for i in range(2,n):
        if isCarmichael(i):
            print(i)

if __name__ == '__main__':
    main()