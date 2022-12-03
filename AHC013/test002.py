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
# コンピュータの識別番号表(Computers_id_div[CP_id]=CP_div)
Computers_id_div = []
# コンピュータの座標管理
Computers_position = []
CP_id = 0 # サーバID: 0~100K-1
for i in range(N):
    in_record = list(str(sys.stdin.readline().replace('\n', '')))
    for j in range(N):
        CP_div = int(in_record[j]) # サーバ種類番号: 1~K
        # サーバ種類番号 * 1000 + サーバID の4桁で情報を持つ
        if CP_div > 0:
            CP_cell = CP_div*1000+CP_id
            in_record[j] = CP_cell
            Computers_id_div.append(CP_div)
            CP_id += 1

            Computers_position.append([i, j])
        else:
            in_record[j] = 0
    Room.append(in_record)

## 出力用の変数 ##
X, Move_out    = 0, [] # 移動
Y, Connect_out = 0, [] # 接続

## 状態管理用の変数 ##
Clusters = UnionFind(100*K)

## 初期状態で可能な接続を行う (移動はしない) ##
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
                            # ケーブルが接続している種類の識別と、接続情報番号を記録
                            Room[i][k] = -1 * (CP_div_self*1000 + len(Connect_out))
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
                            # ケーブルが接続している種類の識別と、接続情報番号を記録
                            Room[k][j] = -1 * (CP_div_self*1000 + len(Connect_out))
                        # 接続情報の出力生成
                        Y += 1
                        Connect_out.append([i, j, i+move_to_search, j])

                        # 処理終了、次のセルへ
                        break
                    
                    else: # 異種の場合、何もせず次のセルへ
                        break

                else: # 空きセル
                    move_to_search += 1 # さらに右へ

# for c, d in enumerate(Connect_out): print(c, d) 


## 移動と再接続 ##
# クラスタに所属していないコンピュータを、上下左右1マス移動させて接続可能ならする
# 他のコンピュータがどいた結果、別種が接続可能になる場合もあるので、種類ごとにループ
# 始点として全座標を探索すると2*10^6となるので、コンピュータがいる座標(<=500)のみを始点とする
# 移動ベクトル[右, 下, 左, 上]
v_row = [0, -1,  0, 1] # 縦方向
v_col = [1,  0, -1, 0] # 横方向
for div in range(1, K+1):
    for id in range(100*K):

        # あるコンピュータ始点で移動と再接続の探索をしようとする時点で100K-(X+Y)<2であればこれ以上できないので終了
        if 100*K - (X+Y) < 2: break  # ただし、divループは回り続けてしまう      

        # 探索中の種類で、かつどのクラスタにも接続していないコンピュータ
        if Computers_id_div[id]==div and Clusters.parents[id]==-1:
            # コンピュータの座標を取得
            row_self, col_self = Computers_position[id]
            for i in range(len(v_row)):
                row_search, col_search = row_self+v_row[i], col_self+v_col[i]
                # 移動先を探索 Roomからはみ出ないように
                if row_search >= 0 and row_search < N and col_search >= 0 and col_search < N:
                    
                    if ( Room[row_search][col_search] < 0 and 
                            (-1 * Room[row_search][col_search])//1000 == div): #　同種クラスタのケーブル

                        # print(Computers_position[id], Room[row_search][col_search], len(Connect_out)) ### debug ###

                        # X, Yを加算した後に100Kを超える場合はNG
                        add_X, add_Y = abs(v_row[i])+abs(v_col[i]), 1        
                        if X+Y+add_X+add_Y > 100*K: continue

                        #　移動させる
                        Con_info_index =(-1 * Room[row_search][col_search])%1000
                        Room[row_search][col_search] = Room[row_self][col_self]
                        Room[row_self][col_self] = 0
                        Computers_position[id] = [row_search, col_search]
                        # 移動情報の保存
                        Move_out.append([row_self, col_self, row_search, col_search])
                        X += add_X

                        # ケーブルを接続し直す
                        # 元の接続情報を探して分解
                        Con_bef_1r, Con_bef_1c, Con_bef_2r, Con_bef_2c = Connect_out[Con_info_index]

                        # ケーブル情報の更新(新たに接続したコンピュータの右側or下側のケーブル)
                        if i in {1, 3}: # 縦移動してきた場合、右側にあるケーブル
                            for j in range(col_search+1, Con_bef_2c):
                                Room[row_search][j] = -1 * (div*1000 + len(Connect_out))
                        else: # 横移動してきた場合、下側にあるケーブル
                            for j in range(row_search+1, Con_bef_2r):
                                Room[j][col_search] = -1 * (div*1000 + len(Connect_out))

                        # 再度保存する
                        Connect_out[Con_info_index] = [Con_bef_1r, Con_bef_1c, row_search, col_search]
                        Connect_out.append([row_search, col_search, Con_bef_2r, Con_bef_2c])

                        # print(row_search, col_search, Con_bef_2r, Con_bef_2c)

                        Y += 1
                        # 同一クラスタに所属させる
                        Clusters.union(Room[Con_bef_1r][Con_bef_1c]%1000, id)
                        
                        
                        # # その始点から移動する先が見つかった場合は、次の始点へ
                        break # for i ~~ を抜ける


## 得点計算 ##
# 各コンピュータがどのクラスタに接続されているかはUnion-Find森が持っている
# (i, j)の組を総当りで得点を計算する
Score = 0
for i in range(100*K-1):
    for j in range(i+1, 100*K):
        # print(i, j, Clusters.same(i, j), Computers[i], Computers[j])
        if Clusters.same(i, j):
            Score += 1 if Computers_id_div[i]==Computers_id_div[j] else -1


## 出力 ##
print(X)
for ans in Move_out: print(*ans)
print(Y)
for ans in Connect_out: print(*ans)


# # local test
# print(Score)
# # test
# sys.stdout = open('./test001-out.txt', 'w')
# print(X)
# for ans in Move_out: print(*ans)
# print(Y)
# for ans in Connect_out: print(*ans)
# sys.stdout = sys.__stdout__
