def main():
  K = int(input())
  factK = prime_factorize(K)

  def is_ok(X, pK, eK):
    # X!がpKで割れる回数cntをルジャンドルの定理で求める
    cnt = 0
    Y = pK
    while Y <= X:
      cnt += int(X//Y)
      Y *= pK

    # cntがeK以上であれば、X!は条件を満たす
    if cnt >= eK:
      return True
    else:
      return False


  # 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
  def bin_srch_mgr(ok, ng, pK, eK):
      while abs(ok-ng) > 1:
          mid = (ok+ng) // 2
          if is_ok(mid, pK, eK): ok = mid
          else: ng = mid
      return ok

  ans = 2
  for pK, eK in factK.items():
    # pK が eK回登場するような最小のNを二分探索で求める
    ok = 10**100
    ng = 1
    tmp = bin_srch_mgr(ok, ng, pK, eK)

    ans = max(ans, tmp)

  print(ans)
  


  # 素因数分解 O(√N)
def prime_factorize(n):
    a = collections.defaultdict(int)
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2 # 2以外の偶数は素因数にならない
    if n != 1:
        a[n] += 1
    return a # n=1は空list


if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator

  main()