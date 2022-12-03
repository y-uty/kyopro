n, r = map(int, input().split())
M = 10**9+7

# nCr = n! / r!*(n-r)! mod M を高速に求める
#  1. 分子 n! をMで割った余りaを繰り返し二乗法で求める
#  2. 分母 r!*(n-r)! をMで割った余りbを繰り返し二乗法で求める
#  3. a*b^(M-2) をMで割った余りを繰り返し二乗法で求める -> これが答え

# 1. 分子 a = n!
a = 1
for i in range(1, n+1): a = (a*i)%M

# 2. 分母 b = r!*(n-r)!
b = 1
for i in range(1, r+1): b = (b*i)%M
for i in range(1, n-r+1): b = (b*i)%M

# 3. ans = a*b^(M-2)%M -> b^(M-2)%M
ans = a * pow(b, M-2, M) % M
print(ans)