class UnionFind:
    def __init__(self,N):
        self.par = [-1]*N
        self.size = [1]*N

    #根を求める
    def root(self,x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    #xとyが同じグループか
    def issame(self,x,y):
        return self.root(x) == self.root(y)

    #xのグループとyのグループを併合する
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)

        if x==y:
            return
        #yの方を小さくする
        if self.size[x] < self.size[y]:
            x,y = y,x

        self.par[y] = x
        self.size[x] += self.size[y]
        return True

    def size(self,x):
        return self.size[self.root(x)]

#辺を重みが小さい順にsort
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
es = []
for i in range(n):
    for j in range(n):
        if a[i][j]!=-1:
            es.append([a[i][j],i,j])
            es.append([a[i][j],j,i])
es = sorted(es, key=lambda x: x[0])

#クラスカル法
uf = UnionFind(n)
res = 0
for w,i,j in es:
    if uf.issame(i,j):
        continue
    uf.unite(i,j)
    res += w
print(res)