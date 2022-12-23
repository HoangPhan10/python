import math
def main():
    a = int(input())
    w =8
    p = 2147483647
    result = []
    m = round(math.log2(p))
    t = round(m/w)
    n = [pow(2, i*w) for i in range(t)]
    for i in n[::-1]:
        result.append(math.floor(a/i))
        a%=i
    print(result)
if __name__ == '__main__':
    main()    