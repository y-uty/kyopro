n = int(input())
p = int(''.join(list(map(str, input().split()))))
q = int(''.join(list(map(str, input().split()))))

import itertools
perm = itertools.permutations([str(i) for i in range(1, n+1)])
cnt = 0
a = 0
b = 0
for x in perm:
    cnt += 1
    if int(''.join(list(x))) == p:
        a = cnt
    if int(''.join(list(x))) == q:
        b = cnt

print(abs(a-b))