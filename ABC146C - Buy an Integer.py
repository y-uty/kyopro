a, b, x = map(int, input().split())

# X円で整数Nが買えるとき、より小さいどの整数N'も、X円で買うことができる
# よって、Nで二分探索して買える/買えないの境界を見つける

def is_ok(n): # NをX円で買えるか？ O(1)
    if x >= a*n + b*len(str(n)):
        return True
    else:
        return False

# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
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
