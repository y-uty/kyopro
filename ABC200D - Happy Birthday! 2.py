n = int(input())
a = list(map(int, input().split()))

dp = [[0]*(200) for _ in range(n+1)]
brk = False

for i in range(1, n+1):
    # そのまま下ろす. 選び方は同じパターン.
    for k in range(200):
        if dp[i-1][k] > 0:
            dp[i][k] = dp[i-1][k]

    # Aiのみを選ぶ場合. 選び方は別パターン.
    x = a[i-1]%200
    # 既存パターンとかち合うなら答え.
    if dp[i][x] > 0:
        b = dp[i][x]
        c = 2**i
        brk = True
        break
    else:
        dp[i][x] = 2**i

    # 使うAiを増やす時の遷移
    for j in range(200):
        if dp[i-1][j] > 0:
            m = (x+j)%200

            # 既存パターンとかち合うなら答え.
            if dp[i][m] == 0:
                dp[i][m] = dp[i-1][j] + 2**i
            else:
                b = dp[i][m]
                c = dp[i-1][j] + 2**i
                brk = True
                break
    
    if brk: break

if brk:
    print('Yes')
    b = format(b, '0200b')
    c = format(c, '0200b')
    bcnt, ccnt = 0, 0
    bans, cans = [], []
    for i in range(200):
        if b[i]=='1':
            bcnt += 1
            bans.append(199-i)
        if c[i]=='1':
            ccnt += 1
            cans.append(199-i)
    print(bcnt, *bans[::-1])
    print(ccnt, *cans[::-1])

else:
    print('No')