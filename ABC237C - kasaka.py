S = list(str(input()))

x = 0
y = 0

for i in range(len(S)):
    if S[i] == 'a':
        pass
    else:
        x = i
        break

for j in range(len(S), 0, -1):
    if S[j-1] == 'a':
        pass
    else:
        y = len(S) - j
        break

if x > y:
    print('No')
else:
    n = y - x
    T = list(reversed(S))
    for _ in range(n):
        T.append('a')
    for l in range(len(T)):
        if T[l] != T[len(T)-1-l]:
            print('No')
            exit()
        else:
            pass
    print('Yes')