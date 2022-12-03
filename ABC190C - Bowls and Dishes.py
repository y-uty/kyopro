import sys
n, m = map(int, input().split())

cond = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cond.append([a, b])

k = int(input())

pe = []
for _ in range(k):
    c, d = map(int, sys.stdin.readline().split())
    pe.append([c, d])

ans = 0

# bit全探索
for i in range(2**k):
    b = format(i, '0'+str(k)+'b')
    tmp = 0
    dishes = [0]*n

    for j in range(k):
        if b[j]=='0':
            dishes[pe[j][0]-1] += 1
        else:
            dishes[pe[j][1]-1] += 1
    
    for l in range(m):
        if dishes[cond[l][0]-1] and dishes[cond[l][1]-1]:
            tmp += 1
    
    if tmp > ans:
        ans = tmp

print(ans)