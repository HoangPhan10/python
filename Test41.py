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
    a = int(input())
    k = int(input())
    n = int(input())

    if isPrime(binhPhuongCoLap(a,k,n)) :
        print("So nguyen to")
        return
    print("khong phai la so nguyen to")

if __name__ == '__main__':
    main()