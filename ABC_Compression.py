# 二分探索による配列の座標圧縮(1-indexed)
def compression(a, x_indexed=1):
    a_unique = sorted(list(set(a)))
    acomp = []
    for i in range(len(a)):
        ng, ok  = -1, len(a_unique)
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if a_unique[mid] >= a[i]: ok = mid
            else: ng = mid
        acomp.append(ok+x_indexed)
    return acomp