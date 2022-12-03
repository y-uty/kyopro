import collections
n = int(input())
p = 10**9+7
if n==1:
    print(1)
    exit()

facts = collections.defaultdict(int)
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

for i in range(2, n+1):
    fs = prime_factorize(i)
    for f in fs:
        facts[f] += 1

ans = 1
for v in facts.values():
    ans *= v+1
    ans %= p

print(ans)