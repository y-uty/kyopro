import bisect
N = int(input())
A = list(map(int, input().split()))
A_rev = A[::-1]


def Calc_LIS(A, INF=10**15, INIT=-10**15):
    N = len(A)

    # L[i]:= 長さがiである増加部分列の末尾の値(=最大値)の最小値
    L = [INF]*(N+1)
    L[0] = INIT
    # dp[i]:= 要素の最後がAiである部分列のうち、最長のものの長さ
    dp = []

    # returnで、LIS, dp, Lのうち必要なものを返す
    LIS = 0
    for i in range(N):
        idx = bisect.bisect_left(L, A[i])
        L[idx] = min(L[idx], A[i])
        if idx > LIS:
            LIS = idx
            dp.append(LIS)
        else:
            dp.append(idx)
            
    return dp


# dpA[i]:= 末尾A[i]のLISの最大長
dpA = Calc_LIS(A)
# dpA_rev[i]:= 末尾A_rev[i]のLISの最大長
# もう一度反転して同じ添え字で前から見られるようにする
dpA_rev = Calc_LIS(A_rev)[::-1]


# すべてのiについて、末尾A[i]となるLISの最大長 + 末尾A_rev[i]となるLISの最大長 - 1 を求め、
# それの最大が答え
ans = 0
for i in range(N):
  ans = max(ans, dpA[i] + dpA_rev[i] - 1)

print(ans)