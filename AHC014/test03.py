import collections
import sys
from math import ceil
from random import randint, seed
from copy import deepcopy
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

sys.stdin = open('./in001.txt', 'r')
N, M = map(int, sys.stdin.readline().split())

# 全ての格子点の重みの総和
c = (N-1)//2
all_weight = 0
for x in range(N):
    for y in range(N):
        all_weight += (x-c)**2 + (y-c)**2 + 1

# 印を打った格子点(既存点)一覧
lattice_list_init = [(-1, -1)] # p2の取得に使う. 1-indexed
lattice_check_init = defaultdict(int) # ある座標となる既存点の存在判定に使う
for i in range(1, M+1):
    x, y = map(int, sys.stdin.readline().split())
    lattice_list_init.append((x, y))
    lattice_check_init[(x, y)] = i # 格子点番号を付与. 1-indexed


# 8方向移動ベクトル: 上を0として、時計回りに左上へ7までの番号を割り当てる
vx = [0, 1, 1, 1, 0, -1, -1, -1]
vy = [1, 1, 0, -1, -1, -1, 0, 1]

def all_proc():
    # 格子点情報の初期化
    lattice_list = deepcopy(lattice_list_init)
    lattice_check = deepcopy(lattice_check_init)

    # 既存点から8方向へ辺を張ったかどうかを管理するリスト
    # 辺を張ったとき2^(方向:0~7)を加算する
    lattice_edges = [0]*(M+1)

    # p2により近いp1を選ぶためのheapq
    p1nearest = []
    heapify(p1nearest)

    # 次にp2とする点を取り出すqueue
    cands_p2 = collections.deque()

    # 印を打った全ての格子点から盤面のスコアを計算する
    def calc_score():
        sum_weight = 0
        for i in range(1, len(lattice_list)):
            lx, ly = lattice_list[i]
            sum_weight += (lx-c)**2 + (ly-c)**2 + 1
        
        return round(10**6 * (N**2 / M) * (sum_weight/all_weight))


    # 既存点からp2としてランダムに1つ取得する
    def rand_choice_p2(): 
        idx = randint(1, len(lattice_list)) - 1 # 1-indexed
        return lattice_list[idx]

    # p1~p4がつくる長方形の面積を、ベクトルの外積として求める
    def calc_rect_area(p2x, p2y, p3x, p3y, p4x, p4y):
        v1x, v2x = p2x-p3x, p4x-p3x
        v1y, v2y = p2y-p3y, p4y-p3y
        return abs(v1x*v2y - v1y*v2x)

    # p2, p4 -> p1へ辺を結べるかの検証
    def verify_p1(p1x, p1y, p2x, p2y, p4x, p4y, dir0, dir1):
        # 方眼紙からはみ出る場合は即NG
        if p1x < 0 or p1x >= N or p1y < 0 or p1y >= N:
            return False
        # 既存点と重複する場合は即NG
        if lattice_check[(p1x, p1y)]:
            return False

        # p1 -> p2 はd1の逆方向、p1 -> p4 はd0と同方向
        dir0rev = (dir0+4)%8
        dir1rev = (dir1+4)%8

        # p4 -> p1の方向に既に辺が張られている場合、このp4, p1は選べないのでNG
        if lattice_edges[lattice_check[(p4x, p4y)]] & 1<<dir0rev:
            return False  
        # p2 -> p1の方向についても同様
        if lattice_edges[lattice_check[(p2x, p2y)]] & 1<<dir1:
            return False
        # p1 -> p2, p4, p4の逆方向も同様
        if lattice_edges[lattice_check[(p1x, p1y)]] & 1<<dir1rev:
            return False
        if lattice_edges[lattice_check[(p1x, p1y)]] & 1<<dir0:
            return False
        if lattice_edges[lattice_check[(p1x, p1y)]] & 1<<dir0rev:
            return False


        # まずは p1 -> p2
        dx, dy = vx[dir1rev], vy[dir1rev]
        nowx, nowy = p1x+dx, p1y+dy
        while True:
            if nowx==p2x and nowy==p2y: break

            # 既存点の存在チェック. p1に向かっているので「存在してはならない」
            if lattice_check[(nowx, nowy)]:
                return False
            else: # 存在しない場合、一歩先へ
                nowx, nowy = nowx+dx, nowy+dy
        # 既存点が見つからないままp2に到達できたら、次にp4への到達判定へ

        # 次に p1 -> p4
        dx, dy = vx[dir0], vy[dir0]
        nowx, nowy = p1x+dx, p1y+dy
        while True:
            if nowx==p4x and nowy==p4y: break

            # p4に到達するまでに既存点が「存在してはならない」
            if lattice_check[(nowx, nowy)]:
                return False
            else: # 存在しない場合、一歩先へ
                nowx, nowy = nowx+dx, nowy+dy
        # 既存点に衝突せずに p1 -> p2, p4 両方に到達できた場合、p1を採用OK

        return True

    # p3 -> p4を探す
    def srch_p3_to_p4(p2x, p2y, p3x, p3y, dir0):
        p_cw_ccw = [] # 出力用

        # p2->p3の方向から、CW/CCWに90度回転した方向への探索
        dir1cw, dir1ccw = (dir0+2)%8, (dir0-2)%8

        for dir1 in (dir1cw, dir1ccw):

            # その方向にp3から既に辺を張っている場合、スキップ
            if lattice_edges[lattice_check[(p3x, p3y)]] & 1<<dir1:
                return p_cw_ccw

            dx, dy = vx[dir1], vy[dir1]
            nowx, nowy = p3x+dx, p3y+dy

            while nowx >= 0 and nowx < N and nowy >= 0 and nowy < N: # 方眼紙全体から出ない
                # 既存点の存在チェック
                if lattice_check[(nowx, nowy)]:
                    # 存在する場合p4となる. ここで、p1の座標が一意に定まる
                    p4x, p4y = nowx, nowy
                    p1x, p1y = p2x+p4x-p3x, p2y+p4y-p3y
                    
                    # p1を選んで長方形が作れるかの最終チェックへ
                    res = verify_p1(p1x, p1y, p2x, p2y, p4x, p4y, dir0, dir1)

                    # p1を採用OKの場合、p1~p4を出力に追加
                    if res:
                        # 作られる長方形の面積を計算して出力に含める
                        S_rect = calc_rect_area(p2x, p2y, p3x, p3y, p4x, p4y)
                        p_cw_ccw.append((S_rect, p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1)) 
                    break
                    
                else: # 存在しない場合、一歩先へ
                    nowx, nowy = nowx+dx, nowy+dy

        # 0~2個のp1~p4を返す
        return p_cw_ccw

    # 採用したp1が既存辺の上だった場合、p1もその辺方向に辺を張ったことにする
    def edge_apply_from_p1(p1x, p1y):
        for dir in range(8): # dir0: p3となる直近点の探索方向
            dx, dy = vx[dir], vy[dir]
            nowx, nowy = p1x+dx, p1y+dy

            while nowx >= 0 and nowx < N and nowy >= 0 and nowy < N: # 方眼紙全体から出ない
                # 既存点の存在チェック
                if lattice_check[(nowx, nowy)]:
                    # 既存辺上である場合、その辺方向(2方向)にp1も辺を張っている
                    if lattice_edges[lattice_check[(nowx, nowy)]] & 1<<(dir+4)%8:
                        lattice_edges[lattice_check[(p1x, p1y)]] |= 1 << dir
                        lattice_edges[lattice_check[(p1x, p1y)]] |= 1 << (dir+4)%8
                    # この方向で直近の既存点が、対向する辺を張っていない場合、問題なし
                    else:
                        pass
                    # いずれにせよ、直近の既存点を見つけたら、その方向の探索は終了
                    break

                else: # 存在しない場合、一歩先へ
                    nowx, nowy = nowx+dx, nowy+dy

    # 1. 新規点を格子点リストに追加する
    # 2. 辺を張った方向を記録する
    def add_p1_and_record_edges(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1):

        next_number = len(lattice_list)
        lattice_list.append((p1x, p1y))
        lattice_edges.append(0)
        lattice_check[(p1x, p1y)] = next_number


        lattice_edges[lattice_check[(p1x, p1y)]] |= 1 << dir0
        lattice_edges[lattice_check[(p1x, p1y)]] |= 1 << (dir1+4)%8

        lattice_edges[lattice_check[(p2x, p2y)]] |= 1 << dir0
        lattice_edges[lattice_check[(p2x, p2y)]] |= 1 << dir1

        lattice_edges[lattice_check[(p3x, p3y)]] |= 1 << (dir0+4)%8
        lattice_edges[lattice_check[(p3x, p3y)]] |= 1 << dir1

        lattice_edges[lattice_check[(p4x, p4y)]] |= 1 << (dir0+4)%8
        lattice_edges[lattice_check[(p4x, p4y)]] |= 1 << (dir1+4)%8

        edge_apply_from_p1(p1x, p1y)


    # p2 -> p3を探す
    def srch_p2_to_p3(p2x, p2y, Slim):

        # 8方向への探索
        for dir0 in range(8): # dir0: p3となる直近点の探索方向
            # その方向とにp2から既に辺を張っている場合、スキップ
            if lattice_edges[lattice_check[(p2x, p2y)]] & 1<<dir0:
                continue

            dx, dy = vx[dir0], vy[dir0]
            nowx, nowy = p2x+dx, p2y+dy

            while nowx >= 0 and nowx < N and nowy >= 0 and nowy < N: # 方眼紙全体から出ない
                # 既存点の存在チェック
                if lattice_check[(nowx, nowy)]:
                    # 存在する場合p3となる. さらにp3を起点にp4を探索する
                    res = srch_p3_to_p4(p2x, p2y, nowx, nowy, dir0)
                    res0, res1 = False, False
                    if len(res) > 1:
                        res0, res1 = res
                        heappush(p1nearest, res0)
                        heappush(p1nearest, res1)
                    elif len(res)==1:
                        res0 = res[0]
                        heappush(p1nearest, res0)

                    # p2 から dir0 方向への探索を終了       
                    break

                else: # 存在しない場合、一歩先へ
                    nowx, nowy = nowx+dx, nowy+dy
        
        # できる長方形の面積が最も小さくなるようなp1を選ぶ
        if len(p1nearest):
            S, p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1 = heappop(p1nearest)
            if S > Slim:
                ret_blank = tuple()
                return ret_blank
            
            add_p1_and_record_edges(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1)

            ret_p1234 = (p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y)
            return ret_p1234 # 出力
        
        else: # p2からp1をひとつも選べない場合、空のタプルを返す
            ret_blank = tuple()
            return ret_blank


    # p2をランダムに選んでp1~p4の組を生成し、出力リストに追加していく
    anslist = []
    Slim_stt = 4
    Slim_end = N**2
    loop_count = 5000
    for i in range(loop_count):

        if cands_p2:
            p2num = cands_p2.popleft()
            p2x, p2y = lattice_list[p2num]
        else:
            p2x, p2y = rand_choice_p2()

        p1nearest = []

        Slim = ceil(Slim_stt + (Slim_end-Slim_stt)*i/loop_count)
        # Slim = 100000
        ans = srch_p2_to_p3(p2x, p2y, Slim)

        # ansが空でない(p1を選んで長方形を作れた)場合、出力に追加する
        # その長方形を作った4点を次回優先的に選ぶようにする

        # ansが空の場合、何もしない
        if ans:
            anslist.append(ans)

            p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y = ans
            cands_p2.appendleft(lattice_check[(p2x, p2y)])
            cands_p2.appendleft(lattice_check[(p3x, p3y)])
            cands_p2.appendleft(lattice_check[(p4x, p4y)])
            cands_p2.appendleft(lattice_check[(p1x, p1y)])
        
        else:
            # continue
            cands_p2.append(lattice_check[(p2x, p2y)])

        # print(i, ans)

    score = calc_score()

    return score, anslist

# 処理全体の実行 #
best_score = 0
best_ans = []

for i in range(1, 101):
    # seed(i)
    now_score, now_ans = all_proc()

    if now_score > best_score:
        best_score = now_score
        best_ans = deepcopy(now_ans)


print(len(best_ans))
for bans in best_ans:
    print(*bans)

sys.stdout = open('./out001.txt', 'w')
print(len(best_ans))
for bans in best_ans:
    print(*bans)
sys.stdout = sys.__stdout__
