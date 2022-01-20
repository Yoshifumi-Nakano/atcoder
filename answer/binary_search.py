N = 8
a = [3,5,8,10,14,17,21,39]

ok=8
ng=-1
key = 100

while ok-ng > 1 :
    mid = (ok+ng)//2
    if a[mid] == key:
        print(mid)
        exit()
    if a[mid] > key:
        ok = mid
    if a[mid] < key:
        ng = mid

print(-1)