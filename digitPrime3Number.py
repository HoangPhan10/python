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
def checkCube(x):
    for i in range(5,10):
        if x%(i*i*i)==0 :
            return True
    return False

def main():
    for i in range(100,730):
        if isPrime(i):
            x=int(str(i)[::-1])
            if checkCube(x):
                print(i) 

if __name__ == '__main__':
    main()    