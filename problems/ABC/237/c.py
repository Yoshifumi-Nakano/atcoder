from collections import deque
s = list(input())
q = deque(s)


while len(q)>1:
    right = q.pop()
    left = q.popleft()
    if right == "a":
        if left !="a":
            q.appendleft(left)
    else:
        if left != right:
            print("No")
            exit()

print("Yes")
