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

def main():
    n =int(input())
    for i in range(1,n+1):
        x = random.randint(1,1000)
        if isPrime(x):
            print(x)
if __name__ == "__main__":
    main()