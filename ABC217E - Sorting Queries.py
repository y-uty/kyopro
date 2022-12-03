import sys
import collections
import heapq
q = int(input())

# クエリ1の追加は通常キュー
appended = collections.deque()

# クエリ3の並び替えは優先度付きキュー
ordered = []
heapq.heapify(ordered)

for _ in range(q):
    qry = list(map(int, sys.stdin.readline().split()))

    if qry[0]==1:
        appended.append(qry[1])

    elif qry[0]==2:
        # 並び替え済みのものがある(=優先度付きキューが空でない)場合はそちらから
        if ordered:
            ans = heapq.heappop(ordered)
        else:
            ans = appended.popleft()
        
        print(ans)

    else:
        # 並び替えは、通常キューを全て優先度付きキューに移すことで実現
        while appended:
            x = appended.popleft()
            heapq.heappush(ordered, x)