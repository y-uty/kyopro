n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

masu = [0]*(n+1)
koma = [0]*(k+1)

# マスとコマの初期状態
for i in range(k):
    masu[a[i]] = 1
    koma[i+1] = a[i]

# 移動のシミュレーション
for i in range(q):
    x = l[i]

    if koma[x] == n:
        continue

    else:
        if masu[koma[x]+1] == 0:
            masu[koma[x]], masu[koma[x]+1] =  masu[koma[x]+1], masu[koma[x]]
            koma[x] += 1

print(*koma[1:])
