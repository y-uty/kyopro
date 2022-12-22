def main():
  N = int(input())
  A = list(map(int, input().split()))

  # 高橋がAiを選ぶとき、青木にはAi以下のものを選ばせる必要がある
  # 青木から見ると、高橋がBiを選ぶので、自分はBi以上を選ぶ必要がある
  # よって、(高橋のプレゼントNo, 青木のプレゼントNo) = (i, j)とすると、
  # Ai >= Aj かつ Bi <= Bj が成り立つ(i, j)の組が、求める答えとなる

  # 点(A, B)をxy二次元座標にプロットすると、
  # 高橋がAiを選ぶとき、青木が選ぶ点はx <= Aiの領域にあることが必要で、
  # 逆に言えば、Aを昇順に見ながら固定して考えると、登場済みの点だけで適切なBをカウントできればよくなる
  # -> Ai登場時、BiをFenwick Treeに記録して、Bi以上となる点の個数を答えに加算する(Bは座標圧縮する)

  # ただし、下記の2点に注意
  # 1. Aが等しい異なる点については、Bの降順に見る(そうしないと、自分より上側にいるはずのBがカウントできない)
  # 2. A, Bともに等しい異なる点については、まとめて加算する(1.と同じような理由)


  # Bを座標圧縮
  B = compression(list(map(int, input().split())))

  # 同じ座標をまとめる
  ABdict = collections.defaultdict(int)
  for i in range(N):
    ABdict[(A[i], B[i])] += 1
    
  # Aの昇順、Bの降順にsort
  X = []
  for k, cnt in ABdict.items():
    a, b = k
    X.append((a, -b, cnt))
  X.sort()

  # 答えを求めていく
  ans = 0
  FT = BIT(N)
  for a, b, cnt in X:
    b *= -1
    FT.add(b, cnt)
    ans += (FT.get(N) - FT.get(b-1))*cnt

  print(ans)




def compression(a, x_indexed=1):
    a_unique = sorted(list(set(a)))
    acomp = []
    for i in range(len(a)):
        ng, ok  = -1, len(a_unique)
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if a_unique[mid] >= a[i]: ok = mid
            else: ng = mid
        acomp.append(ok+x_indexed)
    return acomp

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
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator
  import copy

  main()