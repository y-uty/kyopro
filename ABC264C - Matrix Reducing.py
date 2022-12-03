h1, w1 = map(int, input().split())
A = []
for _ in range(h1):
    r1 = list(map(int, input().split()))
    A.append(r1)

h2, w2 = map(int, input().split())
B = []
for _ in range(h2):
    r2 = list(map(int, input().split()))
    B.append(r2)


for i in range(1, 2**h1): # 行
    b_row = bin(i)[2:].zfill(h1)
    chk_row = []
    for r in range(h1):
        if b_row[r]=='1':
            chk_row.append(r)

    for j in range(1, 2**w1): # 列
        b_col = bin(j)[2:].zfill(w1)
        chk_col = []

        for c in range(w1):
            if b_col[c]=='1':
                chk_col.append(c)

        tmp = []
        for x in chk_row:
            tmp_row = []
            for  y in chk_col:
                tmp_row.append(A[x][y])
            tmp.append(tmp_row)
        
        if tmp==B:
            print('Yes')
            exit()         
            
print('No')