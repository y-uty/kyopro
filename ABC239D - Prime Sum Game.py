a, b, c, d = map(int, input().split())

import math
winner = 'Aoki'

def prornot(x):
    if x == 2:
        return 1
    
    for i in range(1, math.ceil(pow(x, 1/2))):
        if x % (i+1) == 0:
            return 0
    
    return 1

for taka in range(a, b+1):
    prexist = []
    for aoki in range(c, d+1):
        pr = taka + aoki
        jd = prornot(pr)
        prexist.append(jd)

    if max(prexist) == 0:
        winner = 'Takahashi'
        break


print(winner)