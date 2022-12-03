def main():
    import sys
    n, m, e = map(int, input().split())
    cables = []
    uf = UnionFind(n+1) # 発電所は全て1つにまとめる
    for _ in range(e):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        u = min(u, n)
        v = min(v, n)
        cables.append([u, v])


    q = int(input())
    queries_list = []
    queries_set = set()
    for _ in range(q):
        x = int(sys.stdin.readline()) # cables[x]を削除するイベント
        x -= 1
        queries_list.append(x)
        queries_set.add(x)
    queries_list = queries_list[::-1]

    for i in range(e): # イベントで削除対象外の辺をつなぐ
        if i in queries_set:
            continue
        a, b = cables[i]
        uf.union(a, b)

    anslist = [-uf.parents[uf.find(n)]-1]

    # イベントを逆順に見ていく
    for i in range(q):
        x = queries_list[i]
        a, b = cables[x]

        uf.union(a, b)

        anslist.append(-uf.parents[uf.find(n)]-1)

    print(*anslist[:-1][::-1], sep='\n')


####################################################################################################
####################################################################################################

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

class Node:
    """ノード
    Attributes:
        key (any): ノードのキー。比較可能なものであれば良い。(1, 4)などタプルも可。
        val (any): ノードの値。
        lch (Node): 左の子ノード。
        rch (Node): 右の子ノード。
        bias (int): 平衡度。(左部分木の高さ)-(右部分木の高さ)。
        size (int): 自分を根とする部分木の大きさ

    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lch = None
        self.rch = None
        self.bias = 0
        self.size = 1

if __name__ == '__main__':
 
    main()