n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = '_' + str(input())

dp = [[0]*2 for _ in range(n+1)]

def pwin(rsp):
    if rsp=='r':
        return p
    elif rsp=='s':
        return r
    else:
        return s

# Win/Loseで最大値を取るdp
# Winを求めるときは、k手先のtが一致するとき-1で埋める
# dp[Win][i] == -1 のときはスルーする
for i in range(1, n+1):
    # Win
    if dp[i][0] < 0:
        pass
    else:
        dp[i][0] = max([dp[i-1][0], dp[i-1][1]]) + pwin(t[i])
        
        if i + k <= n and t[i]==t[i+k]:
            dp[i+k][0] = -1

    # Lose
    dp[i][1] = max([dp[i-1][0], dp[i-1][1]])

print(max([dp[n][0], dp[n][1]]))