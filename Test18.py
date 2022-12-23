import math


def reverseNumberToArr(n,t,w):
    result = []
    x = [pow(2, i*w) for i in range(t)]
    for i in x[::-1]:
        result.append(math.floor(n/i))
        n%=i
    return result

def main():
    p = 2147483647
    w =8
    m = round(math.log2(p))
    t = round(m/w)

    a = int(input())
    b = int(input())

    arrA = reverseNumberToArr(a,t,w)
    arrB = reverseNumberToArr(b,t,w)

    result = []
    epsilon = 0

    e = pow(2,8)
    for i in range(t) :
        d = arrA[i] - arrB[i] -epsilon
        if d < 0 :
            d+=e
            epsilon = 1
        else : epsilon =0
        x = d%e    
        result.append(x)
    print(result[::-1])    
    print(a+b)    
if __name__ == '__main__':
    main()    