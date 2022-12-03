import collections
import heapq
N, M, T, K = map(int, input().split())

roads = collections.defaultdict(list)
for _ in range(M):
    a, b, c, d = map(int, input().split())
    roads[a].append((c, b, d))
    roads[b].append((c, a, d))


INF = 10**18
nx = []
cost = [INF]*(N+1)
cost[1] = 0
fixed = [False]*(N+1)

heapq.heappush(nx, (0, 1))

while nx:
    _, v_from = heapq.heappop(nx)

    if fixed[v_from]: continue

    fixed[v_from] = True

    for c_to, v_to, d_to in roads[v_from]:

        ks = d_to-T-K
        kg = d_to+T-K

        ts = cost[v_from]
        tg = ts+c_to

        # 行き先への到着時刻を求める
        if tg <= ks:
            pass # tgのまま
        elif ts > ks and ts < kg:
            tg = kg+c_to
        elif tg > ks and tg < kg:
            tg = kg+c_to
        elif ts <= ks and tg >= kg:
            tg = kg+c_to
        else: # ts >= kg
            pass
            
        if cost[v_to] > tg:
            cost[v_to] = tg
            heapq.heappush(nx, (tg, v_to))

if cost[N] < INF:
    print(cost[N])
else:
    print(-1)