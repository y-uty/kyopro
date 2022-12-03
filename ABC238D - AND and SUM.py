import sys
T = int(input())

for _ in range(T):
    a, s = map(int, sys.stdin.readline().split())

    b = s-2*a # a = x&y , b = x^y

    if b < 0:
        print('No')
        continue

    abin = bin(a)[2:].zfill(60)
    bbin = bin(b)[2:].zfill(60)

    flg = True
    for i in range(60):
        if abin[i]=='1':
            if bbin[i]!='0':
                flg = False
                break

    if flg:
        print('Yes')
    else:
        print('No')