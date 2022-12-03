import sys
import collections
n = int(input())
cnt = collections.defaultdict(int)
for _ in range(n):
    s = str(sys.stdin.readline().replace('\n', ''))
    if cnt[s]==0:
        print(s)
    else:
        x = cnt[s]
        print(s+'('+str(x)+')')
    
    cnt[s] += 1