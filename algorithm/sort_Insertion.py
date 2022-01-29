def insertSort(a):
    N = len(a)
    for i in range(1,N):
        #並び替える値
        v = a[i]

        cnt = 0
        for j in range(i-1,-1,-1):
            if v < a[j]:
                a[j+1] = a[j]
            else:
                cnt = j+1
                break
        a[cnt] = v
    return a

print(insertSort([1]))