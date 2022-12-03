N = int(input())

S = []
for i in range(N):
    s = list(input())
    S.append(s)

# check in horizontal
for i in range(N):
    for j in range(N-6+1):
        if S[i][j:j+6].count('#') >= 4:
            print('Yes')
            exit()

# check in vertical
S_t = list(zip(*S))
for i in range(N):
    for j in range(N-6+1):
        if S_t[i][j:j+6].count('#') >= 4:
            print('Yes')
            exit()

# check in diagonal
for i in range(N-6+1):
    for j in range(N-6+1):
        s_diag = []
        for k in range(6):
            s_diag.append(S[i+k][j+k])
        if s_diag.count('#') >= 4:
            print('Yes')
            exit()

for i in range(N-6+1):
    for j in range(N-1, 5-1, -1):
        s_diag = []
        for k in range(6):
            s_diag.append(S[i+k][j-k])
        if s_diag.count('#') >= 4:
            print('Yes')
            exit()

print('No')
