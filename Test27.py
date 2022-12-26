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
def timUocChungLonNhat(a,b):
    if a<b:
        tmp =a
        a=b
        b=tmp
    while b>0 :
        r = a%b
        a=b
        b=r
    return a
def main():
    a = int(input())
    b = int(input())
    for i in range(a,b+1):
        for j in range(a,b+1):
            if i!=j :
                check = isPrime(timUocChungLonNhat(i,j))
                if check:
                    print(i,j)
if __name__ == '__main__':
    main()