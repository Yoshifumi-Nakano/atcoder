from bisect import bisect_left
N=3
K = 10
a = [8,5,4]
b = [4,1,9]
b.sort()

ans= float("inf")
for i in range(len(a)):
    if a[i] >= K:
        ans = min(a[i],ans)
    else:
        index = bisect_left(b,K-a[i])
        if a[i] + b[index] >= K:
            ans = min(ans,a[i]+b[index])



print(ans)