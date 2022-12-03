import sys
n, x = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

anslist = []
tmp = 0
cnt = 0
rep = 10**9*1
# より短い時間でクリアできるステージが待ってるなら先に進んだほうがよい
# 短時間化を期待して進むなら、前のステージに戻って繰り返すことはない
for i in range(n):
    a, b = g[i]
    tmp += a+b
    cnt += 1
    if cnt >= x: # xがnより小さい場合、最終ステージに辿り着くことはない
        anslist.append(tmp)
        break
           
    # 最小時間でクリアできるものだけを貪欲に繰り返しクリアしてかかる時間が解答候補
    rep = min([rep, b])
    anslist.append(tmp+rep*(x-cnt))

print(min(anslist))   
