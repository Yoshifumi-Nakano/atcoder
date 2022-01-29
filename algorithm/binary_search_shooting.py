N = int(input())
H = []
S = []

ng = 0
ok = 0
for i in range(N):
    h,s = map(int,input().split())
    H.append(h)
    S.append(s)
    ok = max(ok,h+s*N)+1

def check(H,S,N,x):
    check_list = [0]*N
    for i in range(N):
        if x - H[i] < 0:
            return False
        check_list[i] = (x-H[i])//S[i]
    check_list.sort()
    for i in range(N):
        if check_list[i] < i:
            return False

    return True



while ok - ng > 1:
    mid = (ok+ng)//2

    #midで達成可能かどうかを調べる
    if check(H,S,N,mid):
        ok = mid
    else:
        ng = mid


print(ok)