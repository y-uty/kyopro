import collections
import math
N = int(input())
A = list(map(int, input().split()))
gcdA = 0
for i in range(N):
    gcdA = math.gcd(gcdA, A[i])

ans = 0
# minにそろえる
# minAでないaをminAで割る
# わりきれない -> 不可能
# わりきれる -> 商をdとして、dを素因数分解する
# その結果、素因数が2,3のみであれば、指数の和を加算する
# そうでないとき、不可能

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

# x = prime_factorize(1)
# print(x)

for i in range(N):
    # A[i]=minAなら無視
    if A[i] != gcdA:

        # A[i]がminAでわりきれるときだけ考える
        if A[i]%gcdA > 0:
            print(-1)
            exit()
        else:
            # A[i]/minA を素因数分解する
            d = A[i]//gcdA
            fact_d = prime_factorize(d)

            # d=2^p*3^qのとき、答えにp+qを加算
            # それ以外のときはNG
            for k, v in fact_d.items():
                if k > 3:
                    print(-1)
                    exit()
                elif k in (2, 3):
                    ans += v

print(ans)