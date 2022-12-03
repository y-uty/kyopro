import sys
h, w, n = map(int, input().split())

a_bisect = set()
b_bisect = set()
cards = []
ans = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a_bisect.add(a)
    b_bisect.add(b)
    cards.append([a, b])

a_bisect = sorted(list(a_bisect))
b_bisect = sorted(list(b_bisect))

from bisect import bisect_right
for i in range(n):
    a_idx = bisect_right(a_bisect, cards[i][0])
    b_idx = bisect_right(b_bisect, cards[i][1])
    print(str(a_idx) + ' ' + str(b_idx))