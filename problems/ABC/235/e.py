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


n,m,q = map(int,input().split())
es = []
for i in range(m):
    a,b,c = map(int,input().split())
    es.append([c,a-1,b-1,-1])
    es.append([c,b-1,a-1,-1])

for i in range(q):
    u,v,w = map(int,input().split())
    es.append([w,u-1,v-1,i])
    es.append([w,v-1,u-1,i])

es = sorted(es,key=lambda x:x[0])

uf = UnionFind(n)
ans = [0]*q
for w,u,v,index in es:
    if index == -1:
        if uf.issame(u,v):
            continue
        uf.unite(u,v)
    else:
        if uf.issame(u,v):
            ans[index] = "No"
        else:
            ans[index] = "Yes"

for an in ans:
    print(an)

