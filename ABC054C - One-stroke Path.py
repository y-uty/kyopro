import collections
import itertools
n, m = map(int, input().split())
G = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

x = list(range(2, n+1))
paths = itertools.permutations(x)
ans = 0
for p in paths:
    v_from = 1
    for v_to in p:
        if v_to in G[v_from]:
            v_from = v_to
        else:
            break

    else:
        ans += 1

print(ans)