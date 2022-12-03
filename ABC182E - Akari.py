def main():
    import sys
    h, w, n, m = map(int, input().split())
    masu = [[0]*w for _ in range(h)]

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        masu[a-1][b-1] = 2

    for _ in range(m):
        c, d = map(int, sys.stdin.readline().split())
        masu[c-1][d-1] = -1


    range_h = list(range(h))
    range_w = list(range(w))
    range_h_rev = list(range(h-1, -1, -1))
    range_w_rev = list(range(w-1, -1, -1))

    # 行方向
    for i in range_h:
        # 左から右へ
        lit = False
        for j in range_w:
            if masu[i][j]==2:
                lit = lit | True
            elif masu[i][j]==-1:
                lit = lit & False        
            if lit:
                masu[i][j] = 1 if masu[i][j]==0 else masu[i][j]
        # 右から左へ
        lit = False
        for j in range_w_rev:
            if masu[i][j]==2:
                lit = lit | True
            elif masu[i][j]==-1:
                lit = lit & False       
            if lit:
                masu[i][j] = 1 if masu[i][j]==0 else masu[i][j]

    ans = 0

    # 列方向
    for i in range_w:
        # 上から下へ
        lit = False
        for j in range_h:
            if masu[j][i]==2:
                lit = lit | True
            elif masu[j][i]==-1:
                lit = lit & False    
            if lit:
                masu[j][i] = 1 if masu[j][i]==0 else masu[j][i]
        # 下から上へ
        lit = False
        for j in range_h_rev:
            if masu[j][i]==2:
                lit = lit | True
            elif masu[j][i]==-1:
                lit = lit & False
            
            if lit:
                masu[j][i] = 1 if masu[j][i]==0 else masu[j][i]
            if masu[j][i] >= 1:
                ans = ans + 1

    print(ans)

if __name__ == '__main__':
    main()