n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0

for i in range(n):
    ans += (-1*n + 2*(i+1) - 1) * a[i]

print(ans)