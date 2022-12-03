h, w, k = map(int, input().split())
row_sum = []
col_sum = [0]*w
ans = 0

C = []
for _ in range(h):
    c_row = list((str(input())).replace('#', '1').replace('.', '0'))
    for j in range(w):
        c_row[j] = int(c_row[j])
        col_sum[j] += c_row[j]
    row_sum.append(sum(c_row))

    C.append(c_row)

tot = sum(row_sum)

# bit全探索
for x in range(2**(h+w)):
    tmp = 0
    b = format(x, '0'+str(h+w)+'b')
    
    b_row = b[:h]
    b_col = b[h:]

    # bitを行/列の部分に分解して、1が立っているindexのrow/col_sum配列を参照して加算
    for i in range(h):
        if int(b_row[i]):
            tmp += row_sum[i]
    for j in range(w):
        if int(b_col[j]):
            tmp += col_sum[j]

    # 行i, 列jを同時に選ぶとき、包除原理により要素i, jのぶんを減算
    for i in range(h):
        for j in range(w):
            if int(b_row[i]) and int(b_col[j]):
                tmp -= C[i][j]   

    if tot-tmp==k:
        ans += 1

print(ans)