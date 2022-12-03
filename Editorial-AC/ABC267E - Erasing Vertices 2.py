import sys
import collections

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
G = collections.defaultdict(list)
cost_v = [0]*(N+1)
for _ in range(M):
    U, V = map(int, sys.stdin.readline().split())
    G[U].append(V)
    G[V].append(U)
    cost_v[U] += A[V]
    cost_v[V] += A[U]
maxcost = max(cost_v)

def is_ok(X):
    C = cost_v[::]
    erasable = collections.deque()
    erased = [False]*(N+1)
    cnt_erase = 0
    # 初期状態でeraseできる頂点を入れる
    for i in range(1, N+1):
        if cost_v[i] <= X:
            erasable.append(i)

    while erasable:
        v_erase = erasable.pop()
        # 削除済みの頂点は無視
        if erased[v_erase]: continue
        else:
            erased[v_erase] = True
            cnt_erase += 1

        for v_adj in G[v_erase]:
            # 削除済みの頂点は無視
            if erased[v_adj]: continue
            
            C[v_adj] -= A[v_erase]
            if C[v_adj] <= X:
                erasable.append(v_adj)

    if cnt_erase==N:
        return True
    else:
        return False
    
# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
def bin_srch_mgr(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid): ok = mid
        else: ng = mid
        print(mid)
    return ok

ok, ng  = maxcost, -1   
ans = bin_srch_mgr(ok, ng)
print(ans)