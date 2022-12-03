import sys
h, w = map(int, input().split())
masu = []
for _ in range(h):
    a = list(sys.stdin.readline().replace('\n', ''))
    masu.append(a)

# 初手から考えるといろんな可能性があってどうにもならない
# マス(H, W)からは互いのスコアの増減は無いので、ここの状態は一意に定められるから、
# 最終局面から逆順で考える(ゲーム系の常套手段)

# 2人のスコアをそれぞれ考えると大変だが、勝敗さえわかればよいので、
# X = 高橋のスコア - 青木のスコア とするとその正負だけを考えれば良い
# また、こうすると、高橋は自分の手番でXを最大化するように、
# 青木は自分の手番でXを最小化するように操作するのが最善となる

# dp[i][j]:= マス(i, j)から先手でゲームを始めたときのXの最適値(Max/Min)とする
# 各マスは、(i+j)が奇数なら高橋が、偶数なら青木が踏むマスなので、
# (i+j)の偶奇によって、dp[i][j]を最大化するか、最小化するか考えれば良い
# 移動先は下か右なので、dp[i][j]は、マス(i, j)で増減するスコアをp(i, j)とすると
# dp[i+1][j]+p(i+1, j) か dp[i][j+1]+p(i, j+1) の最適な方、となる

# p(i+1, j)は、マスに書かれた文字が+/-で+1/-1を判定することになるが、
# 青木の手番の場合は+/- -> -1/+1とする点にだけ注意して、dpの遷移を記述する

def p(s, i ,j):
    # +/-とi+jの偶奇(どちらの手番か)に応じて値を返す
    if s=='+':
        if (i+j)%2==0:
            return 1
        else:
            return -1
    elif s=='-':
        if (i+j)%2==0:
            return -1
        else:
            return 1

dp = [[0]*w for _ in range(h)]

for i in range(h-1, -1, -1):
    for j in range(w-1, -1, -1):
        if i==h-1 and j==w-1: continue

        # マス外参照に注意

        if (i+j)%2==0: # turn: Takahashi
            if i+1 == h:
                dp[i][j] = dp[i][j+1]+p(masu[i][j+1], i, j)
            elif j+1 == w:
                dp[i][j] = dp[i+1][j]+p(masu[i+1][j], i, j)
            else:
                dp[i][j] = max(dp[i+1][j]+p(masu[i+1][j], i, j), dp[i][j+1]+p(masu[i][j+1], i, j))

        else: # turn: Aoki
            if i+1 == h:
                dp[i][j] = dp[i][j+1]+p(masu[i][j+1], i, j)
            elif j+1 == w:
                dp[i][j] = dp[i+1][j]+p(masu[i+1][j], i, j)
            else:
                dp[i][j] = min(dp[i+1][j]+p(masu[i+1][j], i, j), dp[i][j+1]+p(masu[i][j+1], i, j))

if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] < 0:
    print('Aoki')
else:
    print('Draw')
