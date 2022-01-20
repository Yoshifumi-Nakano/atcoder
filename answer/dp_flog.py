N = int(input())
h=list(map(int,input().split()))
dp= [float("inf")]*N

#貰うdp
for i in range(1,N):
    if i==1:
        dp[i] = abs(h[i]-h[i-1])
    else:
        dp[i]=min(
            dp[i-1]+abs(h[i]-h[i-1]),
            dp[i-2]+abs(h[i]-h[i-2])
        )

#配るdp
dp[0]=0
for i in range(N):
    if i+1 <= N-1:
        dp[i+1] = min(dp[i+1],dp[i]+abs(h[i+1]-h[i]))
    if i+2 <= N-1:
        dp[i+2] = min(dp[i+2],dp[i]+abs(h[i+2]-h[i]))


print(dp[N-1])