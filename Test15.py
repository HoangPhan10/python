import math
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
    for i in range(0,len(listPrime)-1):
        if listPrime[i+1]-listPrime[i]==2:
            print(listPrime[i],listPrime[i+1])

if __name__ == '__main__':
    main()