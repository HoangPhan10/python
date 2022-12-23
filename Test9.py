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
   for i in range(l,r+1):
        if isPrime(i): 
            print(i)

def main():
    n = int(input())
    sang(1,n)

if __name__ == '__main__':
    main()