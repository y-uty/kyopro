def main(in_path='./test005-in.txt', out_path='./test-out.txt'):

    ## ライブラリのimport ##
    import sys
    import random
    random.seed(0) # 乱数シードの固定
    import copy

    #### やきなまし法 ####
    # 山登り法 + 温度関数 + 遷移確率関数
    # 1. 初期状態- > 入力から受け取った状態のRoom
    # 2. スコア計算関数 -> 問題で与えられてた通りの計算を全点対で行って素直に計算
    # 3. 遷移関数 -> コンピュータの移動 未接続で移動させるので、衝突さえなければ
    # 任意のコンピュータを任意の方向へ移動させることができる
    # スコアがよくなったら確定し、座標の更新と出力情報の格納を行う
    # 4. 温度関数 -> start_temp, end_tmp = (1遷移で動きうるスコア幅のMax, Min程度)
    # temp = (線形でstart_tempからend_tempに減少する)
    # 5. 遷移確率関数 -> prob = exp((new_score-pre_score)/temp)

    sys.stdin = open(in_path, 'r')


    ## 入力 ##
    N, K = map(int, input().split())
    # 配置されるコンピュータの数
    Computers_num = 100*K

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
    X, Move_out = 0, [] # 移動

    ### ケーブルの接続 ###
    def Connection(): 
        Y, Connect_out = 0, []
        ## 得点計算 ##
        # 各コンピュータがどのクラスタに接続されているかはUnion-Find森が持っている
        # (i, j)の組を総当りで得点を計算する
        # 同種のコンピュータした接続されていないことを前提に、計算を高速化する
        # Clusters.parentsでroot -> (そのクラスタのコンピュータ数)C2を加算
        def Calculate_ver2(Clusters):
            Score = 0
            for rt in Clusters.parents:
                if rt < -1: Score += rt*(rt+1)//2 # nC2
            return Score

        ## 状態管理用の変数 ##
        Clusters = UnionFind(Computers_num)
        ## 接続用にRoomをコピー ##
        Room_Connect = copy.deepcopy(Room)
        ## 接続情報出力用の変数初期化 ##
        
        # 右方向へ、接続できるコンピュータの探索
        for i in range(N):
            for j in range(N):
                cell_self= Room_Connect[i][j]
                # セルにコンピュータがある場合、右へ同種探索
                if cell_self > 0:
                    move_to_search = 1
                    while j+move_to_search < N: # はみ出るまで
                        cell_next = Room_Connect[i][j+move_to_search]

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
                                    Room_Connect[i][k] = -1 * (CP_div_self*1000 + len(Connect_out))
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
                cell_self= Room_Connect[i][j]
                # セルにコンピュータがある場合、下へ同種探索
                if cell_self > 0:
                    move_to_search = 1
                    while i+move_to_search < N: # はみ出るまで
                        cell_next = Room_Connect[i+move_to_search][j]

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
                                    Room_Connect[k][j] = -1 * (CP_div_self*1000 + len(Connect_out))
                                # 接続情報の出力生成
                                Y += 1
                                Connect_out.append([i, j, i+move_to_search, j])

                                # 処理終了、次のセルへ
                                break
                            
                            else: # 異種の場合、何もせず次のセルへ
                                break

                        else: # 空きセル
                            move_to_search += 1 # さらに右へ

        Score = Calculate_ver2(Clusters)
        return Score, Y, Connect_out

    ## 山登り法で移動を行う ## 
    Search_lim = 5000 # 実行時間制限を考慮した探索回数の条件
    v_row = [0, -1,  0, 1]
    v_col = [1,  0, -1, 0]

    # 初期状態で接続したときの得点
    Score_Prev, Y, Connect_out = Connection()

    # 温度関数、遷移確率関数
    Temp_start = 100
    Temp_end = 1
    def Temperture(diff, all_diff):
        return Temp_start + (Temp_end - Temp_start)*diff/all_diff
    def Probability_trans(temp, score_new, score_prev):
        return 2.718*((score_new - score_prev) / temp)

    # 探索回数の上限まで焼きなまし ただし、X+Yが上限に達したら即終了
    Search_cnt = 0
    while Search_cnt < Search_lim:
        Search_cnt += 1

        # 移動させるコンピュータを 0~100K-1 から乱択
        Selected_CP_id = random.randrange(0, Computers_num)
        # コンピュータの座標を取得
        row_self, col_self = Computers_position[Selected_CP_id]
        # 移動させる方向を 0~3 から乱択
        Direction = random.randrange(0, 4)
        Move_OK = False
        for Try_cnt in range(4):
            Direction = (Direction+Try_cnt)%4
            Dest_row = row_self + v_row[Direction]
            Dest_col = col_self + v_col[Direction]
            # 移動先が Room外 or 既にコンピュータあり の場合は別の方向へ
            if Dest_row in {-1, N} or Dest_col in {-1, N}: continue
            if Room[Dest_row][Dest_col] > 0: continue
            Move_OK = True
            break
        if not Move_OK: continue

        # コンピュータの移動 -> Room座標情報のSwap, 座標情報の更新
        Room[row_self][col_self], Room[Dest_row][Dest_col] = Room[Dest_row][Dest_col], Room[row_self][col_self]
        Computers_position[Selected_CP_id] = [Dest_row, Dest_col]

        # ケーブルの接続とRoom情報の更新と得点計算
        Score_Now, Y_Now, Connect_out_Now = Connection()

        # 温度の計算
        Temp_now = Temperture(Search_cnt, Search_lim)
        # 遷移確率の計算
        Prob_now = Probability_trans(Temp_now, Score_Now, Score_Prev)

        # 遷移確率をもとにコミット/ロールバックを判定
        # X+Yが100Kを超えてしまうような移動は許可しない
        # print(Score_Now, Temp_now, round(Prob_now, 8))
        if Prob_now > random.random() and (X+1)+Y_Now <= Computers_num:
            Move_out.append([row_self, col_self, Dest_row, Dest_col])
            X += 1
            Y = Y_Now
            Connect_out = copy.deepcopy(Connect_out_Now)
            Score_Prev = Score_Now
        else:
            Room[row_self][col_self], Room[Dest_row][Dest_col] = Room[Dest_row][Dest_col], Room[row_self][col_self]
            Computers_position[Selected_CP_id] = [row_self, col_self]


        # 移動+接続の回数上限に達したら山登り終了
        if X+Y >= Computers_num: break

    ## 出力 ##
    print(Score_Prev, Search_cnt)

    # ### 提出時はここだけを有効化する ###
    # print(X)
    # for ans in Move_out: print(*ans)
    # print(min(Y, Computers_num-X))
    # for ans in Connect_out[:Computers_num-X]: print(*ans)


    # # local test
    # print(Score_Prev)
    # test
    # sys.stdout = open('./test004-out.txt', 'w')
    # print(X)
    # for ans in Move_out: print(*ans)
    # print(Y)
    # for ans in Connect_out: print(*ans)
    # sys.stdout = sys.__stdout__


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

if __name__ == '__main__':

    main()