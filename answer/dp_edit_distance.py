s1 = list(input())
s2 = list(input())

#dp[i][j]:s1のi番目までとs2のj番目までの編集距離
dp = [[float("inf")]*(len(s2)+1) for i in range(len(s1)+1)]

#初期化
for i in range(len(s1)+1):
    dp[i][0] = i
for j in range(len(s2)+1):
    dp[0][j] = j

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        #変更
        if s1[i-1] == s2[j-1]:
            dp[i][j] = min(dp[i][j],dp[i-1][j-1])
        else:
            dp[i][j] = min(dp[i][j],dp[i-1][j-1]+1)

        #sの削除
        dp[i][j] = min(dp[i][j],dp[i-1][j]+1)

        #tの削除
        dp[i][j] = min(dp[i][j],dp[i][j-1]+1)

print(dp[len(s1)][len(s2)])