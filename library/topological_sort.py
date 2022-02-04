v,e = map(int,input().split())

es = [[] for i in range(v)]
for i in range(e):
    s,t = map(int,input().split())
    es[s].append(t)

#トポロジカルソート
seen = [False]*v
order = [] #トポロジカル順
def dfs(v):
    seen[v] = True
    for to in es[v]:
        if seen[to]:
            continue
        dfs(to)

    #dfsが終わったものから順に記録していく
    order.append(v)

#トポロジカルソート
for i in range(v):
    if seen[i]:
        continue
    dfs(i)
order.reverse()

#ソート
for i in order:
    print(i)


