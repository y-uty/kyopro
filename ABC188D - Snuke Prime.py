from sys import stdin
n, c_prime = map(int, input().split())
c_daily = []

for _ in range(n):
    a, b, c = map(int, stdin.readline().split())
    c_daily.append([a, c]) 
    c_daily.append([b+1, -c]) 

c_daily.sort()

ans = 0
cnt = 0
for i in range(len(c_daily)-1):
    cnt += c_daily[i][1]
    duration = c_daily[i+1][0] - c_daily[i][0]
    ans += duration * min([cnt, c_prime])

print(ans)