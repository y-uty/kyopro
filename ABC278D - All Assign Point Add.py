import sys
import collections
N = int(input())
A = [0] + list(map(int, input().split()))

Adict = collections.defaultdict(int)
for i in range(1, N+1):
    Adict[i] = A[i]

Q = int(input())

all_add = 0
for _ in range(Q):
    qry = list(map(int, sys.stdin.readline().split()))

    t = qry[0]

    if t==1:
        x = qry[1]
        Adict.clear()
        all_add = x

    elif t==2:
        i, x = qry[1], qry[2]
        Adict[i] += x

    else:
        i = qry[1]
        print(Adict[i]+all_add)
