n, t = map(int, input().split())
a = list(map(int, input().split()))

tsum = 0
for i in range(1, n):
    tsum += min([a[i]-a[i-1], t])

print(tsum+t)