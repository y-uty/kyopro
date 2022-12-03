N, K = map(int, input().split())
A = list(map(int, input().split()))

p = A[:K]
amin = min(p)
print(amin)

import heapq
heapq.heapify(p)

for i in range(K, N):
    # 現時点のPの最小よりも、追加する数字が大きければ、それと入れ替える（そうでなければ元に戻す）
    pmin = heapq.heappop(p)
    pmin = max(pmin, A[i])
    heapq.heappush(p, pmin)

    # Pの最小を取り出して出力し、またPに戻す
    amin = heapq.heappop(p)
    print(amin)
    heapq.heappush(p, amin)
