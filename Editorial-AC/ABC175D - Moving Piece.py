import collections
n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

# 全体でいくつかのサイクルになるので、それごとに考える

# 連結成分はUnion-Findで管理
class UnionFind():
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # path compression; search for root, and connect to each parent
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # Unionでグループ数が減少したかを確認するために、0 or 1をreturnするように改修
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # union by rank;
        #  connect less-depth group to higher-depth one not to increase max-depth
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return 1

uf = UnionFind(n)
for i in range(n):
    pi = p[i]-1 # 0-indexedに注意
    uf.union(i, pi)

# 連結成分ごとに、サイクルごとの和を調べる
sum_of_cycle = collections.defaultdict(int)
for i in range(n):
    pi = p[i]-1
    parent_pi = uf.find(pi)
    sum_of_cycle[parent_pi] += c[pi]

# 始点ごとに答えを調べる
INF = -10**18
ans = INF
for i in range(n):
 
    # 始点が属する連結成分の周期Tはuf.parents[root]に記録された頂点数
    parent_i = uf.find(i)
    T = -1*uf.parents[parent_i]

    # 「できるだけサイクルして、余りを全部調べてそのうち最大」...としたくなるがNG
    # たとえば、周期4, サイクル和13 のサイクル [2, -3, 20, -6] についてK=14とすると、
    # 3周してスコア39で、そこから2歩まで進めて、そのときのスコアは 41, 38 だが、
    # 3周の1歩, 2歩手前はそれぞれ 45, 25 であり、45が最適となる

    # 一方、サイクル和が正であれば、(歩数%周期)でのスコアは
    # 1サイクルで必ず増加するので、周期ぶんだけ調べればそこに最大値が存在する

    # サイクル和は、開始/終了の場所をシフトさせても変わらないので、
    # 固定した始点から余りの部分として何歩進むか？について全探索する
    # 余りの歩数をMとすると、K回のうちサイクルのために残された部分はK-Mとなり、
    # よって周期Tでサイクルできる回数は (K-M)//T である

    # なお、サイクル和が0以下の場合はサイクルしても得しないので、
    # 単に1サイクル未満の歩数をすべて調べれば最大値がわかる
    pos = i
    tmp = 0
    max_rem = INF
    for M in range(1, min(k, T)+1):
        # 移動先でスコアを獲得
        next_pi = p[pos]-1
        tmp += c[next_pi] 

        # 余りM回のときの周回数を求めて、最終的な獲得スコアに一気に加算
        repcnt = 0 if sum_of_cycle[parent_i] <= 0 else (k-M)//T
        if tmp+repcnt*sum_of_cycle[parent_i] > max_rem:
            #
            max_rem = tmp+repcnt*sum_of_cycle[parent_i]

        pos = next_pi #　次へ

    ans = max(ans, max_rem)

print(ans)     
