# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

#V：頂点数、E：辺数, r:始点
V,E,r = map(int,input().split())

#辺のリスト
es = [[] for i in range(V)]
for i in range(E):
    s_,t_,w_ = map(int,input().split())
    es[s_].append((t_,w_))

#ダイクストラ
import heapq
def dijkstra(r):
    d = [float("INF")]*V
    d[r] = 0
    used = [False]*V
    used[r] = True

    q = []
    for e in es[r]:
        heapq.heappush(q,(e[1],e[0]))

    while len(q) > 0:
        #残っている点で最小のものを探し出す
        dist, v = heapq.heappop(q)

        #すでに値が決定している頂点
        if used[v]:
            continue

        #vを決定する
        used[v] = True
        d[v] = dist

        #vから伸びる辺を探索
        for t,w in es[v]:
            if not used[t]:
                heapq.heappush(q,(d[v]+w,t))
    return d

#実行
d = dijkstra(r)
for ans in d:
    if ans == float("INF"):
        print("INF")
    else:
        print(ans)


