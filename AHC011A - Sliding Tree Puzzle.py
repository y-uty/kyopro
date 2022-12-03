import time
time_s = time.perf_counter()
import collections

# 入力を10進数整数に変換
# 空きマスの場所を調べておく
n, t = map(int, input().split())
tiles = []
blank = []
for i in range(n):
    t_row = list(str(input()))
    for j in range(n):
        t_row[j] = int(t_row[j], 16)
        if t_row[j]==0:
            blank = [j, i] # j:x座標, i:y座標
    tiles.append(t_row)

# 縦横方向の移動ベクトル [下, 右, 上, 左]
move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]
move_out = ['D', 'R', 'U', 'L']

# 現在の空きマス座標と移動方向を与えてスライドさせる処理
def slide(pos_blank, direction):
    # 移動先の座標を計算
    x = pos_blank[0] + direction[0]
    y = pos_blank[1] + direction[1]
    # 移動できない方向の場合、Falseを返す
    if x<0 or x>=n or y<0 or y>=n: return False

    # タイルのスライド(リストの要素の入れ替え)
    # j:x座標, i:y座標 に注意
    tiles[y][x], tiles[pos_blank[1]][pos_blank[0]] = tiles[pos_blank[1]][pos_blank[0]], tiles[y][x]
    return [x, y]


# パズルの盤面から木を作成してその大きさを計算する
# 始点を固定した処理(外部から全始点に対して試すループを回す)
# st: [x, y]
def make_tree(st):
    # 空きマス0は&で絶対0なので気にしない
    if st==blank: return 0
    # seen==Trueに辿り着いた場合は閉路あり=木ではないので点数を0とする
    seen = [False]*(n**2)
    size_tree = 0

    nx = collections.deque()
    nx.append(st)

    while nx:
        tile_from = nx.popleft()
        size_tree += 1
        from_x = tile_from[0]
        from_y = tile_from[1]
        num_from = tiles[from_y][from_x]
        seen[from_y*n+from_x] = True
        # 4方向へつながっているか？
        for adj in range(4):
            # 移動先の座標
            adj_x = from_x + move_x[adj]
            adj_y = from_y + move_y[adj]
            # 移動できない方向の場合スキップ
            if adj_x<0 or adj_x>=n or adj_y<0 or adj_y>=n: continue
            # 移動先のタイルの数字を取得
            num_adj = tiles[adj_y][adj_x]

            # 方向に対応した2^kのビットマスクで繋がっているかを判定
            con_ok = False
            if adj==0: #下
                if (num_from & 8 == 8) and (num_adj & 2 == 2):
                    con_ok = True
            elif adj==1: #右
                if (num_from & 4 == 4) and (num_adj & 1 == 1):
                    con_ok = True
            elif adj==2: #上
                if (num_from & 2 == 2) and (num_adj & 8 == 8):
                    con_ok = True
            else: #左
                if (num_from & 1 == 1) and (num_adj & 4 == 4):
                    con_ok = True
            # print(num_from, num_adj)
            if con_ok:
                # 移動先が未到達であれば次の地点候補に追加する
                if seen[adj_y*n+adj_x]==False:
                    nx.append([adj_x, adj_y])
                # else: return 0 # そうでないとき木ではない
                # 閉路の検出をどうする？                 

    return size_tree

# 点数計算
def calc_score(s):
    return round(500000*(s/(n**2-1)))

# 初期の盤面の点数計算
ans = ''
ans_max = ''
score_max = 0
score_this_time = 0
size_this_time = 0
for i in range(n**2):
    size_now = make_tree([i%n, i//n])
    # print(size_now, [i%n, i//n])
    if size_now > size_this_time:
        size_this_time = size_now
        score_this_time = calc_score(size_this_time)

if score_this_time > score_max:
    score_max = score_this_time

# 4方向どこに移動するかをt回ランダムに繰り返す
# 同じところを行き来しても改善しないので、そのような移動は禁止する
# 必ず2方向は移動可能、禁止されるのは1方向のみなので、移動できなくなることはない
prev_ran = -1
score_best = 0
for i in range(t):
    res = False
    ran = int(str(time.perf_counter())[-2:])%4
    while res==False:
        # 直前の場所に戻らない
        if (ran+2)%4 == prev_ran:
            ran = (ran+1)%4
        res = slide(blank, [move_x[ran], move_y[ran]])
        # 移動できない方向へ行かない
        if res==False:
            ran = (ran+1)%4
        else:
            blank = res
            ans += move_out[ran]
            prev_ran = ran

    # 現在の盤面のスコアを計算
    for i in range(n**2):
        size_now = make_tree([i%n, i//n])
        if size_now > size_this_time:
            size_this_time = size_now
            score_this_time = calc_score(size_this_time)

    # 最高スコアを更新した場合、その出力を記録しておく
    if score_this_time > score_max:
        score_max = score_this_time
        ans_max = ans

print(ans_max)
# print(ans)
