x = list(str(input()))
sum_x = 0
for i in range(len(x)):
    sum_x += int(x[i])

import collections
ans = collections.deque()
agari = 0
for i in range(len(x)):
    tmp = sum_x + agari
    ans_tmp = str(tmp)[-1]
    if len(str(tmp)) > 1:
        agari = int(str(tmp)[:-1])
    else:
        agari = 0
    ans.appendleft(ans_tmp)
    sum_x -= int(x[-1-i])

if agari > 0:
    ans.appendleft(str(agari))
print(''.join(ans))