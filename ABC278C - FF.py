import sys
import collections
N, Q = map(int, input().split())

follow = collections.defaultdict(set) # ｋがvをfollowしている
for _ in range(Q):
    T, A, B = map(int, sys.stdin.readline().split())

    if T==1:
        follow[A].add(B)
    elif T==2:
        follow[A].discard(B)
    else:
        if B in follow[A] and A in follow[B]:
            print("Yes")
        else:
            print("No")
