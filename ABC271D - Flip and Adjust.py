n, s = map(int, input().split())
cards = []
for _ in range(n):
    a, b = map(int, input().split())
    cards.append((a, b)) # (表, 裏)

# dp[i][j][k]:=i枚目までで最後にk向きにおいたときの総和がjになるかどうか
dp = [[[False]*(2) for _ in range(s+1)] for _ in range(n+1)]
dp[0][0][0] = True
dp[0][0][1] = True

for i in range(n): # 1~N
    a, b = cards[i]

    for j in range(s+1):

        for k in range(2): # 0:表, 1:裏

            if dp[i][j][k]:
                if j+a <= s:
                    dp[i+1][j+a][0] = True
                if j+b <= s:
                    dp[i+1][j+b][1] = True

if not (dp[n][s][0] or dp[n][s][1]):
    print('No')
    exit()



ans = ['H'] if dp[n][s][0] else ['T']

j = s
k = 0 if dp[n][s][0] else 1
for i in range(n, 0, -1):
    
    a, b = cards[i-1]
    x = a if k==0 else b

    if dp[i-1][j-x][0]:
        ans.append('H')
        j -= x
        k = 0
    else:
        ans.append('T')
        j -= x
        k = 1

ans = ans[:n]
print('Yes')
print(''.join(ans[::-1]))