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
def sang(A,B) :
    rs = []
    for i in range (0,B-A+1):
        rs.append(1)
    for i in range (2,math.ceil(math.sqrt(B))) :
        for j in range (max(i*i,(A+i-1)//i*i),B+1,i):
            rs[j-A]=0
    sum = 0
    for i in range (max(2,A),B+1):
        if rs[i-A] :
            sum+=i
    return sum
def main():
    n = int(input())
    print("So uoc ",analyticPrime(n))
    print("So uoc nguyen to ",sang(1,n))

if __name__ == '__main__':
    main()