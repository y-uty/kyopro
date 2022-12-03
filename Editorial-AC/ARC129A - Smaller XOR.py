n, l, r = map(int, input().split())

# Nとどれかひとつでも1が立つビットが同じ場合、
# N^x でそのビットが0になり、元のNより小さくなる

# xのビット列長kを固定すれば、
# xの最上位ビットが1である数、すなわち2^(k-1) ~ 2^k-1 (k=3なら4~7)1が
# 条件を満たすかどうかは、Nの同じ桁が1であるかどうかである

# よって、xの桁数kに対する範囲は、あとはL以上R以下も共に満たせばよく、
# max(2^(k-1), L) <= x <= min(2^k-1, R) となるxである

nbin = bin(n)[2:]
nbin_len = len(nbin)
ans = 0

for i in range(nbin_len):
    if nbin[-1-i]=='1':
        lower_limit = max(2**i, l)
        upper_limit = min(2**(i+1)-1, r)
        # 上限/下限の大小が逆転する場合に注意！
        ans += max(upper_limit-lower_limit+1, 0)

print(ans)