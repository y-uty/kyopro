import sys
import collections
n = int(input())

req = collections.defaultdict(int)
for i in range(n):
    s = str(sys.stdin.readline().replace('\n', ''))
    if req[s]:
       pass 
    else:
        print(i+1)
        req[s] += 1