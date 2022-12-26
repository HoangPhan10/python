import math
def sang(A,B) :
    rs = []
    for i in range (0,B-A+1):
        rs.append(1)
    for i in range (2,math.ceil(math.sqrt(B))) :
        for j in range (max(i*i,(A+i-1)//i*i),B+1,i):
            rs[j-A]=0
    result = []
    for i in range (max(2,A),B+1):
        if rs[i-A] :
            result.append(i)
    return result

def main():
    listPrime = sang(pow(10,2),pow(10,3))
    for i in range(0,len(listPrime)):
        v = int(str(listPrime[i])[::-1])
        x = round(pow(v,1/3))
        if pow(x,3)==v:
            print(listPrime[i])

if __name__ == '__main__':
    main()