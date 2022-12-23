def nghichDao(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u!=1 :
        q = int(v/u)
        r = v-q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    print(x1)
def main():
    a = int(input())
    p = int(input())
    nghichDao(a,p)
if __name__ == '__main__':
    main()