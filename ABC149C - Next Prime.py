X = int(input())
brflg = False
ans = 0

import math
def prornot(x):
    if x < 2:
        return 0

    if x == 2:
        return 1
    
    for i in range(1, math.ceil(pow(x, 1/2))):
        if x % (i+1) == 0:
            return 0
    
    return 1

while brflg == False:
    if prornot(X):
        ans = X
        brflg = True
    else:
        X += 1

print(ans)