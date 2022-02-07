n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]

def dist(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

ans=-1
for i in range(n-1):
    for j in range(i+1,n):
        ans = max(ans,dist(xy[i],xy[j]))

import math
print(math.sqrt(ans))
