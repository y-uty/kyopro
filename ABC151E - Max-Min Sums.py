n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
MOD = 10**9+7

# Aからk個取り出した集合をS1, S2, ..., Spとすると、
# 求める答えは maxS1 - minS1 + maxS2 - minS2 ... + maxSp - minSp
# よって、(maxSiの総和) - (minSiの総和) であり、max, minを独立に計算してよい

# 最大となる値Xを固定したときのmaxSは、Aに含まれるそれ以下の値の数をmとして X*mCk-1 となる
# Aを予めソートしておけば、固定する最大値を順番に見つつ、まだ見ていないAの要素数がmとなるため
# すぐにmCk-1を求めることができ、これをすべてのiについて足し合わせればOK
# 最小値についても同様
# ただし、0<=m<=N-1についてmCk-1 mod 10^9+7 は前計算が必要

# Cを先に求めておく
class CombMod:
    # 線形時間で 1<=N<=n,r について nCr mod M のテーブルを求める
    def __init__(self, N, mod):
        self.fact = [1, 1]
        self.factinv = [1, 1]
        self.inv = [0, 1]
        self.mod = mod
 
        for i in range(2, N + 1):
            self.fact.append((self.fact[-1] * i) % self.mod)
            self.inv.append((-self.inv[mod % i] * (self.mod // i)) % self.mod)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.mod)
 
    # 計算済みのテーブルから nCr を定数時間で求める
    def cmb(self, n, r):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod

C = CombMod(n, MOD)

ans = 0
for i in range(n):

    # minS
    ans -= a[i] * C.cmb(n-(i+1), k-1)

    # maxS
    ans += a[-1-i] * C.cmb(n-(i+1), k-1)

    ans %= MOD

print(ans)
