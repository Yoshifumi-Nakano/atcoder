V,E = map(int,input().split())
s = 0
goal = V-1

#辺のinput
from collections import defaultdict
from collections import deque
es = defaultdict(set)
cost = [[0]*V for i in range(V)]
for i in range(E):
    u,v,c = map(int,input().split())
    if c!= 0:
        es[u].add(v)
    cost[u][v]+=c

#フォードファッカーソン法
ans = 0
def flow(s,goal):
    global ans
    #BFS用のque
    q = deque()
    q.append((s,float("INF")))
    # 到達済み判定用
    used  = [False]*V
    used[s] = True
    #ルート
    route = [0 for i in range(V)]
    route[s] = -1

    #BFS
    while len(q)>0:
        s,flow = q.pop()
        for t in es[s]:
            if not used[t]:
                flow = min(flow,cost[s][t])
                route[t] = s
                q.append((t,flow))
                used[t] = True
                if t == goal:
                    ans += flow
                    break
        else:
            #もしbreakしなかったらwhile文の先頭まで戻る
            continue
        break
    else:
        return False

    #辺の更新
    t = goal
    s = route[t]
    while s!=-1:
        #s-tのコスト減少
        cost[s][t] -=flow
        if cost[s][t] == 0:
            es[s].remove(t)
        #t-sのコスト
        if cost[t][s]==0:
            es[t].add(s)
        cost[t][s] += flow

        t = s
        s = route[t]
    return True


#実行
ans = 0
while True:
    if not flow(s,goal):
        break

print(ans)