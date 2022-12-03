import sys
n = int(input())
max_xply = -10**10
max_xmiy = -10**10
min_xply = 10**10
min_xmiy = 10**10
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if x+y > max_xply: max_xply = x+y
    if x+y < min_xply: min_xply = x+y
    if x-y > max_xmiy: max_xmiy = x-y
    if x-y < min_xmiy: min_xmiy = x-y

d_cand1 = max_xply - min_xply
d_cand2 = max_xmiy - min_xmiy
d_cand3 = -1 * (max_xply - min_xply)
d_cand4 = -1 * (max_xmiy - min_xmiy)

print(max([d_cand1, d_cand2, d_cand3, d_cand4]))
