N = int(input())
W = int(input())
A = list(map(int,input().split()))

def create_bit(N):
    bit_list = []
    for i in range(2**N):
        bit=[]
        for j in range(N):
            bit.append(i >> j & 1)
        bit_list.append(bit)
    return bit_list

#N個の配列が与えられてその中から何個かの整数を選んで和をWにすることができるどうか
bit_list = create_bit(N)
ans=False

for bit in bit_list:
    S = 0
    for j in range(N):
        if bit[j]:
            S+=A[j]

    if S == W:
        ans = True

print(ans)