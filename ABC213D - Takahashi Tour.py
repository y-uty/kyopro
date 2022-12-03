import sys
import collections
n = int(input())
G = collections.defaultdict(list)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

for k in G.keys():
    G[k] = collections.deque(sorted(G[k]))

ans = []
def bfs(v_stt):
    procflg = True
    seen = [0]*n
    v_from = v_stt
    seen[v_stt-1] = 1

    while procflg:
        ans.append(v_from)
        
        existflg = False
        q_v_next = G[v_from]
        while q_v_next:
            v_next = q_v_next.popleft()
            if seen[v_next-1] > 0:
                pass
            else:
                seen[v_next-1] = v_from
                v_from = v_next
                existflg = True
                break
                
        if existflg==False:
            if v_from == 1:
                procflg = False
            else:
                v_from = seen[v_from-1]

bfs(1)
print(*ans)