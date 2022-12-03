import sys
n, q = map(int, input().split())
a = list(map(int, input().split()))

# BITの実装
id_elem = 0 # 単位元
bit = [id_elem]*n
bit_size = n+1
def update(i, x):
    # i: bitの要素番号(1-indexed)
    # x: bit[i]に対して作用させる値
    while i < bit_size:
        bit[i-1] ^= x
        i += i & -i # 最後の1のビットを加算

def get(i):
    # i: 1~iまでの累積作用結果を取得する(1-indexed)
    ret = id_elem # 単位元で初期化
    while i > 0:
        ret ^= bit[i-1]
        i -= i & -i # 最後の1のビットを減算
    return ret

# BIT構造配列の初期化
for i in range(n):
    update(i+1, a[i])

# クエリ処理
for _ in range(q):
    t, x, y = map(int, sys.stdin.readline().split())

    if t==1:
        update(x, y)
    
    else:
        if x > 1:
            l = get(x-1)
        else:
            l = 0
        r = get(y)
        ans = l ^ r
        print(ans)
