n, k = map(int, input().split())
ans = 0

for i in range(1, n+1):
    inp = i
    cnt = 0
    while inp < k:
        cnt += 1
        inp *= 2

    ans += (1/n * (0.5)**cnt)

print(ans)