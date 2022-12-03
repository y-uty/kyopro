def main():
    # sys.stdin = open('./in01.txt', 'r')
    sys.stdout = open('./out01.txt', 'w')

    # 事前情報: キャンディの種類
    F = list(map(int, input().split()))
    # 種類ごとの個数
    Fcnt = collections.defaultdict(int)
    for f in F: Fcnt[f] += 1

    # 傾ける方向
    Directions = ['F', 'B', 'L', 'R']
    # サーチする方向: 右と下だけ
    vr = [0, 1]
    vc = [1, 0]
    
    # スコアの分母
    Score_Div = 0
    for _, v in Fcnt.items(): Score_Div += v**2
    # 現在の盤面のスコアを求める
    def Calculate_Score(masu):
        uf = UnionFind(100)
        for i in range(100): # 左上から順番に、右と下だけ連結しているか調べる
            from_r, from_c = i//10, i%10
            for j in range(2):
                to_r, to_c = from_r+vr[j], from_c+vc[j]
                if to_r < 10 and to_c < 10: # はみでない
                    # 隣が同じ種類なら、連結する
                    if masu[from_r][from_c] > 100:
                        from_type = masu[from_r][from_c]//100
                        to_type = masu[to_r][to_c]//100
                        if from_type==to_type:
                            uf.union(i, to_r*10+to_c)
        sc = 0
        for i in range(100):
            if uf.parents[i] < 0:
                sc += uf.parents[i]**2
        
        return 10**6 * (sc / Score_Div)


    # 初期状態を生成
    Box = [list(range(10*i, 10*i+10)) for i in range(10)]

    for i in range(1, 101):

        pi = int(input())
        pi -= 1

        Eval = [] # 'F', 'B', 'L', 'R'
        Box_Tilt_FBLR = []
        for _ in range(4):
            B = CandyBox(Box)
            Box_Tilt_FBLR.append(B)
        for j in range(4):

            Box_Tilt = Box_Tilt_FBLR[j]

            # pがどこの空きマスか見つける
            break_flag = False
            for r in range(10):
                for c in range(10):
                    if Box_Tilt.masu[r][c]==pi:
                        break_flag = True
                        break
                if break_flag: break
            # キャンディを入れる
            Box_Tilt.Put_Candy(r, c, i, F[i-1])
            # 傾ける
            Box_Tilt.Tilt(Directions[j])
            # スコアを計算
            Eval.append((Calculate_Score(Box_Tilt.masu), j))

        # 最もスコアが高い方向を選ぶ
        Eval.sort()
        # print(Eval)
        print(Directions[Eval[-1][1]])
        sys.stdout.flush()

        # その盤面を記録して、次へ
        Box = copy.deepcopy(Box_Tilt_FBLR[j].masu)


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
    import collections
    import copy

    main()