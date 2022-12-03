n = int(input())
s = str(input())
w = list(map(int, input().split()))

import heapq
import collections
x = []
for i in range(n):
    heapq.heappush(x, [-1*w[i], s[i]])

cp_cnt = collections.Counter(s)

anslist = [cp_cnt['1'], cp_cnt['0']]
ans = 0
while x:
    wt, cp = heapq.heappop(x)
    if cp == '1':
        ans += 1
        cp_cnt['1'] -= 1
        anslist.append(ans+cp_cnt['0'])

    else:
        cp_cnt['0'] -= 1
        anslist.append(ans+cp_cnt['0'])

print(max(anslist))