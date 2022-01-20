N,W = list(map(int,input().split()))

w=[]
v=[]
for i in range(N):
    w_,v_ = map(int,input().split())
    w.append(w_)
    v.append(v_)

dp=[[0]*(W+1) for i in range(N+1)]

#dp[i][j]:i番目までの荷物を用いて重さj以下の価値の最大値
for i in range(1,N+1):
    for j in range(1,W+1):
        if j-w[i-1] >=0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])