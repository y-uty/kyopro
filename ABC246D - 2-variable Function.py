n = int(input())

def ansfunc(x1, x2):
    return x1**3 + x1**2 * x2 + x1 * x2**2 + x2**3

def is_ok(x):
    if ansfunc(a, x)>=n:
        return True
    else:
        return False

# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
def bin_srch_mgr(ok, ng):

    while abs(ok-ng) > 1:

        mid = (ok+ng) // 2
        # print(ok, ng)

        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return ok

ans = 10**19
# aを固定して、n以上となるxをつくるbを二分探索で求める
for a in range(10**6+1):
    ng, ok  = -1, 10**6
    b_bound = bin_srch_mgr(ok, ng)
    # 求めたbでxを求める
    tmp = ansfunc(a, b_bound)

    # 答えはxの最小値
    if tmp < ans:
        ans = tmp

print(ans)