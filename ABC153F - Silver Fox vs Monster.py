import sys
import bisect
import math
N, D, A = map(int, input().split())
XH = []
for _ in range(N):
    x, h = map(int, sys.stdin.readline().split())
    XH.append([x, h])

# 左端から順番に倒していくのが最適

XH.sort()
XH.append([10**18+1, 0])
X, H = [], []
for x, h in XH:
    X.append(x)
    H.append(h)
damage_range = [0]*(N+1)
damage_tempsum = 0

ans = 0
for i in range(N):

    # 攻撃による与ダメージの累積を計算してから、手前での攻撃を先に処理
    damage_tempsum += damage_range[i]
    H[i] -= damage_tempsum

    # 手前までの攻撃で倒しきれているかどうかで分岐
    if H[i] <= 0:
        pass

    else:
        # X[L]のモンスターを倒し切るのに必要な最小回数の攻撃
        attack_count = math.ceil(H[i]/A)
        ans += attack_count

        # 2D先以下までダメージ -> 二分探索で見つける
        R = bisect.bisect_right(X, X[i]+2*D)
        damage_tempsum += attack_count*A
        damage_range[R] -= attack_count*A

print(ans)
