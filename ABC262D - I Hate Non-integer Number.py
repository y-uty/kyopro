n = int(input())
a = list(map(int, input().split()))

ans = 0
MOD = 998244353
# 何個の平均か？を固定する; その個数をmとする
# dpで余りを状態として持つので、除数を揃えるため
for m in range(1, n+1):
    # dp_m[i][j][k]:= i個めまででj個選んだ合計をmで割った余りがkとなるような選び方の数
    dp_m = [[[0]*n for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n):
        # i+1個で初めて選ぶ
        dp_m[i+1][1][a[i]%m] += 1

        for j in range(m+1):
            for k in range(n):

                # 選ばない
                dp_m[i+1][j][k] = (dp_m[i+1][j][k] + dp_m[i][j][k])%MOD
                
                # 選ぶ
                if j < m:
                    k_next = (k+a[i])%m
                    dp_m[i+1][j+1][k_next] = (dp_m[i+1][j+1][k_next] + dp_m[i][j][k])%MOD

    # 合計をmで割った余りが0のときm個の平均が整数になる
    ans += dp_m[n][m][0]
    ans %= MOD

print(ans)