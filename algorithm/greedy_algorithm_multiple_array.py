N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

ans=0
for i in range(N-1,-1,-1):
    a,b = A[i]
    a += ans
    if a%b!=0:
        ans += b*(a//b+1)-a

print(ans)
