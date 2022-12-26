def binhPhuongCoLap(a,k,n):
    b=1
    if k==0 :
        return b
    A =a
    binK = list(bin(k)[::-1].split('b0')[0])

    if int(binK[0])==1:
        b=a
    for i in range(1,len(binK)):
        A = pow(A,2)%n
        if int(binK[i])==1 :
            b=(A*b)%n
    return b

def fermat(n,t):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n %2==0 :
        return False
    a = 2
    for i in range(1,t+1):
        x = binhPhuongCoLap(a,n-1,n)
        a+=1
        if x != 1:
            return False
    return True

def tinhF(i) :
    if fermat(i,3) :
        return i
    return 0

def main():
    l =int(input())
    r =int(input())
    sum = 0;
    for i in range(l,r):
        for j in range(l+1,r+1):
            if j>i :
                tich = tinhF(i)*tinhF(j)
                sum+=tich
    print("sum",sum)

if __name__ == '__main__':
    main()    