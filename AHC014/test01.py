import sys
from random import randint, seed
seed(0)
from collections import defaultdict

sys.stdin = open('./in001.txt', 'r')
N, M = map(int, sys.stdin.readline().split())

# 印を打った格子点(既存点)一覧
lattice_list = [(-1, -1)] # p2の取得に使う. 1-indexed
lattice_check = defaultdict(int) # ある座標となる既存点の存在判定に使う
for i in range(1, M+1):
    x, y = map(int, sys.stdin.readline().split())
    lattice_list.append((x, y))
    lattice_check[(x, y)] = i # 格子点番号を付与. 1-indexed

# 8方向移動ベクトル: 上を0として、時計回りに左上へ7までの番号を割り当てる
vx = [0, 1, 1, 1, 0, -1, -1, -1]
vy = [1, 1, 0, -1, -1, -1, 0, 1]

# 既存点から8方向へ辺を張ったかどうかを管理するリスト
# 辺を張ったとき2^(方向:0~7)を加算する
lattice_edges = [0]*(M+1)

# 既存点からp2としてランダムに1つ取得する
def rand_choice_p2(): 
    idx = randint(1, len(lattice_list)) - 1 # 1-indexed
    return lattice_list[idx]

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
        # print(nowx, nowy)
        if nowx==p2x and nowy==p2y: break

        # 既存点の存在チェック
        # ここでは、p1に向かっているので「存在してはならない」
        if lattice_check[(nowx, nowy)]:
            return False
        else: # 存在しない場合、一歩先へ
            nowx, nowy = nowx+dx, nowy+dy
    # 既存点が見つからないままp2に到達できたら、次にp4への到達判定へ

    # 次に p1 -> p4
    dx, dy = vx[dir0], vy[dir0]
    nowx, nowy = p1x+dx, p1y+dy
    while True:
        # print(nowx, nowy)
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
    # どちらかをランダムで選ぶ
    dir1 = set([dir1cw, dir1ccw]).pop()

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
            p2xO, p2yO = p2x-p3x, p2y-p3y
            p4xO, p4yO = p4x-p3x, p4y-p3y
            p1x, p1y = p2xO+p4xO+p3x, p2yO+p4yO+p3y
            
            # p1を選んで長方形が作れるかの最終チェックへ
            res = verify_p1(p1x, p1y, p2x, p2y, p4x, p4y, dir0, dir1)

            # p1を採用OKの場合、p1~p4を出力に追加
            if res:
                p_cw_ccw.append((p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1)) 
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


# p2 -> p3を探す
def srch_p2_to_p3(p2x, p2y):
    plist = [] # 出力用
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
                elif len(res)==1:
                    res0 = res[0]
                
                # 1. 新規点を格子点リストに追加する
                # 2. 辺を張った方向を記録する
                if res0 != False:
                    p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1 = res0

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

                    plist.append((p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y))

                if res1 != False:
                    p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, dir0, dir1 = res1

                    next_number = len(lattice_list)
                    lattice_list.append((p1x, p1y))
                    lattice_edges.append(0)
                    lattice_check[(p1x, p1y)] = next_number


                    lattice_edges[lattice_check[(p1x, p1y)]] |= 1 << dir0
                    lattice_edges[lattice_check[(p1x, p1y)]] |= 1 << (dir1+4)%8

                    lattice_edges[lattice_check[(p2x, p2y)]] |= 1 << dir0
                    lattice_edges[lattice_check[(p2x, p2y)]] |= 1 << (dir1+4)%8

                    lattice_edges[lattice_check[(p3x, p3y)]] |= 1 << (dir0+4)%8
                    lattice_edges[lattice_check[(p3x, p3y)]] |= 1 << dir1

                    lattice_edges[lattice_check[(p4x, p4y)]] |= 1 << (dir0+4)%8
                    lattice_edges[lattice_check[(p4x, p4y)]] |= 1 << (dir1+4)%8

                    edge_apply_from_p1(p1x, p1y)

                    plist.append((p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y))

                # p2 から dir0 方向への探索を終了       
                break

            else: # 存在しない場合、一歩先へ
                nowx, nowy = nowx+dx, nowy+dy
        
    return plist # 出力


anslist = []
for _ in range(100000):
    p2x, p2y = rand_choice_p2()
    tmplist = srch_p2_to_p3(p2x, p2y)
    for tmp in tmplist:
       anslist.append(tmp) 

sys.stdout = open('./out001.txt', 'w')
print(len(anslist))
for ans in anslist:
    print(*ans)
sys.stdout = sys.__stdout__
