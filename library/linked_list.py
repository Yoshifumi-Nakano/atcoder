#アルゴリズムとデータ構造をpythonのコードに直したもの

#連結リストの一つ一つのNode
class Node:
    def __init__(self,name):
        self.prev = None
        self.next = None
        self.name = name


#初期化
def init():
    nil = Node("nil")
    nil.next = nil
    nil.prev = nil
    return nil

#グローバル領域においておく
nil = init()

#連結リストの出力
def printList():
    cur = nil.next
    while (cur != nil):
        print(cur.name)
        cur = cur.next

#ノードpの直後にノードvを挿入する
def insert(v,p):
    v.next = p.next
    p.next.prev = v
    p.next = v
    v.prev = p

#ノードvの削除
def erase(v):
    if (v==nil):
        return
    v.prev.next = v.next
    v.next.prev = v.prev
    del v


names = ["yamamoto","watanabe","ito","takahashi","suzuki","sato"]

for i in range(len(names)):
    node = Node(names[i])
    insert(node,nil)

    if names[i]=="watanabe":
        watanabe = node

print(printList())
erase(watanabe)
print(printList())









