h,w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]

for i in range(w):
    for j in range(h):
        if j==h-1:
            print(a[j][i])
        else:
            print(a[j][i],end=" ")
