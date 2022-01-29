N = int(input())
A = list(map(int,input().split()))

from collections import Counter

dic = Counter(A)

for key in dic:
    if dic[key] == 3:
        print(key)
        exit()
