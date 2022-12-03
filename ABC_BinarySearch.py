### めぐる式二分探索 ###
# 問題に応じて条件を満たすかを判定する関数を定義.
a = list(range(0, 10**6+1, 5))
n = 12

def is_ok(x):
    if n >= a[x]:
        return True
    else:
        return False

# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
ok, ng  = 10**9, -1
def bin_srch_mgr(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid): ok = mid
        else: ng = mid
    return ok
