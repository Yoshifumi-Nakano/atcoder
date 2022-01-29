S = list(input())
a,b =map(int,input().split())

a_ch = S[a-1]
b_ch = S[b-1]

S[a-1] = b_ch
S[b-1] = a_ch

print("".join(S))
