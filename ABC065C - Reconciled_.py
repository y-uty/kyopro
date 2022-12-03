n, m = map(int, input().split())

MOD = 10**9+7

def calc_factorial_mod(x):
    x_fact = 1
    while x > 0:
        x_fact = (x_fact * x) % MOD
        x -= 1
    return x_fact

if abs(n-m) > 1:
    print(0)
elif n==m:
    ans = (calc_factorial_mod(n) ** 2) * 2
    print(ans%MOD)
else:
    min_fact = calc_factorial_mod(min([n, m]))
    ans = min_fact * (min_fact * max([n, m]))
    print(ans%MOD)
