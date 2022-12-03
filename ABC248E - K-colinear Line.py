import collections
n, k = map(int, input().split())
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

if k==1:
    print('Infinity')
    exit()

ans = collections.defaultdict(int)

# 2点を決めると、その2点を通る直線は一意に定まる
# ある直線を定める2点のペアはN(N-1)/2個あるが、それぞれのペアについて、
# 他に何個の点がその直線に乗るかを各点について調べ、それがK個になるかを判定すればよい


for i in range(n-1):
    for j in range(i+1, n):
        # 点iと点jが定める直線に対して、
        tmpset = set([i, j])
        xi, yi = p[i]
        xj, yj = p[j]

        # 点aがその直線上にあるかを判定する
        for a in range(n):
            if a==i or a==j: continue

            xa, ya = p[a]

            # i->aベクトル(xa-xi, ya-yi)とi->jベクトル(xj-xi, yj-yi)の外積が0のとき、
            # 2つのベクトルがなす角は0, πであり、それは同一直線上となる
            if (xa-xi)*(yj-yi)==(ya-yi)*(xj-xi):
                tmpset.add(a)

        if len(tmpset) >= k:
            ans[tuple(list(sorted(tmpset)))] += 1

print(len(ans))
