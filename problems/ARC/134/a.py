n,l,w = map(int,input().split())
a = list(map(int,input().split()))

last = 0
ans = 0
for i in range(n):
    first = a[i]
    if first > last:
        if (first-last)%w ==0:
            ans += (first-last)//w
        else:
            ans += (first-last)//w +1
    last = a[i] + w


if last < l:
    if (l-last)%w ==0:
        ans += (l-last)//w
    else:
        ans += (l-last)//w +1
print(ans)
