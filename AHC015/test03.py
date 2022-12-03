def main():
    # sys.stdin = open('./in01.txt', 'r')
    sys.stdout = open('./out01.txt', 'w')

    # 事前情報: キャンディの種類
    F = list(map(int, input().split()))
    # 種類ごとの個数
    Fcnt = collections.defaultdict(int)
    for f in F: Fcnt[f] += 1

    # 一番多いのは右上に、それ以外はランダムに
    Fnum = []
    for k, v in Fcnt.items():
        Fnum.append((v, k))
    Fnum.sort(reverse=True)

    No1num = Fnum[0][1]

    # 番号ごとの方向
    Dir = ['F', 'B', 'L']

    for i in range(100):
        if F[i]==No1num:
            print('R')

        else:
            d = random.randint(0, 2)
            print(Dir[d])

class CandyBox():
    # キャンディ箱の初期化
    def __init__(self, masu_given):
        # 空きが0~99
        # キャンディありは、10**f+(0~99)
        self.masu = masu_given
        # 空きマス番号 to マスの座標
        self.blank_place = collections.defaultdict(int)
        for i in range(100): self.blank_place[i] = (i//10, i%10)


    # 入力piに従って、箱にキャンディを詰める
    def Put_Candy(self, put_r, put_c, input_count, f):
        input_count -= 1
        self.masu[put_r][put_c] = f*100+input_count

    # 空きマス番号の振り直し
    def ReIndex(self):
        BlankNo = 0 # 空きマスに左上から降っていく通し番号
        for i in range(10):
            for j in range(10):
                if self.masu[i][j] < 100:
                    self.masu[i][j] = BlankNo
                    self.blank_place[BlankNo] = (i, j)
                    BlankNo += 1 

    # FBLR方向へ傾けるときの箱の状態の更新
    def Tilt(self, direction):
        if direction=='R':
            # 各行について、キャンディを一通りかき集めて、それを端から詰めていく
            for i in range(10):
                Candies = []
                for j in range(10):
                    x = self.masu[i][j] 
                    if x >= 100: Candies.append(x)
                # キャンディは右から
                for j in range(len(Candies)):
                    self.masu[i][-1-j] = Candies[-1-j]
                for j in range(10-len(Candies)):
                    self.masu[i][j] = 0

        elif direction=='L':
            for i in range(10):
                Candies = []
                for j in range(10):
                    x = self.masu[i][j] 
                    if x >= 100: Candies.append(x)
                # Lと逆から
                for j in range(len(Candies)):
                    self.masu[i][j] = Candies[j]
                for j in range(10-len(Candies)):
                    self.masu[i][-1-j] = 0

        elif direction=='F':
            # 各列について、キャンディを一通りかき集めて、それを端から詰めていく
            # その後、空きマスに順番に番号を振る
            for j in range(10):
                Candies = []
                for i in range(10):
                    x = self.masu[i][j]
                    if x >= 100: Candies.append(x)
                # キャンディは上から
                for i in range(len(Candies)):
                    self.masu[i][j] = Candies[i]
                for i in range(10-len(Candies)):
                    self.masu[-1-i][j] = 0

        elif direction=='B':
            for j in range(10):
                Candies = []
                for i in range(10):
                    x = self.masu[i][j]
                    if x >= 100: Candies.append(x)
                # Fと逆から
                for i in range(len(Candies)):
                    self.masu[-1-i][j] = Candies[-1-i]  
                for i in range(10-len(Candies)):
                    self.masu[i][j] = 0 

        # その後、空きマスに順番に番号を振る
        self.ReIndex()


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return 0
        if self.parents[x] > self.parents[y]: x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return 1
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)

if __name__=='__main__':
    import sys
    import random
    import collections
    import copy

    main()