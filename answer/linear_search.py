A = list(map(int,input().split()))
v= int(input())
N = len(A)

#与えられた数列の中から該当する値があるかどうかとその場所を特定する
ans=False
id= -1
for i in range(N):
    if A[i]==7:
        ans = True
        id = i

print(ans,id)

#配列の中から最小要素を導き出す
min_value = float("inf")
for i in range(N):
    if A[i]<min_value:
        min_value=A[i]

print(min_value)
