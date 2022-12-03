N = int(input())
A = list(map(int, input().split()))

# 左端を固定して、右端を高速に見つける必要がある
# 連続部分列について、累積和 >= 累積xor である(どこかのビットが1つでも一度でも複数1になると > になる)から、
# ある左端に対して、累積和 > 累積xor となった場所以降の右端では、絶対に 累積和 = 累積xor とはならない
# したがって、OK/NGには単調性があり、二分探索でその場所をO(logN)で求めることができる

csum = [0] # 累積和
cxor = [0] # 累積xor
for i in range(N):
    csum.append(csum[-1]+A[i])
    cxor.append(cxor[-1]^A[i])
# 末尾で必ずNGとなるように番兵を入れる
# Ai < 2**20より、累積xorが2**20以上になることはない
csum.append(2**20) 
cxor.append(0)

ans = 0
for l in range(1, N+1):

    def is_ok(x):
        # 区間xorは、左側含まない部分をxorとる (A^B^A = B より)
        if csum[x]-csum[l-1]==cxor[x]^cxor[l-1]:
            return True
        else:
            return False

    def bin_srch_mgr(ok, ng):
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            if is_ok(mid): ok = mid
            else: ng = mid
        return ok

    ok, ng = l, N+1
    r = bin_srch_mgr(ok, ng)
    ans += r-l+1

print(ans)
