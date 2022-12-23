def main():
    n = int(input())
    coso = []
    somu = []
    i =2
    d=0
    while n > 1:
        if n%i==0 :
            n/=i
            if i not in coso:
                coso.append(i)
            d+=1
        else :
            if i in coso :
                somu.append(d)
            i+=1;
            d=0;
    somu.append(d)
    print(coso)
    print(somu)
if __name__ == '__main__':
    main()