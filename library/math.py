##aとbの最大公約数を求める
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
