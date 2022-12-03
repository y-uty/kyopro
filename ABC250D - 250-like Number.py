n = int(input())

# 素数列挙:エラトステネスの篩
import math
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

prime_set = sieve_of_eratosthenes(math.floor(n**(1/3)))
prime_set.discard(2)
prime_list = sorted(list(prime_set))

import bisect
p = [2]

ans = 0
# q未満の素数のうち、k // q^3 以下であるものがpとなるので、二分探索で個数を数える
for q in prime_list:
    k_ok = n // (q**3)
    ans += bisect.bisect_right(p, k_ok)
    p.append(q)

print(ans)