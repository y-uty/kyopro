import math
import collections
n = int(input())
a = list(map(int, input().split()))


# 互いに素 <=> 共通の素因数を持たない
fact_pair = set()
fact_set = set()
pair_flag = True
set_flag = False
gcd_ = 0

# 素因数分解 O(√N)
def prime_factorize(n):
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2 # 2以外の偶数は素因数にならない
    if n != 1:
        a.add(n)
    return a # n=1は空をreturn

for i in range(n):
    x = a[i]

    if (not pair_flag) and set_flag:
        break # pairwiseでない かつ setwiseである が確定した

    facts_x = prime_factorize(x)
    if i==0: fact_set=facts_x

    # 一度でも同じ素因数が現れたらpairwise coprimeではない
    if len(fact_pair & facts_x) == 0:
        fact_pair |= facts_x
    else:
        pair_flag = False

    # 一度しか現れない素因数が1つでもあればsetwise copirmeである
    if len(fact_set & facts_x) == 0 or x==1: # Aiに1が含まれるならGCD(Ai)は1にしかならない
        set_flag = True
    else:
        fact_set &= facts_x

if pair_flag:
    print('pairwise coprime')
elif set_flag:
    print('setwise coprime')
else:
    print('not coprime')
