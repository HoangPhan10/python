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

def findPandS(n):
    listPS =[]
    for i in range(1,n+1):
        if n%i == 0:
            listPS.append(i)
    return listPS

def main():
    while True:
        n = int(input())
        if n>0 :
            break
    ps = findPandS(n)
    q =0
    k =0
    p=0
    s=0
    for i in range(0,len(ps)):
        p+=ps[i]
        s+=1
        if isPrime(ps[i]) :
            q+=ps[i]
            k+=1
    print(n+p+s-q-k)

if __name__ == '__main__':
    main()