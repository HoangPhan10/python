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

def main():
    n = int(input())
    for i in range(1,n+1):
        if analyticPrime(i)==4:
            print(i)

if __name__ == '__main__':
    main()