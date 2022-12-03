n = int(input())
t, a = 1, 1

dp = [(0, 0)]
for i in range(n):
    t, a = map(int, input().split())

    # 二分探索
    # ある時点の比がT:Aのとき、T, Aが互いに素であることから、
    # それぞれの得票数がTx, Axとなるxが存在す
    # 得票数が減ることはないから、Tx, Axともに直前の得票数以上となる最小のxを求めると、
    # N回目まで順次求まっていく
    # なお、1回目は必ずx=1, すなわち得票数はT, Aからスタートする

    ok, ng  = 10**18, 0
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if t*mid >= dp[-1][0] and a*mid >= dp[-1][1]:
            ok = mid
        else:
            ng = mid
    
    dp.append((t*ok, a*ok))

    # AC後追記
    # (現在の比率)*x >= (直前の得票数)より、
    # 最小のx は max( ceil( (現在の比率) / (直前の得票数)) )_(高橋, 青木) によりO(1)でわかる

print(sum(dp[-1]))