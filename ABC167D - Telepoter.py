n, k = map(int, input().split())
a = list(map(int, input().split()))
# 町iに到達済か、到達済みなら何回目の移動かを管理
town = [-1]*n

d = 1
cnt = 0
# ループが発生するまで移動を続ける
while town[d-1] < 0:
    town[d-1] = cnt

    d = a[d-1]
    cnt += 1

    # ループする前にk回移動した場合は答えを出力して終了
    if cnt==k:
        print(d)
        exit()

# 1ループの周期を求めて、残りの移動回数の剰余を求める
cycle_ = cnt - town[d-1]
k = (k - cnt) % cycle_

# 余りの数だけ再度移動をシミュレートして終了
for _ in range(k):
    d = a[d-1]

print(d)