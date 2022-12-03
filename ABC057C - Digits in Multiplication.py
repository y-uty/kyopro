n = int(input())

def make_divisors(n):
    ans = 11
    i = 1
    while i*i <= n:
        if n % i == 0:
            div1 = i
            div2 = n // i
            f = max([len(str(div1)), len(str(div2))])
            if f < ans:
                ans = f
        i += 1
    return ans

print(make_divisors(n))