## ライブラリのimport ##
import sys
import collections

class UnionFind():
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent.
        # To show, write print(uf.parents).
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # path compression; search for root, and connect to each parent.
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # If not yet; return 1(Done), already; return 0(Nothing).
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # union by rank;
        #  connect less-depth group to higher-depth one not to increase max-depth.
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return 1

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


## 入力 ##
N, K = map(int, input().split())
# N*Nマスからなるサーバルームの初期状態
Room = []
# コンピュータの識別番号表(Computers[CP_id]=CP_div)
Computers = []
CP_id = 0 # サーバID: 0~100K-1
for _ in range(N):
    in_record = list(str(sys.stdin.readline().replace('\n', '')))
    for j in range(N):
        CP_div = int(in_record[j]) # サーバ種類番号: 1~K
        # サーバ種類番号 * 1000 + サーバID の4桁で情報を持つ
        if CP_div > 0:
            CP_cell = CP_div*1000+CP_id
            in_record[j] = CP_cell
            Computers.append(CP_div)
            CP_id += 1
        else:
            in_record[j] = 0
    Room.append(in_record)

## 出力用の変数 ##
X, Move_out    = 0, [] # 移動
Y, Connect_out = 0, [] # 接続

## 状態管理用の変数 ##
Clusters = UnionFind(100*K)

## 初期状態で可能な接続を行う (移動はしない) ##
# 移動ベクトル [Right, Down]
# v_row = [0, 1]
# v_col = [1, 0]

# 右方向へ、接続できるコンピュータの探索
for i in range(N):
    for j in range(N):
        cell_self= Room[i][j]
        # セルにコンピュータがある場合、右へ同種探索
        if cell_self > 0:
            move_to_search = 1
            while j+move_to_search < N: # はみ出るまで
                cell_next = Room[i][j+move_to_search]

                if cell_next < 0: # ケーブルに衝突
                    break # 何もせず次のセルへ
                
                elif cell_next > 0: # コンピュータを発見
                    CP_div_self, CP_id_self = divmod(cell_self, 1000)
                    CP_div_next, CP_id_next = divmod(cell_next, 1000)

                    if CP_div_self==CP_div_next: # 同種の場合、接続する
                        # 同一クラスタへの結合
                        Clusters.union(CP_id_self, CP_id_next)
                        # ケーブルの敷設
                        for k in range(j+1, j+move_to_search):
                            Room[i][k] = -CP_div_self # ケーブルが接続している種類の識別
                        # 接続情報の出力生成
                        Y += 1
                        Connect_out.append([i, j, i, j+move_to_search])

                        # 処理終了、次のセルへ
                        break
                    
                    else: # 異種の場合、何もせず次のセルへ
                        break

                else: # 空きセル
                    move_to_search += 1 # さらに右へ


# 下方向へ、接続できるコンピュータの探索
for i in range(N):
    for j in range(N):
        cell_self= Room[i][j]
        # セルにコンピュータがある場合、下へ同種探索
        if cell_self > 0:
            move_to_search = 1
            while i+move_to_search < N: # はみ出るまで
                cell_next = Room[i+move_to_search][j]

                if cell_next < 0: # ケーブルに衝突
                    break # 何もせず次のセルへ
                
                elif cell_next > 0: # コンピュータを発見
                    CP_div_self, CP_id_self = divmod(cell_self, 1000)
                    CP_div_next, CP_id_next = divmod(cell_next, 1000)

                    if CP_div_self==CP_div_next: # 同種の場合、接続する
                        # 同一クラスタへの結合
                        Clusters.union(CP_id_self, CP_id_next)
                        # ケーブルの敷設
                        for k in range(i+1, i+move_to_search):
                            Room[k][j] = -CP_div_self # ケーブルが接続している種類の識別
                        # 接続情報の出力生成
                        Y += 1
                        Connect_out.append([i, j, i+move_to_search, j])

                        # 処理終了、次のセルへ
                        break
                    
                    else: # 異種の場合、何もせず次のセルへ
                        break

                else: # 空きセル
                    move_to_search += 1 # さらに右へ


## 得点計算 ##
# 各コンピュータがどのクラスタに接続されているかはUnion-Find森が持っている
# (i, j)の組を総当りで得点を計算する
Score = 0
for i in range(100*K-1):
    for j in range(i+1, 100*K):
       # print(i, j, Clusters.same(i, j), Computers[i], Computers[j])
        if Clusters.same(i, j):
            Score += 1 if Computers[i]==Computers[j] else -1

## 出力 ##
# print(X)
# for ans in Move_out: print(*ans)
# print(Y)
# for ans in Connect_out: print(*ans)
# debug
print(Score)


sys.stdout = open('./test001-out.txt', 'w')
print(X)
for ans in Move_out: print(*ans)
print(Y)
for ans in Connect_out: print(*ans)
sys.stdout = sys.__stdout__
