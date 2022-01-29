N=int(input())
K=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#二つの配列のペアの中から和がK以上の中で最小のもの
min_value=float("inf")
for i in range(N):
    for j in range(N):
        S = a[i]+b[j]
        if S >= K and S < min_value:
            min_value = S

print(min_value)