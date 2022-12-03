s = '_' + str(input())
col = [0]*7

col[0] += 1 if s[7]=='1' else 0
col[1] += 1 if s[4]=='1' else 0
col[2] += 1 if s[8]=='1' else 0
col[2] += 1 if s[2]=='1' else 0
col[3] += 1 if s[5]=='1' else 0
col[3] += 1 if s[1]=='1' else 0
col[4] += 1 if s[9]=='1' else 0
col[4] += 1 if s[3]=='1' else 0
col[5] += 1 if s[6]=='1' else 0
col[6] += 1 if s[10]=='1' else 0
# print(col)
if s[1]=='1':
    print('No')
    exit()

for i in range(1, 6):
    if col[i]==0:
        x = max(col[:i])
        y = max(col[i+1:])
        if x>=1 and y>=1:
            print('Yes')
            exit()

print('No')
