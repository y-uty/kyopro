def main():
  N, Q = map(int, input().split())
  C = [0] + list(map(int, input().split()))

  ColRight = [-1]*(N+1) # 色iの最も右の位置
  FT = BIT(N) # 最も右の色の球があるとき1, ないとき0
  # クエリの答えは、[l, r]にある「色ごとに最も右の位置の玉」の総和 
  
  # rの昇順に応える
  queries = []
  ans = [0]*Q
  # クエリをrの昇順に処理する
  for i in range(Q):
    l, r = map(int, input().split())
    queries.append((r, l, i))
  queries.sort(operator.itemgetter(0))

  now = 1 # Cの状態をどこまで反映したか
  for qry in queries:
    r, l, qno = qry

    # Cの状態を、rまで順に更新する
    while now <= r:
      c = C[now]
      # 最も右の位置を更新する
      # その色が左に登場済みの場合は、削除してから
      if ColRight[c] >= 0:
        prev = ColRight[c]
        FT.add(prev, -1)
      
      ColRight[c] = now
      FT.add(now, 1)

      now += 1
    
    # クエリ回答
    tmp = FT.get(r) - FT.get(l-1)
    ans[qno] = tmp

  print(*ans)


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


if __name__=="__main__":
  import sys
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator
  import copy

  main()