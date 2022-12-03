N = int(input())
H = list(map(int, input().split()))

stay_ok = True
sage_ok = True

for i in range(N-1):
    if stay_ok: stay = H[i]
    if sage_ok: sage = H[i] - 1

    stay_ok = True if stay <= H[i+1] or sage <= H[i+1] else False
    sage_ok = True if stay <= H[i+1]-1 or sage <= H[i+1]-1 else False
        
    if not (stay_ok or sage_ok):
        print('No')
        exit()

print('Yes')