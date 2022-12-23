def findSum(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum
def main():
    n = int(input())
    for i in range(1,n):
        a = findSum(i)
        if findSum(a)==i :
            print(i,a)
if __name__ == '__main__':
    main()