n, s = map(int, input().split())
bags = []
for _ in range(n):
    a, b = map(int, input().split())
    bags.append([a, b])

# dp[i][j]:= i日目までに購入金額がちょうどj円になる購入計画文字列
# dp[N][S]に購入計画文字列があればそれが答え、なければ'Impossible'
# DP復元で解くことも可能(後述)

# 条件を満たす購入計画(文字列)が複数ある場合はどれを出力してもよいので
# 同じ(i, j)に複数回到達する場合は、上書きでOK

dp = [['']*(s+1) for _ in range(n+1)]
dp[0][0] = '_' # 始点を判別するため文字を入れておく

for i in range(n):
    a_today, b_today = bags[i]
    for j in range(s):
        if len(dp[i][j])>0:
            if j+a_today <= s:
                dp[i+1][j+a_today] = dp[i][j] + 'A'
            if j+b_today <= s:
                dp[i+1][j+b_today] = dp[i][j] + 'B'

if len(dp[-1][-1]) > 0:
    print(dp[-1][-1][1:]) # 始点の文字を除いて出力
else:
    print('Impossible')


### DP復元で解く場合 ###

# テーブルにはTrue/Falseを持つので、テーブル初期化以降から異なるコード

# dp = [[False]*(s+1) for _ in range(n+1)]
# dp[0][0] = True

# for i in range(n):
#     a_today, b_today = bags[i]
#     for j in range(s):
#         if dp[i][j]:
#             if j+a_today <= s:
#                 dp[i+1][j+a_today] = True
#             if j+b_today <= s:
#                 dp[i+1][j+b_today] = True

# if dp[-1][-1]:
#     ans = []
#     j = s
#     for i in range(n, 0, -1):
#         a_yesterday, b_yesterday = bags[i-1]
#         if j-a_yesterday >= 0 and dp[i-1][j-a_yesterday]:
#             ans.append('A')
#             j -= a_yesterday
#         else:
#             ans.append('B')
#             j -= b_yesterday
    
#     print(''.join(ans[::-1]))

# else:
#     print('Impossible')
