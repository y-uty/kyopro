X = input()
N = int(input())

atoz = [chr(i) for i in range(97, 123)]
strl = []

import collections
neord = collections.defaultdict(str)
abord = collections.defaultdict(str)

for i in range(26):
    neord[X[i]] = atoz[i]
    abord[atoz[i]] = X[i]
neord = dict(neord)
abord = dict(abord)

for i in range(N):
    S = input()
    S = S.translate(str.maketrans(neord))   
    strl.append(S)

strl.sort()

for i in strl:
    ans = str(i).translate(str.maketrans(abord))
    print(ans)
