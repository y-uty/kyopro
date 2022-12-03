import sys
import collections
n = int(input())

# 頂点数-1の辺があり、全ての頂点に行き来可能、つまり与えられるグラフは木
# 木のどこかに辺を1つ追加すると、1つだけ閉路ができる
# よって、互いに最も遠い場所にある点対を選び、それらを結ぶ辺を追加すれば条件を満たす道ができる
# 従って、「互いに最も遠い場所にある点対」を結ぶパスの長さがわかれば、答えはそれ+1である

# そのようなパスの長さは木の直径とよばれる
# 木の任意の頂点を根とし、距離が同じ頂点を1つのグループとして見ると、
# 木の頂点間の移動は、根を起点に左右に広がる線分上の移動ととらえることができ、
# 木の直径はこの線分の長さに等しい
# 従って、木のは、任意の頂点から最も遠い点を調べ(線分のより遠い端点へ移動)、
# そこからもう一度最も遠い点を調べる(線分の他端へ移動)ことで求めることができる

tr = collections.defaultdict(list)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tr[a].append(b)
    tr[b].append(a)

steps = [-1]*(n+1)
steps[1] = 0
nx = collections.deque([1])
while nx:
    v_from = nx.popleft()

    for v_to in tr[v_from]:
        if steps[v_to] >= 0: continue

        steps[v_to] = steps[v_from] + 1
        nx.append(v_to)

farthest = steps.index(max(steps))

steps = [-1]*(n+1)
steps[farthest] = 0
nx = collections.deque([farthest])
while nx:
    v_from = nx.popleft()

    for v_to in tr[v_from]:
        if steps[v_to] >= 0: continue

        steps[v_to] = steps[v_from] + 1
        nx.append(v_to)

ans = max(steps) + 1
print(ans)