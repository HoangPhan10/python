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
    listSum = []
    sum=0
    for i in range(1,int(math.sqrt(b))+1):
        s1 = pow(i,2)
        for j in range(1,int(math.sqrt(b))+1):
            listSum.append(s1+pow(j,2))
    for i in range(a,b+1):
        if isPrime(i) :
            if i in listSum :
                print(i)
                sum+=1
    print(sum)

if __name__ == '__main__':
    main()