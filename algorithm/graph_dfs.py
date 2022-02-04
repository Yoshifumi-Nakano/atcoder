n,m= map(int,input().split())
seen = [False]
es=[[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    es[a].append(b)


#頂点vから探索してない頂点を全て探索する
def dfs(v):
    #探索済にする
    seen[v] = True

    #vから到達可能な頂点を全て調べる
    for e in es[v]:
        if seen[e[0]]:
            continue
        dfs(e[1])


