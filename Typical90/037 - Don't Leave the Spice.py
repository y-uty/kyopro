def main():
    # a = [10,1,3,4,5]
    # def add(x,y):
    #     return x+y
    # segtr = SegmentTree(a, add, 0)
    # print(segtr.query(0, 5))

    import sys
    w, n = map(int, input().split())
    spice = []
    for i in range(n):
        s = list(map(int, sys.stdin.readline().split()))
        spice.append(s)

    # dp[i][j]:= i番目までの料理を、合計j[mg]の香辛料で作ったときの価値の最大
    # 区間の最大値をlog(区間の長さ)でもらうDP
    INF = -1
    dp = [[INF]*(w+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = 0

    # dp[i][j] = max(dp[i-1][j-R],...,dp[i-1][j-L])+Vi or dp[i-1][j]
    ans = -1
    for i in range(1, n+1):
        segtr = SegmentTree(dp[i-1], max, INF)
        l, r, v = spice[i-1]
        
        for j in range(1, w+1):
            if j>=l:
                max_used = segtr.query(max(j-r, 0), j-l+1)
                if max_used==INF:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(max_used+v, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
        
        ans = max(ans, dp[i][-1])
  
    print(ans)

            
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

class SegmentTree:
    def __init__(self, init_val, function=min, element=float("inf"),
                 default: int = 0, enable_cutoff=True) -> None:
        """
        init_val: 配列の初期値
        function: 区間にしたい操作
        element: 単位元
        n: 要素数
        tree: セグメント木(1-index)
        """
        if hasattr(init_val, "__iter__"):
            self.n = len(init_val)
            self.tree = [element] * self.n + list(init_val)
        else:
            self.n = init_val
            self.tree = [default] * 2 * self.n
        self.function = function
        self.element = element
        self.enable_cutoff = enable_cutoff
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.function(
                self.tree[i << 1], self.tree[(i << 1) + 1])

    def update(self, i: int, x: int) -> None:
        # assert 0 <= i < self.n
        i += self.n
        self.tree[i] = x
        self._propagates(i)

    def add(self, i: int, x: int) -> None:
        # assert 0 <= i < self.n
        i += self.n
        self.tree[i] += x
        self._propagates(i)

    def _propagates(self, i: int) -> None:
        # assert self.n <= i < self.n * 2
        if self.enable_cutoff:
            while i:
                i >>= 1
                before = self.function(
                    self.tree[i << 1], self.tree[(i << 1) + 1])
                if self.tree[i] == before:
                    return
                self.tree[i] = before
        else:
            while i:
                i >>= 1
                self.tree[i] = self.function(
                    self.tree[i << 1], self.tree[(i << 1) + 1])

    def query(self, l: int, r: int) -> int:
        # assert 0 <= l < self.n
        # assert 0 < r <= self.n
        l += self.n
        r += self.n
        res = self.element
        while l < r:
            if l & 1:
                res = self.function(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.function(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

    def get(self, index: int) -> int:
        # assert 0 <= index < self.n
        return self.tree[index + self.n]

    def get_list(self, l: int = 0, r: int = None) -> list:
        # assert 0 <= l < self.n
        if r is None:
            r = self.n
        # assert 0 < r <= self.n
        return self.tree[l + self.n: r + self.n]

if __name__ == '__main__':
    main()