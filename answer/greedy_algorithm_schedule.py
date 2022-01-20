N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
A = sorted(A,key=lambda x:x[1])

last = 0
ans = 0
for i in range(N):
    a,b = A[i]
    if a > last:
        ans+=1
        last = b

print(ans)

