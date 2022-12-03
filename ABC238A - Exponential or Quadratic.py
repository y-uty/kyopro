n = int(input())

import math

if n > 2*(math.log(n, 2)):
    print('Yes')
else:
    print('No')