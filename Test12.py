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

def main ():
    n = int(input())
    listPrime = sang(1,n)
    for i in range(0,len(listPrime)-3):
        sum =0
        result = []
        for j in range(i,i+4):
            sum += listPrime[j]
            result.append(listPrime[j])
        if sum > n:
            return
        print(result[0],result[1],result[2],result[3]) 


if __name__ == '__main__':
    main()