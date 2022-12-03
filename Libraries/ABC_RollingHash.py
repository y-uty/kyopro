def main():
    pass

    # 初期化
    # input_S = input() # 入力文字列S
    # x = RollingHash() 
    # x.Make_HashList(input_S) # S_1~S_|S|のハッシュ値を生成

    # 部分文字列のハッシュ値を計算
    # ans1 = x.GetHash_Substr(a, b)
    # ans2 = x.GetHash_Substr(c, d)


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