def main():
    import sys
    import collections
    n = int(input())
    G = collections.defaultdict(list)

    # N頂点N辺連結グラフ(通称:なもりグラフ)は、1つの閉路と、閉路上の頂点を根とする木(足と呼ぶ)から成る

    # 各頂点が「足に含まれる」「足に含まれない」のいずれかがわかれば、
    # クエリで与えられる2頂点x,yが片方でも足に含まれないとき、x->y単純パスは閉路を左回り/右回りする2通りあり、
    # 両方とも足に含まれるとき、x->y単純パスは(木上の単純パスなので)ただ1つに決まる

    # よって、クエリを処理する前に、その情報を調べておく
    # 次数1の頂点と、それに隣接する辺を(トポロジカルソートでやるように)削除していくと、いずれは閉路のみが残る
    # このとき、削除した辺に隣接する、削除していない側の頂点を次に探索するように、
    # すなわちDFSすることで、閉路上の頂点に到達するまで、同じ木上を探索できる

    # これを利用して、同じ木は同じグループに属するとしてUnion-Find木でつなげておくことで、
    # 「両方とも足に含まれるとき」の判定をUnion-Findで高速に行うことができる


    # 頂点ごとの次数管理
    ecnt = [0]*n
    # 各頂点がどの木に属するか
    ashi = UnionFind(n)

    # Union-Findを使う都合、すべて0-indexedで扱う
    for _ in range(n):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
        ecnt[u] += 1
        ecnt[v] += 1

    # 初期状態で次数1の頂点をdequeに入れる
    nx = collections.deque()
    for i in range(n):
        if ecnt[i]==1:
            nx.append(i)

    # DFSで次数1の頂点をどんどん削除する
    while nx:
        v_from = nx.pop()

        for v_to in G[v_from]:
            ecnt[v_to] -= 1
            # 同じ木を探索している間、Unionしていく
            ashi.union(v_from, v_to)
            # 木の根(閉路の頂点)に到達した時点が最深部となり、次の始点へ
            if ecnt[v_to]==1:   
                nx.append(v_to)

    q = int(input())
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        if ashi.same(x, y):
            print('Yes')
        else:
            print('No')


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
    from sys import stdin
    from math import sqrt, ceil, floor, factorial
    from collections import defaultdict, deque, Counter
    from heapq import heapify, heappop, heappush
    from itertools import accumulate, permutations, combinations, product
    import copy

    # int(input())
    # map(int, stdin.readline().split())
    # list(map(int, stdin.readline().split()))

    main()