n, x = map(int, input().split())
a = list(map(int, input().split()))

sum_pair = []
for i in range(1, n):
    sum_pair.append(a[i]+a[i-1])

ans = 0
for i in range(len(sum_pair)-1): # sum_pairの要素ごとに処理
    # ペア和がxになるまで、箱の中身が0になるまで、どちらか小さい方まで処理できる
    # loopでシミュレーションするとTLEするので、minで一気に計算する
    # ペア和が既にx以下の場合、minが負になるので、0とmaxとってケア
    k = min([max([sum_pair[i]-x, 0]), a[i+1]])
    a[i+1] -= k
    sum_pair[i] -= k
    sum_pair[i+1] -= k
    ans += k

# 両端が残った場合、個別に食べるしかなし
if sum_pair[0] > x:
    ans += sum_pair[0] - x
    sum_pair[0] = x

if sum_pair[-1] > x:
    ans += sum_pair[-1] - x
    sum_pair[-1] = x

print(ans)