def findIndexChar(listCh,ch) :
    for i in range(len(listCh)-1,-1,-1):
        if listCh[i] == ch :
            return i
    return -1

def main():
    s2 = str(input())
    s1 = str(input())

    lx = {}
    listS1 = list(s1)
    listS2 = list(s2)
    listS2Lx = list(set(s2))

    for i in range(0, len(listS2Lx)):
       lx[listS2Lx[i]] = findIndexChar(listS1,listS2Lx[i])
    
    j = len(listS1)-1
    i = len(listS1)-1
    dem =0
    while j >=0 and i<len(listS2):
        dem+=1
        if listS1[j] == listS2[i] :
            j-=1
            i-=1
        else :
            i = i + len(listS1) - min(j,1+lx[listS2[i]])
            j=len(listS1)-1
        print(i,j)
    print(dem)

if __name__ == '__main__':
    main()