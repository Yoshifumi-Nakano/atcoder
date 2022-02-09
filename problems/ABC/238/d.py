t = int(input())
import math
for i in range(t):
    a,s = map(int,input().split())

    #高々dは60
    d = len(str(bin(s)))-1
    x = 0
    for i in range(d+1):
        if a >> i & 1:
            x += int(math.pow(2,i))
    y = s-x
    if y < 0:
        print("No")
        continue
    if x & y == a:
        print("Yes")
    else:
        print("No")
