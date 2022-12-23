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
    a = int(input())
    b = int(input())
    sum =0
    for i in range(a,b+1):
        dem =0
        for j in range(2,i):
            if isPrime(j):
                dem+=1
        if isPrime(dem):
            sum+=1
    print(sum)        
    
if __name__ == '__main__':
    main()    