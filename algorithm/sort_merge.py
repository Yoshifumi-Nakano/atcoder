# a[left,right)をsortする
def mergeSort(a,left,right):
    if right-left == 1:
        return
    mid = (left+right)//2
    mergeSort(a,left,mid)
    mergeSort(a,mid,right)

    #配列を保存しておく
    buf = []
    for i in range(mid):
        buf.append(a[i])
    for i in range(len(a),mid-1,-1):
        buf.append(a[i])

    #併合する
    left = 0
    right = len(buf)-1
    for i in range(len(a)):
        if buf[left] <= buf[right]:
            a[i] = buf[left]

