# N, Q = map(int, input().split())
# A = [int(i) for i in input().split()]

# m = dict()

# for i in range(N):
#     # key(a_iの値)が既にdictにある場合value(その数がある場所list)を追加
#     if A[i] in m:
#         m[A[i]].append(i+1)
#     # keyが無い場合はつくる
#     else:
#         m[A[i]] = [i+1]

# for q in range(Q):
#     x, k = map(int, input().split())
#     if x in m:
#         if k <= len(m[x]):
#             print(m[x][k-1])
#         else:
#             print(-1)
#     else: # そもそもクエリで問う数がa_nに存在しない場合
#         print(-1)

# =================================================================

# defaultdictを用いた実装(ライブラリimport必要)
# 存在しないkeyが指定されたときdefault値(今回なら空list)で要素を追加してくれる
# これにより、keyが存在しない場合の条件分岐不要となる
from collections import defaultdict
N, Q = map(int, input().split())
A = [int(i) for i in input().split()]

m = defaultdict(list) # 存在しないkey指定->空listで要素追加

for i in range(N):
    # 新しいkeyの要素をつくりながらappend
    m[A[i]].append(i+1)

for q in range(Q):
    x, k = map(int, input().split())
    # keyがなくても空list生成されlen=0で判定可
    if k <= len(m[x]):
        print(m[x][k-1])
    else:
        print(-1)
