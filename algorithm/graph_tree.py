n = int(input())
es = [[] for i in range(n)]
for i in range(n-1):
    u,v,w = map(int,input().split())
    es[u-1].append((v-1,w))
    es[v-1].append((u-1,w))

#木上のdfs
#v：現在探索中の頂点 p：vの親(pが根の時は-1)
def dfs(v,p):
    for to in es[v]:
        if to == p:
            continue
        dfs(to,v)

#木の深さ
#d：深さ
depth = [0]*n
def dfs(v,p,d):
    depth[v] = d
    for to in es[v]:
        if to == p:
            continue
        dfs(to,v,d+1)

#部分木のサイズの漸化式
subtree = [0]*n
def dfs(v,p,d):
    depth[v] =d
    for to in es[v]:
        if to == p:
            continue
        dfs(to,v,d+1)

    #帰りがけ時に部分木サイズを求める
    subtree[v] = 1
    for to in es[v]:
        if to==p:
            continue
        subtree[v]+=subtree[to]



