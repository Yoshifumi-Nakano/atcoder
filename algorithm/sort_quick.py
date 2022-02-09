def swap(i,j,a):
    p = a[i]
    a[i] = a[j]
    a[j] = p
    return a

#a[right,left)をsortする
def QuickSort(left,right,a):
    if right - left <=1:
        return a

    #pivotを見つける
    pivot_index = (left + right)//2
    pivot = a[pivot_index]

    #pivotと端っこをswap
    a = swap(pivot_index,right-1,a)

    #pivotより小さいものが現れたらswapする位置
    i = left
    for j in range(left,right-1):
        if a[j] < pivot:
            a = swap(i,j,a)
            i+=1

    #pivotをあるべき場所に戻す
    a = swap(i,right-1,a)

    #再起的に
    QuickSort(left,i,a)
    QuickSort(i+1,right,a)

    return a

a = [12,9,15,3,8,17,6,1]
print(QuickSort(0,len(a),a))