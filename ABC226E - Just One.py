def main():
    import sys
    import collections
    n, m = map(int, input().split())
    e = []
    G = collections.defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        e.append([u, v])
    # e.sort()
    ans = 0
    MOD = 998244353
    loop_cnt = [0]*n
    uf = UnionFind(n)

    # 連結成分ごとの閉路の個数をカウントする
    # 閉路がちょうど1つの連結成分のみに2通りあり、その掛け合わせが答え
    for i in range(m):
        a, b = e[i]
        ret = uf.union(a-1, b-1)
        if ret==0: # union結果が0 <=> 閉路ができた
            pr = uf.find(a-1)
            loop_cnt[pr] += 1

    for i in range(n):
        # 辺を持たない頂点がある場合、即NG
        if uf.parents[i]==-1:
            print(0)
            exit()

        if loop_cnt[i] > 0:
            i_am_p = uf.find(i)
            if i_am_p != i: # 自分がrootではない場合、本当のrootへ移管
                loop_cnt[i_am_p] += loop_cnt[i]
                loop_cnt[i] =  0

    for i in range(n):
        if loop_cnt[i]==1:
            if ans>0:
                ans = (ans*2)%MOD
            else:
                ans = 2
        elif loop_cnt[i]>1:
            print(0)
            exit()

    print(ans)

# https://note.nkmk.me/python-union-find/

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

if __name__ == '__main__':
    main()