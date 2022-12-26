import math
def sang(A,B) :
    rs = []
    for i in range (0,B-A+1):
        rs.append(1)
    for i in range (2,math.ceil(math.sqrt(B))) :
        for j in range (max(i*i,(A+i-1)//i*i),B+1,i):
            rs[j-A]=0
    for i in range (max(2,A),B+1):
        if rs[i-A] :
            print(i)
def main() :
    a = int(input())
    b = int(input())
    sang(a,b)
if __name__ == '__main__':
    main()
