import bisect
n = int(input())
a = list(map(int, input().split()))

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