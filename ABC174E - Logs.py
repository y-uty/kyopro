import math
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)


# k回カット後に、xを最長にできるか？
def is_ok(x):
    ktmp = k

    for i in range(n):
        atmp = a[i]
        cutcnt = atmp//x
        if cutcnt > ktmp:
            return False
        elif cutcnt == ktmp:
            if i==n-1 or a[i+1] <= x:
                return True
            else:
                return False
        else:
            ktmp -= cutcnt

    return True


# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
ok, ng  = max(a), 0
# 連続値の二分探索
def bin_srch_mgr(ok, ng):

    # 十分小さくなるまで繰り返す
    for _ in range(100):

        mid = (ok+ng) / 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return ok

ans = bin_srch_mgr(ok, ng)

if ans-math.floor(ans) < 1e-15:
    print(math.floor(ans))
else:
    print(math.ceil(ans))
