N =int(input())
A = list(map(int, input().split()))

colset = set()
gte3200 = 0

for i in range(N):
    div = A[i] // 400
    if div <= 7:
        colset.add(div)
    else:
        gte3200 += 1

if len(colset) == 0: # gte 3200 only
    ansmin = 1
    ansmax = min([gte3200, 8])
else:
    ansmin = len(colset)
    # ansmax = min([len(colset)+gte3200, 8])
    ansmax = len(colset)+gte3200

print(str(ansmin) + ' ' + str(ansmax))