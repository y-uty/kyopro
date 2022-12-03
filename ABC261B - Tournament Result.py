n = int(input())
res = []
for _ in range(n):
    a = list(str(input()))
    res.append(a)

for i in range(n):
    for j in range(n):
        if i==j: continue

        x = res[i][j]
        y = res[j][i]

        if x=='W':
            if y!='L':
                print('incorrect')
                exit()
        
        elif x=='D':
            if y!='D':
                print('incorrect')
                exit()
        
        elif x=='L':
            if y!='W':
                print('incorrect')
                exit()

print('correct')