
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
    
def checkTprime(x):
    sqrtNum = int(math.sqrt(x))
    if math.pow(sqrtNum,2)== x:
        if isPrime(sqrtNum):
            print(x)
def main():
    n = int(input())
    for i in range(1,n+1):
        checkTprime(i)
if __name__ == "__main__":
    main()

