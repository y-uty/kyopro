n = int(input())
a = list(map(int, input().split()))
for i in range(n): a[i] += 1

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

anslist = []
ans = 0

# まず、初期状態の転倒数を求める
for i in range(n):
    get_all = get(n)
    get_left = get(a[i])
    ans += get_all - get_left
    update(a[i], 1)

anslist.append(ans)

# 次に、シフトするごとの転倒数を求める
for i in range(n-1):
    ans += (n - a[i]) - (a[i] - 1)
    anslist.append(ans)

print(*anslist, sep='\n')