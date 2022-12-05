# N - integer
N = int(input())

# S - string
S = input()

# A B
a, b = map(int, input().split())

# N
# H1, H2, ... , Hn
N = int(input())
H = list(map(int, input().split()))

# reslut by \n
ans_list = [2, 3, 5, 7]
print(*ans_list, sep='\n')

# faster read multiple lines
from sys import stdin
for _ in range(N):
    x, y, z = map(int, stdin.readline().split())
## or ...
xyzs = [list(map(int, stdin.readline().split())) for _ in range(N)]

# alphabets
atoz = 'abcdefghijklmnopqrstuvwxyz'
AtoZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# mod4
expon_1tab = [[0,0,0,0],[1,1,1,1],[6,2,4,8],[1,3,9,7],[6,4,6,4],[5,5,5,5],[6,6,6,6],[1,7,9,3],[6,8,4,2],[1,9,1,9]]

# set
a_set = set()
a_set.add('x')

# default dict
from collections import defaultdict
a_dict = defaultdict(list)

# deque
from collections import deque
d = deque()

# Cartesian product
import itertools
a_list = [[], [], []]
p = itertools.product(*a_list) # unpack

# permutation
import itertools
p = itertools.permutations(list(range(N))) # return iterator
p = list(p) # tupples in list

# DP-table
## dp[i][j][k] 内側からk, j, iの範囲
dp_3D = [[[-1]*(101) for _ in range(101)] for _ in range(101)]

# bit全探索
cand = [] # 選ぶ候補のリスト
for bits in itertools.product([True, False], repeat=len(cand)):
    # 1つの選び方を生成
    choice = [x for x, b in zip(cand, bits) if b]

    # 以下、選び方に対する判定・処理・解答の構成などを行う
    # ...
    # ...



# 整数問題いろいろ
## ABC052C - Factors of Factorial ## 約数の数は各素因数の登場回数+1の掛け算
## ABC114D - 756 ## 約数の個数
## ABC170D - Not Divisible ## 割り切れるか？=>小さい数字から順に倍数を篩でチェック
## ABC172D - Sum of Divisors ## Nまでのすべての整数の約数個数をエラトステネスの篩でO(NlogN)
## ABC177E - Coprime ## 互いに素<=>共通の素因数を持たない
## ABC179E - Sequence Sum ## mod Mのもとで取りうる値は0~M-1のM種類; 鳩ノ巣原理
## ABC254D - Together Square ## 平方数をつくれるか 十分大きい平方数との商に着目
## ABC276D - Divide by 2 or 3 ## gcd*(2^p)*(3^q) 操作順序・相互影響は無視できる

# 文字列操作
## ABC202D - aab aba baa ## 辞書順は前から決める. 小さい文字を置くと仮定したパターン数とk番目を比較
## ABC141E - Who Says a Pun? ## ローリングハッシュ

## 工夫する全探索
## ABC099D - Good Grid ## コストの前計算で計算量を落とす
## ABC119C - Synthetic Kadomatsu ## 使う/使わないでなく使い方4通りの全探索 O(4^N)
## ABC175D - Moving Piece ## サイクル+余りだが、単調性がないので余りを決めてからサイクル数を計算

# bit全探索
## ABC147C - HonestOrUnkind2
## ABC173C - H and V
## ABC197C - ORXOR
## ABC269C - Submask ## itertools.productでの実装例

# 二分探索で解を見つける
## ABC098D - Xor Sum 2 ## 左端を固定して、右端を求める
## ABC146C - Buy an Integer
## ABC174E - Logs ## 連続値の二分探索
## ABC246D - 2-variable Function
## ABC257D - Jumping Takahashi 2 ## is_ok()の中でBFS
## ABC269E - Last Rook ## インタラクティブ
## ABC270E - Apple Baskets on Circle ## サイクルまとめて処理回数を二分探索、端数は個別
## ARC144B - Gift Tax

# DPテーブルの更新を考える
## Typical008 - AtCounter ## 耳DP 指定の部分文字列を作る選び方の数え上げ
## Typical037 - Don't Leave the Spice ## 区間Maxを貰うDP withセグ木
## Typical056 - Lucky Bag ## DP復元 or 答えを持ちながら遷移
## TessokuA21 - Block Game ## 区間DP 短くしていく
## TessokuA79 - River Crossing ## 区間の総和を求めるために累積和を別で計算
## TessokuB21 - Longest Subpalindrome ## 区間DP 長くしていく
## TessokuB23 - Traveling Salesman Problem ## シンプルなTSP
## ABC060D - Simple Knapsack ## 3次元dp; ナップザックの重さの範囲が大きいが、特殊な制約を利用して立式
## ABC082D - FT Robot ## 部分和DP x, yを独立に 配列の取り方に注意しないとTLE/MLE
## ABC104C - All Green ## 回数制限付きで繰り返し選ぶ+ボーナスあり 状態と遷移を工夫して計算量をおさめる
## ABC122D - We Like AGC ## x文字前を状態として持ち禁止文字のパターンを遷移させないように
## ABC135D - Digits Parade ## 桁DP
## ABC142E - Get Everything ## bitDP N個ON/OFF -> 状態が2^N個になる
## ABC145E - All-you-can-eat ## ある選び方の組み合わせでは、コスト最大を最後に取るのが最良->コスト順に検討する
## ABC153E - Crested Ibis vs Monster ## 個数制限なしナップサック. 状態を上限で丸める
## ABC175E - Picking Goods ## 特殊な制約を追加の状態で管理する
## ABC178D - Redistribution ## 配るdpと累積和でパターン数え上げ
## ABC180E - Traveling Salesman among Aerial Cities ## bitDP TSP
## ABC183E - Queen on Grid ## 来た方向どこからでも一歩でこれる→累積和をとっておく
## ABC188E - Peddler ## 売値-買値の最大化 -> (今の売値)-(そこまでの最安値)の最大値
## ABC197E - Traveler ## ある点からx1<x2<...<xkのk点を全て最短で通り終えると、x1,xkのどちらかにいる
## ABC212E - Safety Journey ## 制約に着目して、遷移を高速化する前処理を行う
## ABC219D - Strange Lunchbox ## 3次元dp[k][i][j]:=i番目まででx=i,y=jとなる最小個数. 状態上限丸め
## ABC244E - King Bombee ## 偶数回選ばれる -> %2が0or1を状態に加える
## ABC251E - Takahashi and Animals ## 条件のループ -> どこかを固定して戻ってきたら整合性確認
## ABC253E - Distance Sequence ## 累積和を取りながら
## ABC262D - I Hate Non-integer Number ## 余りを状態に追加して3次元. 除数固定で4重ループ
## ABC266D - Snuke Panic (1D) ## 貰うDP
## ABC267D - Index × A(Not Continuous ver.) ## ナップサック
## ABC271D - Flip and Adjust ## 部分和問題と復元
## ABC274D - Robot Arms 2 ## 部分和DP x, yを独立に考える
## ABC274E - Booster ## bitDP TSP

# 確率dp・期待値dp
## EDPC I - Coins ## 状態を増やして、遷移でシンプルに確率の積の和をとっていく
## EDPC J - Sushi ## 期待値dp 自己ループを、dp遷移式の整理で消去する
## ABC275E - Sugoroku 4 ## 確率mod998244353 -> 確率1/Mをかける = Mの逆元をかける
## ABC280E - Critical Hit ## 遷移元の期待値を確率で重みつけ平均とって、+1すれば繊維先の期待値

# 桁dp
## ABC189D - Logical Expression

# 配列のswap
## ABC250C - Adjacent Swaps

# 累積和/いもす法
## ABC105D - Candy Distribution ## 累積和の剰余
## ABC106D - AtCoder Express 2 ## 区間を2次元座標にプロットして累積和
## ABC153F - Silver Fox vs Monster ## 区間の両端が単調増加->左端を順に参照しながらimosできる
## ABC183D - Water Heater
## ABC256D - Union of Interval
## ABC278E - Grid Filling ## 2次元累積和

# 単純な座標圧縮（座標をsetで重複排除 > listでsort > bisect_right(1-indexedに)）
## ABC213C - Reorder Cards

# 座標圧縮と累積和
## ABC188D - Snuke Prime
## ABC221D - Online games

# 尺取法
## ABC229D - Longest X

# 区間スケジューリング問題(終了最早を選び続ける)
## ABC230D - Destroyer Takahashi
## ABC103D - Islands War

# 多項式除算
## ABC245D - Polynomial division

# 最短経路の数え上げ（BFS）
## ABC211D - Number of Shortest paths

# いろいろなBFS・DFS
## Past009K - Gas Station ## s->a->tの最短距離は、aからの最短距離dist[s]+dist[t]
## Typical021 - Come Back in One Piece（★5）## 閉路のカウント; 強連結成分分解
## ABC126D - Even Relation ## DFSしながら距離の偶奇を判定
## ABC138D - Ki ## 木上でDFSでいもす法
## ABC168D - .. (Double Dots) ## 直前のノード番号を記録していく
## ABC176D - Wizard in Maze ## 01-BFS
## ABC184E - Third Avenue ## 一度使ったテレポータはもう使わない
## ABC187E - Through Path ## 部分木以外への加算 は 全加算 と 部分木の減算
## ABC220F - Distance Sums 2 ## 部分木の大きさを求める
## ABC239E - Subtree K-th Max ## DFSで葉から根へ情報を集めてテーブルに記録
## ABC237E - Skiing ## 同じ場所を複数回探索する. 更新するか、打ち切るかの判定
## ABC246E - Bishop 2 ## 01-BFS 頂点を3要素でもつ
## ABC254E - Small d and k ## DFSをQ回 - 到達頂点数が少ないなら管理を集合型で
## ABC266F - Well-defined Path Queries on a Namori ## なもりグラフ;足は閉路を根とする木

# グリッドBFS/DFS
## ABC088D - Grid Repainting
## ABC096C - Grid Repainting 2
## ABC151D - Maze Master ## 全始点について繰り返しBFS
## ABC272D - Root M Leaper ## 移動できる方向を列挙してからBFS
## ABC276E - Round Trip ## 始点を含む閉路を見つけるDFS

# トポロジカルソート・閉路検出 https://algo-logic.info/topological-sort/
## ABC223D - Restricted Permutation

# 重み付き最短経路
## ABC070D - Transit Tree Path
## ABC079D - Wall
## ABC208D - Shortest Path Queries 2
## ABC243E - Edge Deletion ## Warshall-Floyd法 より小さいコストで辺を迂回
## ABC277E - Crystal Switches ## 辺有無が反転する2世界をコスト0辺で行き来(01-BFSの方が速い)

# 最小全域木
## ABC051D - Candidates of No Shortest Paths ## 最短経路木
## ABC218E - Destruction ## Kruskal法
## ABC235E - MST + 1 ## クエリ先読み; 新たな辺がMSTになれる瞬間に既にオリジナル辺が2頂点を結んでいるかで判定
## ABC252E - Road Reduction ## Dijkstraで最短経路木
## ABC256E - Takahashi's Anguish ## 最"大"全域木を考えた / Functional Graphでは連結成分ごとの閉路は1個以下

# Union-Find
## ABC120D - Decayed Bridges ## 辺を順番に削除=>逆順にみて辺を追加
## ABC157D - Friend Suggestions
## ABC183F - Confluence ## UFの連結成分内のクラス分けはdictで / マージテク
## ABC206D - KAIBUNsyo
## ABC214D - Sum of Maximum Weights ## 重み小さい順に森を連結して木にしていく
## ABC226E - Just One ## 連結成分内の閉路の数をカウントする
## ABC229E - Graph Destruction ## ABC120Dの類題
## ABC231D - Neighbors
## ABC259D - Circumferences
## ABC264E - Blackout 2 ## 辺削除を逆順辺追加Pt.3 どの頂点につながっていてもいいなら1つにまとめてよい
## ABC269D - Do use hexagon grid

# 最大フロー
## ABC091C - 2D Plane 2N Points ## 二部マッチング問題

# BIT
## TessokuA59 - RSQ (Range Sum Queries)
## TessokuB59 - Number of Inversions ## 転倒数
## ABC157E - Simple String Queries ## BITインスタンスをたくさん
## ABC185F - Range Xor Query
## ABC179D - Leaping Tak ## 1つ前までの区間和で現在地を更新
## ABC190F - Shift and Inversions ## 転倒数

# セグメント木
## TessokuA58 - RMQ (Range Maximum Queries) ## 一点更新・区間Max
## TessokuB58 - Jumping ## dp配列をセグメント木に持つ 一点更新・区間Min
## Typical037 - Don't Leave the Spice ## 一点更新・区間Max

# ダブリング
## ABC136D - Gathering Children
## ABC241E - Putting Candies

# ゲーム
## ABC201D - Game in Momotetsu World ## Minimax法
## ABC270D - Stones ## やはりゲーム終了時から逆順で考える

# 部分和問題
## ABC204D - Cooking # bit全探索
## ABC200D - Happy Birthday! 2 # DP

# 逆元でnCk
## TessokuA30 - Combination ## 必要なときはこのまま使える
## ABC156D - Bouquet
## ABC145D - Knight

# 平衡二分探索木
## TessokuA55 - Set
## ABC217D - Cutting Woods
## ABC228D - Linear Probing
## ABC241D - Sequence Query
## ABC260D - Draw Your Cards

# 平面走査
## ABC245E - Wrapping Chocolate ## std::multiset(多重集合)

# Trie木(prefix-tree)
## ABC273E - Notebook

# 最遠点対
## マンハッタン距離
## ABC178E - Dist Max

# 平面幾何
## ABC197D - Opposite # 座標回転
## ABC248E - K-colinear Line # 3点が同一直線上? > 1点始点の2ベクトルの外積で判定
## ABC266C - Convex Quadrilateral ## 外積の正負で多角形の凸判定

# アフィン変換
## ABC189E - Rotate and Flip

# その他テクニック
## 歯抜けクエリ 初めから1つ手前までと後ろから1つ後までの情報を組み合わせて使う
## ABC279E - Cheating Amidakuji


# 約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
## 互いに素 => 約数に持つ素数が異なる
## 公約数が互いに素 => GCDの素因数の素数の種類数
## ABC142D - Disjoint Set of Common Divisors

# 素因数分解 O(√N)
import collections
def prime_factorize(n):
  a = collections.defaultdict(int)
  while n % 2 == 0:
      a[2] += 1
      n //= 2
  f = 3
  while f * f <= n:
      if n % f == 0:
          a[f] += 1
          n //= f
      else:
          f += 2 # 2以外の偶数は素因数にならない
  if n != 1:
      a[n] += 1
  return a # n=1は空list

# 素数列挙:エラトステネスの篩
import math
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    prime_set = set(list(range(2, n+1)))

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
                prime_set.discard(j)

    return prime_set

# 繰り返し二乗法
n = 10**9
ans = 1
MOD = 10**9+7
tmp = 2
for i in range(31): # 29 < log 10^9 < 30

    # nの2進数表示で2^iの桁が1 <=> n and 2^i != 0
    if n & (2**i) != 0:
        ans = (ans * tmp) % MOD

    tmp = (tmp * tmp) % MOD

# ランレングス圧縮
def RunLengthEncode(s):
    import itertools
    sgrp = itertools.groupby(s)
    scomp = []
    for chrtype, chrsub in sgrp:
        scomp.append((chrtype, len(list(chrsub))))

    return scomp

# grid problem
## vector - 8-neibor from upper left
vx = [-1, 0, 1, -1, 1, -1, 0, 1]
vy = [1, 1, 1, 0, 0, -1, -1, -1]

## vector - 4-neibor clockwise from above
vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]


# deci > bin
d = 11
d_bin = format(d, 'b')
d_num = 8
d_bin_zeropad = format(d, '0'+str(d_num)+'b')

# bin > deci
b = 1011 # binary number (type: integer)
b_deci = 0xbb # return decimal number (type: integer)


# judge prime number or not?
# if the provided number is prime, return 1, otherwise 0.
import math
def prornot(x): # x: integer (includes negative)
    if x < 2: return 0
    if x == 2: return 1

    for i in range(1, math.ceil(pow(x, 1/2))):
        if x % (i+1) == 0:
            return 0
 
    return 1


# binary search
## Following function returns which index the given value will be placed.
def binary_search(search_list, target_value):
    ng = -1
    ok = len(search_list)
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if search_list[mid] >= target_value:
            ok = mid
        else:
            ng = mid
    return ok

## use standard library 'bisect'
import bisect
search_list = [1,4,5,13,14,19,19,19,22,24,32,35,49,54,56,57,68,78,78,109]
target_value = 19
idx_l = bisect.bisect_left(search_list, target_value) # Be placed the left end among the same values.
idx_r = bisect.bisect_right(search_list, target_value) # Be placed the right end among the same values.


# Graph (Undirected)
N = 15 # vertex
M = 14 # edge 
from collections import defaultdict
G = defaultdict(list) # G[v]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a) # Delete this line if you address Directed Graph (direction a -> b). 


### Depth or Breadth First Search ######
from collections import deque
todo = deque() # ToDo[]
seen = [False] * N
passed_order = [] # record vertex no. in the order of passing

# start searching at G[0]
s = 0
seen[s] = True
todo.append(0)

while len(todo) > 0:
    v = todo.pop()
    passed_order.append(v)
    for w in G[v]:
        if seen[w]:
            continue
        else:
            seen[w] = True
            todo.append(w) # DFS (FILO)
            # todo.appendleft(w) # BFS (FIFO)


### DFS by recursive function ###
N, M = list(map(int, input().split())) # N:vertex , M:edge

from collections import defaultdict
G = defaultdict(list)

for _ in range(M):
    a, b = list(map(int, input().split()))
    G[a].append(b)
    # G[b].append(a)

seen = [False] * N
fst_order = [0] * N
lst_order = [0] * N
global tclock
tclock = 0

# searching start with
v_arrived = 0

# DFS function (recursive)
def dfs(seen, v_arrived):
    global tclock
    seen[v_arrived] = True
    fst_order[v_arrived] = tclock
    tclock += 1

    for v_reachable in G[v_arrived]:
        if seen[v_reachable] == False: # if this vertex has not seen
            dfs(seen, v_reachable)

    lst_order[v_arrived] = tclock
    tclock += 1

# execute DFS
dfs(seen, v_arrived)

print(G)
print(seen, fst_order, lst_order,)

