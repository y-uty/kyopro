N = int(input())

# 素因数分解 O(√N)
import collections
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
            f += 2
    if n != 1:
        a[n] += 1
    return a

# Kが約数をちょうど75個もつのは、異なる素数p, q, rを用いて
# p^4 * q^4 * r^2
# p^14 * q^4
# p^24 * q^2
# p^74
# のいずれかで表すことができるときである
fs = collections.defaultdict(int)
ans = set()
import itertools
for i in range(2, N+1):
    f = prime_factorize(i)
    for k, v in f.items():
        fs[k] += v

    flist = []
    for k, v in fs.items():
        flist.append((v, k))

    # p^4 * q^4 * r^2
    fcomb = itertools.permutations(flist, 3)
    for fc in fcomb:
        kv1, kv2, kv3 = fc
        v1, k1 = kv1
        v2, k2 = kv2
        v3, k3 = kv3
        if v1 >= 2 and v2 >= 4 and v3 >= 4:
            ans.add(k1**2 * k2**4 * k3**4)
        
    # p^14 * q^4
    fcomb = itertools.permutations(flist, 2)
    for fc in fcomb:
        kv1, kv2 = fc
        v1, k1 = kv1
        v2, k2 = kv2
        if v1 >= 4 and v2 >= 14:
            ans.add(k1**4 * k2**14)
    # p^24 * q^2
        if v1 >= 2 and v2 >= 24:
            ans.add(k1**2 * k2**24)

    # p^74
    for v, k in flist:
        if v >= 74: ans.add(k**74)

print(len(ans))
