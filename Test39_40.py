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
    if a>b:
        tmp =a
        a=b
        b=tmp
    while b>0 :
        r = a%b
        a=b
        b=r
    return a

def main():
    n =int(input())
    listIn = []
    for i in range(0,n):
        x = int(input())
        listIn.append(x)
    sum = 0
    for i in range(0,n):
        for j in range(0,n):
            if listIn[i]>=listIn[j] and isPrime(timUocChungLonNhat(listIn[i],listIn[j])):
                print(listIn[i],listIn[j])
                sum+=1
    print(sum)
if __name__ == '__main__':
    main()