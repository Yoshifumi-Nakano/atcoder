k = int(input())


from collections import deque
ans = deque([])

while k > 1:
    r = k%2
    k = k//2
    if r==0:
        ans.appendleft(0)
    else:
        ans.appendleft(2)

ans.appendleft(2)
ans = list(map(str,list(ans)))


print("".join(ans))

