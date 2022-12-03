def main():
    import collections
    n = int(input())

    input_S = input() # 入力文字列S
    x = RollingHash() 
    x.Make_HashList(input_S) # S_1~S_|S|のハッシュ値を生成

    # K文字で、重ならない連続部分文字列が作れるとき、K文字未満でも必ず作れる
    # よって、作れる連続部分文字列の長さの最大値を二分探索で求める
    # 計算量はハッシュ値計算O(1), 一回のis_okあたりO(N)で、全体でO(NlogN)

    # 長さlensubの連続部分文字列が存在するかの判定
    def is_ok(lensub):
        hash_rpos = collections.defaultdict(int)

        for l in range(1, n-lensub+2):

                r = l+lensub-1
                get_hash = x.GetHash_Substr(l, r)
                minr = hash_rpos[get_hash]
                if minr==0:
                    hash_rpos[get_hash] = r
                else:
                    if minr < l:
                        return True

        return False                    

    # 二分探索で最大値を求める
    ok, ng  = 0, n+1
    def bin_srch_mgr(ok, ng):
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            if is_ok(mid): ok = mid
            else: ng = mid
        return ok

    ans = bin_srch_mgr(ok, ng)
    print(ans)

class RollingHash:
  
    def __init__(self):
        self.MOD = 2**61 - 1
        self.lenS = 0
        self.B = 10007
        self.HashList = None
        self.BasePow = None
    
    def Make_HashList(self, S):

        self.lenS = len(S)

        # S[1, i]のハッシュHiを前計算
        self.HashList = [0]
        for i in range(self.lenS):
            Hi = (self.B * self.HashList[i] + ord(S[i]))%self.MOD
            self.HashList.append(Hi)

        # Bの冪乗の前計算
        self.BasePow = [1]
        Bpow = 1
        for i in range(self.lenS):
            Bpow = Bpow*self.B%self.MOD
            self.BasePow.append(Bpow)

    # S[l, r]のハッシュを求める
    def GetHash_Substr(self, l, r):
        return (self.HashList[r] - self.BasePow[r-(l-1)]*self.HashList[l-1])%self.MOD

if __name__=='__main__':
    main()
