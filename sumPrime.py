import math

def snt(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if (n % i == 0) or (n % (i+2) == 0):
            return False
    return True

def main():
    start = int(input())
    end = int(input())
    sum = 0
    for i in range(start, end+1):
        if snt(i):
            sum+=1
    print(sum)

if __name__=='__main__':
    main()