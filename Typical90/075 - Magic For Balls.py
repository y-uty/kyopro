import collections
import math
n = int(input())

# 素因数分解 O(√N)
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2 # 2以外の偶数は素因数にならない
    if n != 1:
        a.append(n)
    return a # n=1は空list

p = prime_factorize(n)
cnt = collections.Counter(p)
num = sum(tuple(cnt.values()))

if num==1:
    print(0)
else:
    print(math.ceil(math.log2(num)))