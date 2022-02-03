n,m = map(int,input().split())
h = list(map(int,input().split()))
es = [[] for i in range(n)]

for i in range(m):
    u,v = map(int,input().split())
    u -=1
    v -=1
    if h[u] < h[v]:
        es[u].append((h[v]-h[u],v))
        es[v].append((0,u))
    else:
        es[u].append((0,v))
        es[v].append((h[u]-h[v],u))

#ダイクストラ 
import heapq
q = []
heapq.heappush(q,(0,0))
for d,t in es[0]:
    heapq.heappush(q,(d,t))

d=[float("INF")]*n
used = [False]*n

used[0]=True
d[0]=0


while len(q)>0:
    w,v = heapq.heappop(q)
    if used[v]:
        continue

    used[v]=True
    d[v]=w

    for e in es[v]:
        if not used[e[1]]:
            heapq.heappush(q,(d[v]+e[0],e[1]))

for i in range(n):
    d[i] = d[i] + h[i] - h[0]

print(-1*min(d))


