import sys
import collections
import copy
sys.setrecursionlimit(10**7)
n, q = map(int, input().split())
x = [-1] + list(map(int, input().split()))
T = collections.defaultdict(list)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    T[a].append(b)
    T[b].append(a)

INF = -1
# dp[i][j]:= 頂点iを根とする部分木に含まれる頂点でj番目に大きい整数
# 葉から順に、直接の子のdp[child]を全部集めて、そのうち大きい順20個だけをdp[i]とする
dp = [[INF]*20 for _ in range(n+1)]
for i in range(1, n+1): dp[i][0] = x[i]

visited = [False]*(n+1)
def dfs(v_from):
    visited[v_from] = True

    # v_fromを根とする部分木の整数大きい順20個
    # そのまま代入だとdpテーブルも更新されてしまうのでcopy
    children = copy.deepcopy(dp[v_from])

    for v_to in T[v_from]:
        if not visited[v_to]:

            # 直接の子のdp[child]を集める
            children += dfs(v_to)
    
    # 降順ソートして大きい順に20個選ぶ
    children.sort(reverse=True)
    for i in range(20):
        dp[v_from][i] = children[i]
    
    return dp[v_from] # 直接の親に返す

# 根からDFSしてdpテーブル作成
dfs(1)

# dpテーブルができているので、あとはdp[V][K]を答えればOK
for _ in range(q):
    v, k = map(int, sys.stdin.readline().split())
    print(dp[v][k-1])
