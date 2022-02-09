n = int(input())
a = list(map(int,input().split()))

ans = [0]
pre = 0
for cnt in a:
    pre = (pre+cnt)%360
    ans.append(pre)

ans.sort()

k = 0
for i in range(1,n):
    k = max(k,ans[i]-ans[i-1])
k = max(k,360-ans[-1])
print(k)
