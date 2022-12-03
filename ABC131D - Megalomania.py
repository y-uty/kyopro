N = int(input())
import sys
tasks = []
for _ in range(N):
    req, dead = map(int, sys.stdin.readline().split())
    tasks.append([dead, req])

tasks.sort()

csumtime = 0

for t in tasks:
    csumtime += t[1]
    if csumtime > t[0]:
        print('No')
        exit()

print('Yes')