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
