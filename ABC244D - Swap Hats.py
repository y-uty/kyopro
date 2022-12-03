S = list(map(str, input().split()))
T = list(map(str, input().split()))

matchcnt = 0
for i in range(3):
    if S[i] == T[i]:
        matchcnt += 1

if matchcnt == 1:
    print('No')
else:
    print('Yes')
