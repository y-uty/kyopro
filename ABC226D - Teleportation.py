import sys
import math
n = int(input())

cities = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    cities.append([x, y])

import collections
magics = collections.defaultdict(int)

import itertools
c_perm = itertools.permutations(cities, 2)

# x, y座標の距離を、それぞれ最大公約数で割った値が答え
# (a, b) = (2, 3), (4, 6)が候補になったら、より小さい方だけを残せばよい
for c in c_perm:

    dist_x = c[1][0] - c[0][0]
    dist_y = c[1][1] - c[0][1]

    gcd_xy = math.gcd(dist_x, dist_y)
    # (a, b)の組でカウントしたいので、文字列をkeyにする
    magics[str(dist_x//gcd_xy) + ','+ str(dist_y//gcd_xy)] += 1

print(len(magics.keys()))