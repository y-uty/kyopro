n = int(input())

ans = 0
for i in range(1, n):
    # i回目の遷移
    ans += n/(n-i)

print(ans)
