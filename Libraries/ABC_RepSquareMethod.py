def rep_square_mod(base, log2n, MOD):
    tmp = base
    repsqr = []
    for _ in range(log2n):
        tmp = tmp * tmp
        tmp = tmp % MOD
        repsqr.append(tmp)

    return repsqr

MOD = 10**9+7
# x^(2**y)までを前計算
x = 2 
y = 10
a = rep_square_mod(x, y, MOD)

# 求めたいものはx^z
z = 1
ans = x
for i in range(len(a)):
    if 2**(i+1) & z:
        ans *= a[i]
        ans %= MOD

print(a)
print(ans)