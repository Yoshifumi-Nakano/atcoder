N = int(input())
W = int(input())
a = list(map(int,input().split()))

##部分和問題を再起関数を用いてとく
##func(i,S):aの最初のi個を用いてSを作ることができるか
def func(i,S,a):
    if i==0:
        if S==0:
            return True
        else:
            return False

    if func(i-1,S,a):
        return True

    if func(i-1,S-a[i-1],a):
        return True

    return False

print(func(N,W,a))