#a[left,right)をmergeする
def merge_sort(a,left,right):
    if right-left == 1:
        return a
    
    mid = (left+right)//2

    #左半分をsort
    merge_sort(a,left,mid)
    #右半分をsort
    merge_sort(a,mid,right)

    #bufに保存しておく
    buf = []
    for i in range(left,mid):
        buf.append(a[i])
    for i in range(right-1,mid-1,-1):
        buf.append(a[i])

    #併合する
    index_left = 0
    index_right = len(buf)-1
    for i in range(left,right):
        if buf[index_left] < buf[index_right]:
            a[i] = buf[index_left]
            index_left += 1
        else:
            a[i] = buf[index_right]
            index_right -= 1
    return a

a = [12,9,15,3,8,17,6,1]
print(merge_sort(a,0,len(a)))

