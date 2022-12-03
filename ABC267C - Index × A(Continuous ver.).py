n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
prev = 0
for i in range(m):
    ans += (i+1)*a[i]
    prev += a[i]

tmp = ans
for i in range(m, n):
    tmp -= prev
    tmp += m*a[i]

    prev -= a[i-m]
    prev += a[i]
    ans = max(ans, tmp)

print(ans)