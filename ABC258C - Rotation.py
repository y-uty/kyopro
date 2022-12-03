import sys
import collections
n, q = map(int, input().split())
s = ['#'] + list(str(input()))
l = len(s)-1

offset = l+1
for _ in range(q):
    t, x = map(int, sys.stdin.readline().split())

    if t==1:
        offset -= x

    else:
        idx = (offset + (x-1))%l
        if idx==0:
            print(s[-1])
        else:
            print(s[idx])
    
    if offset==1:
        offset += l
