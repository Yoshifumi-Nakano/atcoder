n,q = map(int,input().split())
a = list(map(int,input().split()))

#前処理
dic = {}
for i in range(n):
    if a[i] in dic.keys():
        dic[a[i]].append(i+1)
    else:
        dic[a[i]] = [i+1]

#Query処理
for i in range(q):
    x,k = map(int,input().split())
    if x not in dic.keys():
        print(-1)
        continue
    x_list = dic[x]
    if len(x_list) < k:
        print(-1)
        continue
    print(x_list[k-1])



