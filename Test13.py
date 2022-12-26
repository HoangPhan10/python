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
def sang(n):
    prime = []
    for i in range(0,n+1):
        prime.append(True)
    prime[0] = False
    prime[1] =False
    for i in range(2,math.ceil(math.sqrt(n+1))):
        if prime[i] :
            for j in range(i*i,n+1,i):
                prime[j] = False
    result = []
    for i in range(0,n+1):
        if prime[i]:
            result.append(i)
    return result

def main():
    n = int(input())
    listPrime = sang(1,n)
    for i in range(0,len(listPrime)) :
        for j in range(0,len(listPrime)) :
            tong = listPrime[i]+listPrime[j]
            hieu = listPrime[i]-listPrime[j]
            if isPrime(tong) and isPrime(hieu) and hieu>0:
                print(listPrime[i],listPrime[j])

if __name__ == '__main__':
    main()