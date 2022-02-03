#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=jp

V,E = map(int,input().split())

#初期化
dp = [[float("INF")]*V for i in range(V)]
for i in range(V):
    dp[i][i] = 0
for i in range(E):
    s,t,d = map(int,input().split())
    dp[s][t] = d

#更新
for k in range(V):
    for i in range(V):
        for j in range(V):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])

#負サイクル
negative = False
for i in range(V):
    if dp[i][i] < 0:
        negative = True

#出力
if negative:
    print("NEGATIVE CYCLE")
else:
    for i in range(V):
        for j in range(V):
            if j == V-1:
                if dp[i][j] == float("INF"):
                    print("INF")
                else:
                    print(dp[i][j])
            else:
                if dp[i][j] == float("INF"):
                    print("INF",end=" ")
                else:
                    print(dp[i][j],end=" ")

