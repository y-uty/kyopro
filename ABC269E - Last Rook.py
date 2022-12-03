import sys
n = int(input())

# 盤面を縦に分割して、二分探索的にRookがいない列を決める -> log(1000)<10
# 同様に横分割でルークがいない行を決める
# 合計20回以下で、ルークが置ける(i, j)がわかる

# X列目までのルークの数がX-1個であるようなXの最小値
def is_ok_col(x):
    print('?', 1, n, 1, x)
    sys.stdout.flush()
    t = int(input())

    if t < x:
        return True
    else:
        return False


# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
ok, ng  = n, 0
def bin_srch_mgr_col(ok, ng):

    while abs(ok-ng) > 1:

        mid = (ok+ng) // 2

        if is_ok_col(mid):
            ok = mid
        else:
            ng = mid

    return ok

ans_col = bin_srch_mgr_col(ok, ng)

# X行目までのルークの数がX-1個であるようなXの最小値
def is_ok_row(x):
    print('?', 1, x, 1, n)
    sys.stdout.flush()
    t = int(input())

    if t < x:
        return True
    else:
        return False

# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
ok, ng  = n, 0
def bin_srch_mgr_row(ok, ng):

    while abs(ok-ng) > 1:

        mid = (ok+ng) // 2

        if is_ok_row(mid):
            ok = mid
        else:
            ng = mid

    return ok

ans_row = bin_srch_mgr_row(ok, ng)

print('!', ans_row, ans_col)
exit()
