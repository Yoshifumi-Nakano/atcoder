class Heap:
    def __init__(self):
        self.heap = []

    def push(self,x):
        self.heap.append(x)
        i = len(self.heap)-1
        while i > 0:
            #親の頂点番号
            p = (i-1)//2
            if self.heap[p] >= x:
                break
            #自分の値を親の値にする
            self.heap[i] = self.heap[p]
            i = p
        #最終的にxはiの位置にいく
        self.heap[i] = x

    #最大値の取り出し
    def top(self):
        if len(self.heap) != 0:
            return self.heap[0]

    #最大値の削除
    def pop(self):
        if len(self.heap) == 0:
            return
        #頂点に持っていく値
        x = self.heap[-1]
        self.heap.pop()
        i = 0
        while i*2 +1 < len(self.heap):
            #子頂点同士を比較して大きい方をchild1にする
            child1 = i*2+1
            child2 = i*2+2
            if child2 < len(self.heap) and self.heap[child1] < self.heap[child2]:
                child1 =child2
            if self.heap[i] <= x:
                break
            self.heap[i] = self.heap[child1]
            i = child1

        self.heap[i] = x

h = Heap()
h.push(5)
h.push(3)
h.push(7)
h.push(2)
print(h.top())
h.pop()
print(h.top())





