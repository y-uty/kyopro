import itertools
n = int(input())

n2 = bin(n)[2:].zfill(60)
keta = []
for i in range(60):
    if n2[-1-i]=='1':
        keta.append(i)

# bit全探索
anslist = []
for bits in itertools.product([True, False], repeat=len(keta)):
    choice = [x for x, b in zip(keta, bits) if b]
    
    ans = 0
    for c in choice:
        ans += 2**c
    anslist.append(ans)

print(*sorted(anslist), sep='\n')