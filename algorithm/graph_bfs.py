from collections import deque

#input
n,m= map(int,input().split())
seen = [False]
es=[[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    es[a].append(b)
    es[b].append(a)

print(es)
#始点sから始まる幅優先探索
def bfs(s):
    dist = [-1]*n

    #初期条件
    dist[s] = 0
    q = deque([])
    q.append(s)

    #queが空になるまで探索を行う
    while len(q)>0:
        v = q.popleft()
        #vから辿れる頂点を全て探索
        for to in es[v]:
            #すでに探索済み
            if dist[to] != -1:
                continue
            dist[to] = dist[v]+1
            q.append(to)
    return dist

#出力
print(bfs(0))






