n,q = map(int,input().split())


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

uf = UnionFind(n+1)
for i in range(q):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    uf.unite(l,r+1)

if uf.issame(0,n):
    print("Yes")
else:
    print("No")

