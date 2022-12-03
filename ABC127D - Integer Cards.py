import sys
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())

# 常に最小値を取り出したいので、優先度付きキューを使う。
a = list(map(int, input().split()))
heapify(a)

upd = []
poppushendflg = False
for _ in range(m):
    # 入替後の数字となるcが大きい順に処理する。
    # aから最小値を取り出したとき、c以上になった時点で、
    # それ以降の入れ替えで最大値を更新することはなく、全体ループをbreakできる。
    b, c = map(int, sys.stdin.readline().split())

    # heapqは最小値を取り出すが、予め-1倍しておくことで最大値を取り出せる。
    upd.append([-1*c, b])
heapify(upd)

for _ in range(m):

    c, b = heappop(upd)

    for _ in range(b):
        tmp = heappop(a)
        if tmp < -1*c:
            # 取り出したら-1倍を戻す
            heappush(a, -1*c)
        else:
            heappush(a, tmp)
            poppushendflg = True
            break

    if poppushendflg:
        break

print(sum(a))