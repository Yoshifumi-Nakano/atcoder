N = int(input())
K = int(input())
C = [list(map(int,input().split())) for i in range(N)]

#dp[i]:[0,i)の区間最小コスト
dp = [float("inf")]*N
dp[0] = 0
for i in range(N+1):
    for j in range(i):
        dp[i] = min(dp[i],dp[j]+C[j][i])