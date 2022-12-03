import sys
import heapq
import collections
q = int(input())

bag = []
heapq.heapify(bag)

q_qry = collections.deque()
p2_sum = 0

# 全クエリのうち、加算する操作で加算される数の総和を先に求めておく
for _ in range(q):
    qry = list(map(int, sys.stdin.readline().split()))

    if qry[0]==2:
        p2_sum += qry[1]

    q_qry.append(qry)

# 加算総和を加算してpushする
# 加算操作で加算総和を減算する
# popして加算総和を減算して出力
while q_qry:
    qry = q_qry.popleft()

    if qry[0]==1:
        heapq.heappush(bag, qry[1]+p2_sum)

    elif qry[0]==3:
        ans = heapq.heappop(bag) - p2_sum
        print(ans)
    
    else:
        p2_sum -= qry[1]
