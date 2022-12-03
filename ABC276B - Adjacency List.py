import sys
import collections
N, M = map(int, input().split())
G = collections.defaultdict(list)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    G[A].append(B)
    G[B].append(A)

for i in range(1, N+1):
    anslist = G[i]
    anscnt = len(anslist)

    anslist.sort()
    print(anscnt, *anslist)
