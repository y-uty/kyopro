a, b, c, d = 0, 0, 0, 0

S = []
S.append(['.']*12)
for _ in range(10):
    s = ['.'] + list(input()) + ['.']
    S.append(s)
S.append(['.']*12)

for i in range(11):
    for j in range(11):
        if S[i][j]+S[i][j+1]=='.#':
            c = j+1
        
        if S[i][j]+S[j][j+1]=='#.':
            d = j

        if S[i][j]+S[i+1][j]=='.#':
            a = i+1

        if S[i][j]+S[i+1][j]=='#.':
            b = i

print(a, b)
print(c, d)