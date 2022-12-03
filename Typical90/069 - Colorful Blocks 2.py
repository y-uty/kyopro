n, k = map(int, input().split())

# はじめの3個の選び方はkP3
# それより後は、k-2色から選ぶのをn-3回繰り返す
# よって、求める答えは kP3 * (k-2)^(n-3) mod 10**9+7
# n<=10^18より、(k-2)^(n-3)の部分は繰り返し2乗法で求める

# nやkが小さいケースは例外として先に処理しておく
if n==1:
    print(k)
    exit()
elif n==2:
    if k==1:
        print(0)
    else:
        print(k*(k-1))
    exit()

if k<3:
    print(0)
    exit()

MOD = 10**9+7
kp3 = k*(k-1)*(k-2)
kp3 %= MOD

ans = 1
repexp2 = k-2 # 累乗していきたい値
for i in range(61): # 59 < 10^18 < 60
    if (n-3) & 2**i != 0:
        ans *= repexp2
        ans %= MOD
    
    repexp2 *= repexp2
    repexp2 %= MOD
    
ans *= kp3
print(ans%MOD)