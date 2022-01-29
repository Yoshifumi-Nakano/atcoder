a,n = map(int,input().split())
dp = [float("inf")]*(10**6)
dp[1] = 0

def swap(x):
    q = x //10
    r = x % 10
    digit = 10**(len(str(x))-1)
    x = r*digit + q
    return x

def dfs(x):
    if x > 10**6:
        return

    #aをかける
    y = a*x
    if y < 10**6 and dp[y] > dp[x]+1:
        dp[y] = dp[x]+1
        dfs(y)

    #入れ替え
    if x <= 10 or x % 10 ==0:
        return
    z = swap(x)
    if z < 10**6 and dp[z] > dp[x]+1:
        dp[z] = dp[x]+1
        dfs(z)

dfs(1)

if dp[n] == float("inf"):
    print(-1)
else:
    print(dp[n])




