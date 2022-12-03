import math
n, a, b = map(int, input().split())
A = list(map(int, input().split()))

# 最小値の最大を求める -> 二分探索が使えそう
# あるK以上で必ずTrue、それ以外で必ずFalseとなる判定に落とし込めればよい
# -> 「操作後のmin(Ai)をK以上にできるか？」

# AiがK以下のとき、最小値がK以上であるためには、K-Aiだけ加算しなければならない
# そのためには、少なくともceil((K-Ai)/a)回の操作が必要
# aを足す操作とbを引く操作は必ず1回ずつ行わなければならない.
# AiがKより大きいとき、K未満にならないように、floor((Ai-K)/b)回の操作が可能
# よって、Ai<=Kのceil((K-Ai)/a)の合計が、AI>Kのfloor((Ai-K)/b)の合計以下であればよい

# これは、Aiすべてについて調べてO(N)である
# 制約 0 < Ai < 10^9 より、[0, 10^9+1)で二分探索する(右端はmax(Ai)でよいが)
# 全体計算量 O(N log10^9)

def is_ok(k):
    tmp_plus = 0
    tmp_minus = 0
    for i in range(n):
        x = A[i]
        if x <= k:
            tmp_plus += math.ceil((k-x)/a)
        else:
            tmp_minus += math.floor((x-k)/b)

    if tmp_minus >= tmp_plus:
        return True
    else:
        return False

ok, ng  = 0, 10**9+1
def bin_srch_mgr(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bin_srch_mgr(ok, ng)
print(ans)