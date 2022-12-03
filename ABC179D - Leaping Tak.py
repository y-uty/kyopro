n, k = map(int, input().split())
rng = [list(map(int, input().split())) for _ in range(k)]

# BITの実装
# 1-indexedは内部で行うので、BITとして扱いたい配列の長さがNなら
# 「長さNに対する1~N番目の要素」の感覚で使ってやればOK
id_elem = 0 # 単位元 +:0, *:1, ^:0
bit = [id_elem]*n
bit_size = n+1
def update(i, x):
    # i: bitの要素番号(1-indexed)
    # x: bit[i]に対して作用させる値
    while i < bit_size:
        bit[i-1] += x
        # bit[i-1] *= x
        # bit[i-1] ^= x
        i += i & -i # 最後の1のビットを加算

def get(i):
    # i: 1~iまでの累積作用結果を取得する(1-indexed)
    ret = id_elem # 単位元で初期化
    while i > 0:
        ret += bit[i-1]
        # ret *= bit[i-1]
        # ret ^= bit[i-1]
        i -= i & -i # 最後の1のビットを減算
    return ret

# BIT構造配列の初期化
update(1, 1)

MOD = 998244353
# BITの区間和で貰うDP
for i in range(2, n+1):

    for j in range(k):
        l, r = rng[j]
        from_L = i-r
        from_R = i-l
        if from_R <= 0: continue
        from_L = max(1, i-r)
        rng_sum = get(from_R) - get(from_L-1)

        update(i, rng_sum%MOD)

print((get(n)-get(n-1))%MOD)