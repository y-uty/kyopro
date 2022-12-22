def main():
  N, K, M = map(int, input().split())
  p = 998244353

  # 答えは M^(K^N) mod p
  # フェルマーの小定理より、a, pが互いに素ならば、a^(p-1) ≡ 1 (mod p) 
  # よって、Mの指数部分のうち、p-1乗ぶんは1に置き換えられる
  # したがって、K^N % (p-1) のみを考えればよく、これをLとすると、答えは M^L % p
  # また、aがpの倍数である場合、(aのべき乗) ≡ 0 (mod p) であるから、答えは0
  
  if M%p==0:
    print(0)
  else:
    L = pow(K, N, p-1)
    print(pow(M, L, p))



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