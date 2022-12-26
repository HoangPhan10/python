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
    sum = 0
    for i in range(0,n+1):
        if prime[i]:
            sum +=i
    print(sum)    


def main():
    n = int(input())
    sang(n)
    
if __name__ == '__main__':
    main()