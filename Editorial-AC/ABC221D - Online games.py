import sys

n = int(input())

lilo = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    # login/outの日付を1つにまとめて、最後にソートする
    # どちらなのかは+1/-1で区別する(そのまま人数の加算に用いる)
    lilo.append([a, 1])
    lilo.append([a+b, -1])

lilo.sort()

cnt = 0
# 0人の日数も格納する必要がある点に注意（ここでハマった）
# i=0を用意せず、cnt-1で入れていくと、途中の空白期間でanslist[-1]=anslist[n-1]に
# 0人の日数が加算されてしまう！
anslist = [0]*(n+1)

for i in range(len(lilo)-1):
    # 時点ログイン人数の加減算
    cnt += lilo[i][1]
    # 次のlogin/outまでの日数を求める
    day_diff = lilo[i+1][0] - lilo[i][0]
    # その日数の期間は、時点ログイン人数が続くので、これを答えの配列に加算
    anslist[cnt] += day_diff

print(*anslist[1:])