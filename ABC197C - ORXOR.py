n = int(input())
a = list(map(int, input().split()))

ans = 2**30

# O(2^N * N) ≒ 10^7 なのでPyPyでギリbit全探索で通す
for i in range(2**n):
    a_bit = format(i, '0'+str(n)+'b')
    or_ = 0
    xor_ = 0
    prebit = a_bit[0]
    for j in range(n):
        if a_bit[j] == prebit:
            or_ |= a[j]
        else:
            xor_ ^= or_
            or_ = a[j]
        
        # print(or_, xor_)
        prebit = a_bit[j]

    xor_ ^= or_

    if xor_ < ans:
        ans = xor_

print(ans)