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
    sum = 0
    for i in range(l,r+1):
        if isPrime(i): 
            sum+=i
    return sum
def main():
    a = int(input())
    b = int(input())
    
    sum = sang(a,b)
    if isPrime(sum) :
        print("YES")
        return
    print("NO")

if __name__ == "__main__":
    main()
