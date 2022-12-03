N = int(input())
A = [int(i) for i in input().split()]

import collections

c = collections.Counter(A)

a = c.most_common()[-1][0]

print(a)