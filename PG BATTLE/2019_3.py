import sys
N, M = map(int, input().split())

T = []
# レーンの先(ピンのある位置)に到達するのが早い順に処理する
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    T.append((a+b, i))

T.sort()

pins = [0]*M # 倒れたら1にする

for t, i in T:
    if i-t < 0 or i-t >= M:
        continue

    pins[i-t] |= 1

print(sum(pins))
