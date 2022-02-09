n = int(input())
digit = len(str(n))

def nine(digit):
    if digit ==1:
        return 0
    k = ["9"]
    for i in range(digit-1):
        k.append("0")
    return int("".join(k))


def onezero(digit):
    k = ["1"]
    for i in range(digit-1):
        k.append("0")
    return int("".join(k))

ans = 0
for i in range(1,digit):
    if i == 1:
        ans += 45
    ans = (ans+nine(i)*(nine(i)+1)//2)%998244353


ans = (ans + (n-onezero(digit)+1)*(n-onezero(digit)+2)//2)%998244353

print(ans%998244353)