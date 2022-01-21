#N：頂点数、M：辺数
N,M = list(map(int,input().split()))

G = [[] for i in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    G[a].append([b,w])

    #無向グラフの場合
    G[b].append([a,w])

print(G)