import sys
import collections
sys.setrecursionlimit(10**7) # 7*(10**5)ならPyPyでもAC
n, m = map(int, input().split())

# 頂点x, yがx->y, y->xどちらも到達できるというのは、要は閉路である
# つまり与えられたグラフの閉路を全て見つけ、その頂点数mがわかれば
# mC2で閉路ごとの条件を満たす頂点対を数え上げることができる

# 有向グラフで閉路を見つけるには、強連結成分分解をする
# そもそも、強連結の定義が、この問題の条件を満たす頂点の集合であり、
# 強連結であるためにはそれ以上他の頂点を追加できないような頂点集合を強連結成分という

# アルゴリズムとしては、適当な頂点からDFSを行い、帰りがけ順序を記録する
# その後全ての辺の向きを逆にして、帰りがけ順序が大きかった順にDFSをする
# 元のグラフでトポロジカル順序が前の頂点ほど帰りがけ順序が大きくなり、
# 辺を逆にすると、そのような頂点は移動ができなくなる一方、
# 閉路になっている部分は、辺の向きがどちらでも互いに行き来できるため、
# 帰りがけ順序大きい順に辺を逆にしたグラフでDFSを一回行うごとに、
# そのDFSで通った頂点集合が1つの強連結成分となる


Greg = collections.defaultdict(list)
Grev = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    Greg[a].append(b)
    Grev[b].append(a) # 辺を逆向きにしたグラフも先に作っておく

ans = 0
seen_Greg, seen_Grev = [False]*(n+1), [False]*(n+1)
# 帰りがけ順に入れるスタックとして使う(FILOになる)
back_order = collections.deque()

# 元のグラフのDFS
def dfs_reg(v_from):
    seen_Greg[v_from] = True
    
    for v_to in Greg[v_from]:
        if not seen_Greg[v_to]:
            dfs_reg(v_to)
    # 帰りがけ順に頂点番号をスタックする
    back_order.append(v_from)

for i in range(1, n+1):
    if not seen_Greg[i]:
        dfs_reg(i)

print(back_order)

# 辺を逆向きにしたDFS
def dfs_rev(v_from, cnt):
    seen_Grev[v_from] = True
    cnt += 1
    
    for v_to in Grev[v_from]:
        if not seen_Grev[v_to]:
            cnt = dfs_rev(v_to, cnt)

    return cnt

while back_order:
    v = back_order.pop()
    cnt = 0
    if not seen_Grev[v]:
        cnt = dfs_rev(v, cnt)
        # 強連結成分ごとの頂点数mとしてmC2が答え(m=1は0)
        ans += cnt*(cnt-1)//2

print(ans)