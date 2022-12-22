def main():
  N = int(input())
  A = [0] + list(map(int, input().split()))
  maxA = max(A)
  MOD = 998244353

  # 愚直に考えると、k枚目までのカードがあるとき、行x, 列yとしてk行k列の表にmax(x, y)を埋めていき
  # kごとに、k^2マスの総和を求めたのち、それをk^2で割ればよい(どのマスも等確率)
  # (k-1)*(k-1)の部分を後から書き換えることはないため、総和を取るのは累積和的に考えればよさそうで、
  # k行目とk列目の2*k-1マスを高速に求められれば良い
  
  # 行と列は対称位置で同じ値になるから、行を埋めることだけを考える
  # k枚目のカードをaとすると、下記の2パターンとなる
  #  (1) a以下のカードの列は、すべてaで埋まる
  #  (2) aより大きいカードの列は、それらの値で埋まる
  # よって、aを境界としてそれ以下orそれより大きい領域での区間和を高速に求めたい
  # そこで、(1)のために「添字をカードの値として、値ごとの登場回数を記録するBIT」、
  # (2)のために「添字をカードの値として、値が登場する度に値を加算するBIT」をそれぞれ用意して更新していく
  # これによって、(1)について 1 ~ a, (2)について a+1 ~ max(A) の区間和を求めれば各kについて解答できる
  # ただし、(1)を2倍すると増えた分の右隅が重複するので、aを引いておくのを忘れずに

  FTcount = BIT(maxA)
  FTsum = BIT(maxA)
  E = [0]*(N+1)

  # K=1
  E[1] = A[1]
  FTcount.add(A[1], 1)
  FTsum.add(A[1], A[1])
  print(E[1])

  # K>=2
  for i in range(2, N+1):
    a = A[i]
    # i枚目のカードについてBITに反映
    FTcount.add(a, 1)
    FTsum.add(a, a)

    # 期待値の加算分を求める
    x1 = FTcount.get(a)*a*2 - a
    x2 = (FTsum.get(maxA) - FTsum.get(a))*2
    X = x1+x2
    Y = pow(i**2, MOD-2, MOD)
    E[i] = E[i-1]+X

    ans = E[i]*Y%MOD
    print(ans)




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
  