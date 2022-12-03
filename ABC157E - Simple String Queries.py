import sys
n = int(input())
s = list(input())
q = int(input())

# クエリ2で与えられるSの区間に対して各文字が何回登場するかがわかれば
# 一度でも登場する文字の数が、そのクエリの答え
# よって、Sの中身はリストで持ちつつ、文字種ごとにS[i]で使われていれば1とするBITを用意する

# なお、文字種ごとのindexを対応には ord('a')=97 ~ ord('z')=122 を利用する

class BIT():
    def __init__(self, n):
        self.id_elem = 0
        self.bit = [self.id_elem]*n
        self.bit_size = n+1

    def update(self, i, x):
        # i: bitの要素番号(1-indexed)
        # x: bit[i]に対して作用させる値
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

# BITオブジェクトを26個用意
bit_set = []
for _ in range(26):
    bit_obj = BIT(n)
    bit_set.append(bit_obj)

# Sの初期状態の文字ごとの使用状況をBITに反映
for i in range(n):
    x = s[i]
    bit_set[ord(x)-97].update(i+1, 1)

# 一点更新・区間和クエリを処理
for i in range(q):
    q1, q2, q3 = map(str, sys.stdin.readline().split())
    if q1=='1':
        x = s[int(q2)-1]
        if x==q3: continue
        bit_set[ord(x)-97].update(int(q2), -1)
        bit_set[ord(q3)-97].update(int(q2), 1)
        s[int(q2)-1] = q3
    
    else:
        ans = 0
        for j in range(26):
            chk = bit_set[j].get(int(q3)) - bit_set[j].get(int(q2)-1)
            if chk > 0: ans += 1
        print(ans)
