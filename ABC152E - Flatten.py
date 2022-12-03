import collections
n = int(input())
a = list(map(int, input().split()))
MOD = 10**9+7

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


fcnt = collections.defaultdict(int)
for i in range(n):
    x = a[i]
    fcnt_now = prime_factorize(x)
    
    for k, v in fcnt_now.items():
        if fcnt[k] >= v:
            pass
        else:
            fcnt[k] = v

lcm_ = 1
for k, v in fcnt.items():
    lcm_ *= k**v

ans = 0
for i in range(n):
    ans += (lcm_//a[i])%MOD

print(ans%MOD)
