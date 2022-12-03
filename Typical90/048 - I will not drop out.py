import sys
import heapq
n, k = map(int, input().split())
score_part = []
score_all = []

# 1手にかかるコストは変わらない(1分)から、
# 常にそのときとれる最大利益の手段をとればよい
# 部分点をとったあとは、(満点-部分点)が選択肢に加わる
# 逆に、その問題の部分点を取るまでは満点も取れないことに注意

# 実装は、常に最大(最小)を取り出せる優先度付きキューを使う

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(score_part, [-b, i])
    score_all.append(-(a-b))

ans = 0
for t in range(k):
    x, y = heapq.heappop(score_part)
    ans -= x

    if y>=0:
        heapq.heappush(score_part, [score_all[y], -1])
    
print(ans)