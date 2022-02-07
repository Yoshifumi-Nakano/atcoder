n,k = map(int,input().split())
p=list(map(int,input().split()))

import heapq
q = []

#k個ある
for i in range(k):
    heapq.heappush(q,p[i])
m = heapq.heappop(q)
print(m)
heapq.heappush(q,m)


for i in range(k,n):
    m = heapq.heappop(q)
    if p[i] >= m:
        heapq.heappush(q,p[i])
        l = heapq.heappop(q)
        print(l)
        heapq.heappush(q,l)
    else:
        heapq.heappush(q,m)
        print(m)










# stock = []
# hash = set()
# ans = 0

# for i in range(n,k-1,-1):
#     if i == n:
#         stock.append(n-k+1)
#         ans = n-k+1
#     else:
#         hash.add(p[i])
#         if p[i] >=ans:
#             while True:
#                 ans-=1
#                 if ans not in hash:
#                     stock.append(ans)
#                     break
#         else:
#             stock.append(ans)

# for i in range(len(stock)-1,-1,-1):
#     print(stock[i])

