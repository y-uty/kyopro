def main():
    import bisect
    N, L, R = map(int, input().split())
    X = list(map(int, input().split()))

    # dp[i]:= 足場1から足場iに到達する後必要なジャンプ回数のMin
    # X<=10^9と大きいため、そのままdp配列に持つことはできない
    # 足場i に行きたいとき、 X[i]-R 以上で最小の足場l ~ X[i]-L以下で最大の足場r
    # のいずれかからであれば、足場i にいくことができる
    # このl, rは、Xから二分探索で求められる

    # dp[i] = min(dp[l], dp[l+1], ..., dp[r-1], dp[r]) + 1 であるから、
    # dp配列をセグメント木に持ち、最小値の取得と更新を行うことで、O(NlogN)で答えを求められる
    # 実装上の注意:
    #   1. [i]-L, X[i]-R が負のときは0にする
    #   2. 足場i へ到達できる足場が無い場合は、dp[i]=INFとする
    INF = 10**10
    segtr = SegmentTree([0]*N, min, INF)

    for i in range(1, N):
        x_now = X[i]

        l = bisect.bisect_left(X, max(0, x_now-R))
        r = bisect.bisect_right(X, max(0, x_now-L))

        if r-l==0:
            ans = INF
        else:
            ans = segtr.query(l, r) + 1
        segtr.update(i, ans)

    print(segtr.get(N-1))


####################################################################################################
####################################################################################################

class SegmentTree:
    def __init__(self, init_val, function=min, element=float("inf"),
                 default: int = 0, enable_cutoff=True) -> None:
        """
        init_val: 配列の初期値
        function: 区間にしたい操作
        element: 単位元
        n: 要素数
        tree: セグメント木(0-index)
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

    # 区間[l, r) における演算結果を取得する
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
    import sys
    import collections
    import itertools
    import heapq
    import math
    import copy

    main()