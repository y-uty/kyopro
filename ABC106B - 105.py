N = int(input())

Ncnt = 0

for i in range(1, N+1, 2):
    dcnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            dcnt += 1
    
    if dcnt == 8:
        Ncnt += 1

print(Ncnt)