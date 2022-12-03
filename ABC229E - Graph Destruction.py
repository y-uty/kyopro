# https://note.nkmk.me/python-union-find/

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

    # Unionでグループ数(=連結成分)が減少したかを確認するために、0 or 1をreturnするように改修
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


import sys
import collections
n, m = map(int, input().split())

G = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

ans = 0 # 現時点の連結成分数
anslist = [0] # 出力用
uf = UnionFind(n) # Union-Find森の初期化
for i in range(n, 1, -1):
    conn = G[i] # 現れる頂点と繋がる頂点を隣接リストから取得
    ans += 1 # 頂点が増えるので、一旦連結成分は1増える

    # 繋がる頂点とUnionした場合グループがまとまった(連結成分が減った)ので-1
    for c in conn:
        # 接続先が既に現れていないとUnionできないことに注意
        # (相手側が登場したときに改めてUnionすることとなる)
        if c >= i:
            ans -= uf.union(i-1, c-1) # Union-Findでは0-indexedに注意

    anslist.append(ans)

# 問題の逆順で見たので反転させて改行区切りで出力
print(*anslist[::-1], sep='\n')