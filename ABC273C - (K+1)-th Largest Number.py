import collections
import bisect
n = int(input())
a = list(map(int, input().split()))

itoai = collections.defaultdict(int)
for i in range(n):
    itoai[i] = a[i]

kth = [0]*n

seta = set(a)
seta = sorted(list(seta))
cnt = len(seta)

for i in range(n):
    x = itoai[i] # Aiを取得

    idx = bisect.bisect_right(seta, x)
    kth[cnt-idx] += 1

print(*kth, sep='\n')