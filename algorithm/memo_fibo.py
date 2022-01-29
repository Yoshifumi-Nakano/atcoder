N = int(input())
memo = [-1]*(N+1)

##memo化のフィボナッチ
def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    if memo[N] != -1:
        return memo[N]

    memo[N] = fibo(N-1)+fibo(N-2)
    return memo[N]
