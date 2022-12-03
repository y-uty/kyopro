n, m = map(int, input().split())

# 色ごとに未発見(-1)or発見済(筒番号:1以上)
part = [-1]*(n+1)

import collections
import sys
# 筒の番号をindexにしてリストにキューを格納
q_list = [0]
for _ in range(m):
    k = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    q = collections.deque(a)
    q_list.append(q)

# 方針: 調べられる筒の番号をキューで管理しつつ、各筒の一番上を順番に調べて、
# 発見済みの場合にその筒と、先に発見したときの筒のキューからボール取り出す。
# 取り出したキューは新・一番上を調べられるので、その筒の番号をキューに追加する。
# 一番上を調べて筒が空だったら、空筒数をカウントアップする。
# 空筒数がMと一致したらYes, 調べられる筒の番号がなくなったらNoを出力する。
q_popok = collections.deque(range(1, m+1))
q_cnt_vacant = 0
while q_popok:
    q_num = q_popok.popleft()

    tmpq = q_list[q_num]
    if tmpq:
        x = tmpq.popleft()

        if part[x] < 0:
            part[x] = q_num
        else:
            q_popok.append(q_num)
            q_popok.append(part[x])
    
    else:
        q_cnt_vacant += 1

    if q_cnt_vacant==m:
        print('Yes')
        exit()

print('No')