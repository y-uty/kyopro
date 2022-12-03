Sn = int(input())
ans = 0

# 約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divs = make_divisors(2*Sn)

for d in divs:
    # dは項数
    if ((2*Sn)//d - d + 1) % 2 == 0: # 初項の計算結果が整数であれば和がSnの数列が存在する
        ans += 1

print(ans)