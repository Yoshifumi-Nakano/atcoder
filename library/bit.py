## bit全探索： https://qiita.com/gogotealove/items/11f9e83218926211083a
def create_bit(N):
    bit_list = []
    for i in range(2**N):
        bit=[]
        for j in range(N):
            bit.append(i >> j & 1)
        bit_list.append(bit)
    return bit_list