import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict

G = defaultdict(list)
N = int(input())
W = []
for i in range(N):
    sys.stdin.readline
    w = list(map(int, input().split()))
    W.append(w)
    G[i] = w[2:]

v_arrived = N-1
global tsum
tsum = 0
seen = [False] * N

def dfs(seen, v_arrived):
    global tsum
    tsum += W[v_arrived][0]
    seen[v_arrived] = True

    if (len(G[v_arrived]) > 0):
        for v_reachable in G[v_arrived]:
            if seen[v_reachable-1] == False:
                dfs(seen, v_reachable-1)

dfs(seen, v_arrived)

print(tsum)
