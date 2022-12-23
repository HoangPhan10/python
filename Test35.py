import random
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
    while True:
        n = int(input())
        if n>=3 and n%2!=0 :
            break
    t = int(input())
    m =n-1
    s=0
    while m%2==0 :
        s+=1
        m/=2

    for i in range(1,t+1):
        a = random.randint(2,n-2)
        y = binhPhuongCoLap(a,int(m),n)

        if y!=1 and y!=n-1 :
            j =1
            while j<=s-1 and y!=n-1 :
                    y = binhPhuongCoLap(y,2,n)
                    if y ==1 :
                        print("Hop so")
                        return
                    j+=1
            if y !=n-1:
                print("Hop so")
                return
        print("Nguyen to")
        return


if __name__ == '__main__':
    main()