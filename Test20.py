import math
def main():
    while True:
        m = int(input())
        n = int(input())
        d = int(input())
        if m>0 and n>0 and d>0  and d<1000 and m<1000 and n <=1000:
            break
    if d>n:
        print("Not found")
        return
    for i in range(2,math.ceil(n/d)):
        if d*i >m :
            print(d,d*i)
    for i in range(2,math.ceil(n/d)):
        a = d*i
        if a >m :
            for j in range(1,math.ceil(n/d)):
                b = d*j
                if b >m and a!=b:
                    print(a,b)

if __name__ == '__main__':
    main()