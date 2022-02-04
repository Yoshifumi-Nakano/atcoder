# https://atcoder.jp/contests/abc126/tasks/abc126_d

import sys
sys.setrecursionlimit(10000000)

n = int(input())
es = [[] for i in range(n)]
for i in range(n-1):
    u,v,w = map(int,input().split())
    es[u-1].append((v-1,w))
    es[v-1].append((u-1,w))



color = [-1]*n
def dfs(v,cur):
    color[v]=cur

    for to,w in es[v]:
        if color[to] != -1:
            continue

        #隣は同じ色で塗る
        if w %2== 0:
            dfs(to,cur)
        #隣は違う色で塗る
        else:
            dfs(to,1-cur)

dfs(0,0)
for i in color:
    print(i)

