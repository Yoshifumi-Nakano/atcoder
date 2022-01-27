import copy

N = int(input())
A = list(map(int,input().split()))

#二分探索(平均値)
ok = -1
ng = max(A)+1
cnt = 0

while cnt < 50:
    X = copy.deepcopy(A)
    mid = (ng+ok)/2
    for i in range(N):
        X[i] -= mid

    #dp[i]:最初のi番目までの\sumのMax
    dp = [[0]*2 for i in range(N+1)]
    for i in range(1,N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = max(dp[i-1][1]+X[i-1],dp[i-1][0]+X[i-1])

    #平均をx以上にできる
    if dp[N][0] >=0 or dp[N][1] >=0:
        ok = mid
    else:
        ng = mid
    cnt +=1

print(ok)

#二分探索(中央値)
ok = -1
ng = max(A)+1

while ng-ok >1:
    X = copy.deepcopy(A)
    dp = [[0]*2 for i in range(N+1)]

    mid = (ng+ok)//2
    for i in range(N):
        if X[i] < mid:
            X[i] = -1
        else:
            X[i] = 1

    for i in range(1,N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = max(dp[i-1][1]+X[i-1],dp[i-1][0]+X[i-1])
    
    if dp[N][0] >0 or dp[N][1]>0:
        ok = mid
    else:
        ng = mid

print(ok)

