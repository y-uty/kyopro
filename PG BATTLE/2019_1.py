W, K, D = map(int, input().split())

if D >= K and D >= (W-K):
    print('Yes')
else:
    print('No')