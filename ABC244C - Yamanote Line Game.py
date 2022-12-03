import sys
import numpy as np

N = int(input())

n = list(np.arange(2,2*N+2))
print(1)
sys.stdout.flush()

for i in range(N):
    aoki = int(input())
    n.remove(aoki)
    print(n[0])
    n.remove(n[0])
    sys.stdout.flush()

takahashiwin = int(input())
