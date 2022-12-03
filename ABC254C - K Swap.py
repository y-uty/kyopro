n, k = map(int, input().split())
a = list(map(int, input().split()))
a_sorted = sorted(a)

import heapq
# 並び替えはk個隣どうしとしかできない
# その組み合わせの中でソートして、Aiソート済結果と合致しなければ即No
for i in range(k):
    b = []
    for j in range(i, n, k):
        heapq.heappush(b, a[j])
 
    for j in range(i, n, k):
        a[j] = heapq.heappop(b)
        if a[j] != a_sorted[j]:
            print('No')
            exit()

print('Yes')
