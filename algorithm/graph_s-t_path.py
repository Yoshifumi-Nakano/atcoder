## https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(10000000)

H,W = map(int,input().split())
c = [list(input()) for i in range(H)]
for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            s = (i,j)
        elif c[i][j] == "g":
            t = (i,j)

#始点(i,j)から始まるdfs
seen = [[False]*W for i in range(H)]
def dfs(i,j):
    seen[i][j] = True

    if 0<=i+1<=H-1 and 0<=j<=W-1 and c[i+1][j] != "#":
        if not seen[i+1][j]:
            dfs(i+1,j)
    if 0<=i-1<=H-1 and 0<=j<=W-1 and c[i-1][j] != "#":
        if not seen[i-1][j]:
            dfs(i-1,j)
    if 0<=i<= H-1 and 0<=j+1<=W-1 and c[i][j+1] != "#":
        if not seen[i][j+1]:
            dfs(i,j+1)
    if 0<=i<=H-1 and 0<=j-1<=W-1 and c[i][j-1] != "#":
        if not seen[i][j-1]:
            dfs(i,j-1)

dfs(s[0],s[1])
if seen[t[0]][t[1]]:
    print("Yes")
else:
    print("No")


