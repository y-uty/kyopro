N = int(input())
A = list(map(int, input().split()))

class BIT():
    def __init__(self, n, id_elem=0):
        self.id_elem = id_elem
        self.bit = [id_elem]*n
        self.bit_size = n+1

    def add(self, i, x):
        # i: bitの要素番号(1-indexed)
        while i < self.bit_size:
            self.bit[i-1] += x
            i += i & -i # 最後の1のビットを加算

    def get(self, i):
        # i: 1~iまでの累積作用結果を取得する(1-indexed)
        ret = self.id_elem # 単位元で初期化
        while i > 0:
            ret += self.bit[i-1]
            i -= i & -i # 最後の1のビットを減算
        return ret

bit = BIT(N)
ans = 0
for i in range(N):
    get_all = bit.get(N)
    get_left = bit.get(A[i])
    ans += get_all - get_left
    bit.add(A[i], 1)

print(ans)