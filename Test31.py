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

def main():
    n =123456
    a = int(input())
    k = int(input())
    print(binhPhuongCoLap(a,k,n))

if __name__ == '__main__':
    main()