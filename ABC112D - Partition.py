n, m = map(int, input().split())

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

divs = make_divisors(m)

for i in range(len(divs)):
    d = divs[-1-i]

    if m-d*n>=0 and (m-d*n)%d==0:
        print(d)
        exit()

print(1)