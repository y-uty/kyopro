N, A, B = map(int, input().split()) # A < B

# 「石が0個で先手ターン」の状態から考える
# まず、石を1個も取れない=何もできない状態は負け
# そうでないとき、負けの状態に遷移できる方法があるなら勝ち、それ以外は負け
# 石がN個になったとき、その状態が勝ち/負けどちらかで先手の勝敗が決まる

dp = [False]*(N+1) # 石がi個のとき、先手が勝ち(True)/負け(False)どちらの状態か？
for i in range(1, N+1):
    if i >= A:
        if not dp[i-A]:
            dp[i] = True

    if i >= B:
        if not dp[i-B]:
            dp[i] = True

if dp[N]:
    print('First')
else:
    print('Second')