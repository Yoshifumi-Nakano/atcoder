x = int(input())

ans = []
#初項
for a in range(1,10):
    #交差
    for d in range(-9,10):
        ans.append(a)
        k = a
        pre  = a
        while k < 10**17:
            pre+=d
            if pre <0 or pre >9:
                break
            k = k*10+pre
            ans.append(k)
ans.sort()
for i in range(len(ans)):
    if ans[i] >=x:
        print(ans[i])
        exit()


