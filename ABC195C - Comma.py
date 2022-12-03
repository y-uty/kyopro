N = int(input())

keta = len(str(N))
ans = 0
comma = (keta-1) // 3

for i in range(comma):
    base = 10 ** (3 * (i+1))
    if i + 1 < comma:
        ans += (base * 1000 - base) * (i + 1)
    else:
        ans += (N - base + 1) * (i + 1)

print(ans)