n = int(input())
nlen = len(str(n))

if n % 3 == 0:
    print(0)
    exit()

ketalist = list(str(n))

import itertools
for i in range(nlen, 0, -1):
    comb = itertools.combinations(ketalist, i)
    for c in comb:
        if int(''.join(c)) % 3 == 0:
            print(nlen-i)
            exit()

print(-1)