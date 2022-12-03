x, y = map(int, input().split())

if (x+y)%3 != 0:
    print(0)
    exit()
elif x*2==y or x==2*y:
    print(1)
    exit()

a = (2*x-y)//3
b = (y-a)//2

min_ab = min([a, b])
max_ab = max([a, b])

if min_ab<0:
    print(0)
    exit()
elif min_ab==0:
    print(max_ab)
    exit()


MOD = 10**9+7
f_all = 1
f_a = 1
f_b = 1
for i in range(1, a+b+1):
    f_all *= i
    f_all %= MOD

    if i==a: f_a = f_all
    if i==b: f_b = f_all

f_ab = (f_a * f_b)%MOD
# モジュラ逆数 分母**(M-2) を繰り返し二乗法で求める
f_ab_inv = 1
for i in range(31): # 29 < log 10^9 < 30

    # nの2進数表示で2^iの桁が1 <=> n and 2^i != 0
    if (MOD-2) & (2**i) != 0:
        f_ab_inv = (f_ab_inv * f_ab)%MOD

    f_ab = (f_ab**2)%MOD

print((f_all*f_ab_inv)%MOD)