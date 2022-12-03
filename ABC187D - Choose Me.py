import sys
n = int(input())
votes = []
aoki = 0
taka = 0
ans = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    votes.append([a+(a+b), a+b, a])
    aoki += a

votes.sort(reverse=True)

for v in votes:
    ans += 1
    taka += v[1] # += a+b
    aoki -= v[2] # -= a
    if taka > aoki:
        print(ans)
        exit()