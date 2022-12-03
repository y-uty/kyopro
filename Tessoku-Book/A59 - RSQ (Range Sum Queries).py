def main():
    N, Q = map(int, input().split())
    A = [0]*(N+1)

    rsq = BIT(N)

    for _ in range(Q):
        t, q1, q2 = map(int, sys.stdin.readline().split())

        if t==1:
            # A[i]をXにする -> A[i]に(X-A[i])を加算する
            pos = q1
            x = q2
            rsq.add(pos, x-A[pos])
            A[pos] = x

        else:
            l = q1
            r = q2-1
            ans = rsq.get(r) - rsq.get(l-1)
            print(ans)


####################################################################################################
####################################################################################################
class BIT():
    def __init__(self, n, id_elem=0):
        self.id_elem = id_elem
        self.bit = [id_elem]*n
        self.bit_size = n+1

    def add(self, i, x):
        # i: bitの要素番号(1-indexed)
        # x: bit[i]に対して作用させる値
        while i < self.bit_size:
            self.bit[i-1] += x
            i += i & -i # 最後の1のビットを加算

    def get(self, i):
        # i: 1~iまでの累積作用結果を取得する(1-indexed)
        ret = self.id_elem # 単位元で初期化
        while i > 0:
            ret += self.bit[i-1]
            i -= i & -i # 最後の1のビットを減算
        return ret

if __name__ == '__main__':
    import sys
    import collections
    import itertools
    import heapq
    import math
    import copy

    main()