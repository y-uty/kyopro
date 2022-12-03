import sys
import math
import itertools
q = int(input())

# 取りうる素数を列挙する O(nlog logn)
# x = 素数の2倍 - 1 として、xが10**5以下の素数であれば、
# 2017リストのindex=xのフラグを立てる O(n)
# 累積和をとる O(n)
# クエリ処理 print(2017[r]-2017[l-1]) O(q)

# 素数列挙:エラトステネスの篩
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    prime_set = set(list(range(2, n+1)))

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
                prime_set.discard(j)

    return prime_set

like2017 = [0]*(10**5+1)

prime_set = sieve_of_eratosthenes(10**5)
prime_list = list(prime_set)
for p in prime_list:
    px = 2*p - 1
    if (px in prime_set) and px <= 10**5:
        like2017[px] = 1

anslist = list(itertools.accumulate(like2017))      

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(anslist[r]-anslist[l-1])