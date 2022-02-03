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

nil = init()

#ノードpの直後にノードvを挿入する
def insert(v,p):
    v.next = p.next
    p.next.prev = v
    p.next = v
    v.prev = p

n = int(input())
s = list(input())

zero = Node(0)
insert(zero,nil)

now = zero
for i in range(n):
    node = Node(i+1)
    if s[i] == "L":
        insert(node,now.prev)
    else:
        insert(node,now)
    now = node

def printList():
    cur = nil.next
    while True:
        if cur.next == nil:
            print(cur.name)
            exit()
        else:
            print(cur.name,end=" ")
            cur = cur.next




printList()






