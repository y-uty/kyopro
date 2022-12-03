n, a, b = map(int, input().split())

# nC1 + nC2 + ... + nCn = (1+1)^n - nC0 (二項定理より) = 2^n - 1 で計算できる
# n <= 10^9 なので、繰り返し二乗法で求める
ans = 1
MOD = 10**9+7
tmp = 2
for i in range(31): # 29 < log 10^9 < 30

    # nの2進数表示で2^iの桁が1 <=> n and 2^i != 0
    if n & (2**i) != 0:
        ans = (ans * tmp) % MOD

    tmp = (tmp * tmp) % MOD

# nからa, b個選ぶ組み合わせはNGなので、答えは 2^n - 1 - nCa - nCb
# 先に、分母/分子それぞれの階乗部分の余りを計算しておく
nca_si = 1
nca_bo = 1
for i in range(a):
    nca_si = (nca_si * (n-i)) % MOD
    nca_bo = (nca_bo * (i+1)) % MOD

ncb_si = 1
ncb_bo = 1
for i in range(b):
    ncb_si = (ncb_si * (n-i)) % MOD
    ncb_bo = (ncb_bo * (i+1)) % MOD

# 分子/分母 ≡ ? (mod M) <=> 分子*(分母**(M-2)) ≡ ? (mod M)
# よって、モジュラ逆数 分母**(M-2) を繰り返し二乗法で求める
nca_bo_modinv = 1
ncb_bo_modinv = 1
for i in range(31): # 29 < log 10^9 < 30

    # nの2進数表示で2^iの桁が1 <=> n and 2^i != 0
    if (MOD-2) & (2**i) != 0:
        nca_bo_modinv = (nca_bo_modinv * nca_bo) % MOD
        ncb_bo_modinv = (ncb_bo_modinv * ncb_bo) % MOD

    nca_bo = (nca_bo * nca_bo) % MOD
    ncb_bo = (ncb_bo * ncb_bo) % MOD

nca = (nca_si * nca_bo_modinv) % MOD
ncb = (ncb_si * ncb_bo_modinv) % MOD

print((ans - 1 - nca - ncb)%MOD) 