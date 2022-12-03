n = int(input())
N = n+(n+1)
eq = list(map(str, input().split())) + ['=']

res = []
tmp = 0
for i in range(N+1):
    if eq[i]=='=':
        res.append(tmp)
        tmp = 0
    elif eq[i]=='+':
        pass
    else:
        tmp += int(eq[i])

chk = res[0]
for i in range(1, len(res)):
    if chk != res[i]:
        print('No')
        exit()

print('Yes')