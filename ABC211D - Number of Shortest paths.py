n, m = map(int, input().split())
import sys
import collections

G = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

costs = [n]*(n+1) # 最小コストの最大値はn-1
paths = [0]*(n+1)

MOD = 10**9 + 7
def bfs(v_start):
    q_vtxs = collections.deque()
    q_vtxs.append(v_start)
    costs[v_start] = 0
    paths[v_start] = 1

    while q_vtxs:
        v_from = q_vtxs.popleft()

        for v_to in G[v_from]:
            tmp_min_steps = costs[v_from] + 1

            # from頂点の最小コスト+1が、to頂点の最小コストより小さければ、更新
            # 更新するとき、経路数は上書き
            if tmp_min_steps < costs[v_to]:
                costs[v_to] = tmp_min_steps
                paths[v_to] = paths[v_from]

                q_vtxs.append(v_to)
            
            # 記録済みの最小コストと同一コストのとき、経路数は加算
            elif tmp_min_steps == costs[v_to]:
                paths[v_to] += paths[v_from] % MOD

bfs(1)

print(paths[-1] % MOD)