# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=ja

#V：頂点数、E：辺数, r:始点
V,E,r = map(int,input().split())

#辺のリスト
es = []
for i in range(E):
    s_,t_,w_ = map(int,input().split())
    es.append((s_,t_,w_))

#ベルマンフォード
def bellmanford(r):
    d = [float("INF")]*V
    d[r] = 0

    negative = False
    for i in range(V):
        update = False
        for s,t,w in es:
            #無限大の始点からは緩和をする必要はない
            if d[s] == float("INF"):
                continue

            #緩和が起これば更新
            if d[s] + w < d[t]:
                d[t] = d[s] + w
                update = True

        #更新が行われなければ終了
        if not update:
            break

        #負閉路検出
        if i==V-1 and update:
            negative = True
            break

    if negative:
        print("NEGATIVE CYCLE")
    else:
        for ans in d:
            if ans == float("INF"):
                print("INF")
            else:
                print(ans)

#実行
bellmanford(r)







