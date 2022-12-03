n, k = map(int, input().split())
a = list(map(int, input().split()))

def is_ok(x):
    cnt = 0
    for i in range(n):
        cnt += min(a[i], x)
    
    return True if cnt <= k else False

ok, ng  = 0, 10**12+1
def bin_srch_mgr(ok, ng):

    while abs(ok-ng) > 1:

        mid = (ok+ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return ok

# 取り除きK個以下で周回できる最大値を二分探索で求める
cir = bin_srch_mgr(ok, ng)

# 周回後のAiの状態を求めた後、端数処理
cnt = 0
for i in range(n):
    cnt += min(cir, a[i])
    a[i] = max(a[i]-cir, 0)

# K個になるまで、かご1から1個ずつ取り出し
for i in range(n):
    if cnt==k: break

    if a[i] > 0:
        cnt += 1
        a[i] -= 1

print(*a)