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
    n = int(input())     
    a = int(input())     
    b = int(input())     
    c = int(input())

    for i in range(1,n):
        if isPrime(a*i*i+b*i+c):
            print(i)
            return
    print("not found")
    return        
         
if __name__ == "__main__":
    main()    