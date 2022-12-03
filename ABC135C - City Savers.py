n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    x = min(a[i], b[i])
    a[i] -= x
    b[i] -= x
    ans += x

    y = min(a[i+1], b[i])
    a[i+1] -= y
    b[i] -= y
    ans += y

print(ans)
