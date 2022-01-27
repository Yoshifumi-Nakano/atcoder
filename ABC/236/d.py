N = int(input())
A = [[0]*(i+1)+list(map(int,input().split())) for i in range(2*N-1)]

used = [False]*2*N
comb = []

def calc():
    if len(comb) == N:
        ret = 0
        for co in comb:
            i,j = co
            ret = ret ^ A[i][j]
        return ret

    for i in range(2*N):
        if not used[i]:
            first = i
            break
    used[first] = True

    ret = 0
    for i in range(2*N):
        if not used[i]:
            comb.append((first,i))
            used[i] = True
            ret = max(ret,calc())
            comb.pop()
            used[i] = False
    used[first] = False
    return ret

print(calc())

