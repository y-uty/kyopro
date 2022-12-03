n = int(input())
import collections
cblue = collections.defaultdict(int)
cred = collections.defaultdict(int)
for _ in range(n):
    cblue[str(input())] += 1
m = int(input())
for _ in range(m):
    cred[str(input())] += 1

ans = 0
for k, v in cblue.items():
    if v > cred[k]:
        tmp = v - cred[k]
        if tmp > ans:
            ans = tmp

print(ans)