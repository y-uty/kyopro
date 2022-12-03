n, k = map(int, input().split())

if n==0:
    print(0)
    exit()

# xは10**5で割った余りで、それは0~10**5-1の10**5通りしかない
# xが同じ値になったら、以降はその周期を繰り返す
# よって、高々10**5のxの計算で、必ず周期に突入する(鳩ノ巣原理)
# 周期が検知できるようにxの値ごとの処理回数と、
# 検知後の残処理を周期を用いて一括処理するためのxの計算結果を順に記録しておく

steps = [0]*(10**5)
results = [-1]
x = n
cnt = 0
while True:
    str_y = str(x).zfill(5)
    y = 0    
    for s in str_y:
        y += int(s)
    x = (x+y)%(10**5)
    cnt += 1

    if cnt==k:
        print(x)
        exit()

    if steps[x] > 0:
        break
    else:
        steps[x] = cnt
        results.append(x)

# サイクル検出したら残りは周期で割って余りで処理
# 周期
t = cnt - steps[x]
# xの遷移のうち、サイクル部分のみを抽出
cycle_ = results[steps[x]:]
# k回からサイクル外の部分のカウントを引いて、周期で割る
rest = (k-(cnt-1))%t
# x遷移のサイクル部分の「余り番目」が答え
# ただし、余り0が末尾にくるのでインデックスに注意
print(cycle_[rest-1])
