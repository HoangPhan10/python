def main():
    s2 = str(input())
    s1 = str(input())
    arrS1 = list(s1)
    arrS2 = list(s2)
    fx =[-1]
    for i in range(1,len(s1)):
        arrStr1 = []
        arrStr2 = []
        for j in range(1,i+1) :
            arrStr1.append(s1[0:j])
            arrStr2.append(s1[j:i])
        likeArr=""
        for i in range(0,len(arrStr2)):
            if arrStr2[i] in arrStr1 :
                likeArr = arrStr2[i]
        fx.append(len(likeArr))
    
    i =0
    j =0
    dem =0
    while j <len(s1) :
        dem +=1
        if arrS2[i+j] == arrS1[j]:
            j+=1
        else:
            i = i+j - fx[j]
            if fx[j] == -1 :
                j =0
            else : j = fx[j]
        if i>=len(s2) :
            print("Not found")
            return
    print(dem)
if __name__ == '__main__':
    main()