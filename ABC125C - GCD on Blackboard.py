import math
n = int(input())
a = sorted(list(map(int, input().split())))
amin = a[0] # 全体のGCDはmin(Ai)を超えないので基準とする

def make_divisors(n): # 約数リスト(降順)作成
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return  upper_divisors + lower_divisors[::-1]

# min(Ai)が仲間外れ⇒それ以外の全体GCDが答え
gcd_except_mina = 0
for i in range(1, n):
    gcd_except_mina = math.gcd(gcd_except_mina, a[i])

# min(Ai)の約数を持たないAiが、1個以下であれば直ちに最適
# ただし、min(Ai)が仲間外れの場合はgcd_except_minaが答え
divs = make_divisors(amin)
for d in divs:
    cnt = 0
    for i in range(1, n):
        if a[i]%d == 0:
            cnt += 1
    
    if cnt >= n-2:
        print(max([d, gcd_except_mina]))
        exit()
