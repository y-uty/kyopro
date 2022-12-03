n = int(input())

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

import collections
p_fac = prime_factorize(n)
p_cnt = collections.Counter(p_fac)
p_exp = collections.defaultdict(int)
p_num = collections.deque(list(p_cnt.keys()))

ans = 0

while p_num:
    p = p_num.popleft()
    p_exp[p] += 1

    if p_cnt[p] >= p_exp[p]:
        ans += 1
        p_cnt[p] -= p_exp[p]

        p_num.appendleft(p)

print(ans)