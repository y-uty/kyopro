def main():
    import sys
    import collections
    n = int(input())
    dai = []
    points = []
    for _ in range(n):
        x, y, p = map(int, sys.stdin.readline().split())
        points.append([x, y])
        dai.append(p)
    
    # あるSに対して条件を達成できるかは、始点iから全ての頂点を踏めるかどうかで決まる.
    # 点iからjへジャンプできる条件PiS >= D(距離)において、Pi, DはSに対して不変.
    # 従って、求めたいSの最小値S'より大きいTについて、PiT > PiS' >= Dが必ず成り立つ.
    # これらより、二分探索でその境界値S'を見つけられないかを考える.

    # そのためには、あるSに対して、全ての頂点に到達できるような始点があればよい.
    #  1. まず、点a -> 点bへジャンプできる(PiS >= Dである)ときにaからbへの有向辺を張ったグラフを作る.
    #  2. 次に、全ての点について、それを始点としたときに他の全ての頂点へ到達できるかをBFSなどで調べる.
    # これの成否を用いて、二分探索すればよい.
    # 計算量は1がO(N^2)、2がO(N^3)で、二分探索はO(log(max(D))) (D<=4*10^9)なので、間に合う.

    def is_ok(s):
        G = collections.defaultdict(list)

        # Sに対する有向グラフGの作成
        for i in range(n):
            p = dai[i]
            for j in range(n):
                if i==j: continue
                # 点iから点jへジャンプできるかをps>=dで判定し、できる場合は有向辺を張る
                d = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                if p*s >= d:
                    G[i].append(j)
    
        # Gの任意の頂点を始点として全頂点に到達できるかを探索
        for i in range(n):
            nx = collections.deque([i])
            seen = [0]*n 
            seen[i] = 0 
            cnt = 0

            while nx:
                v_from = nx.popleft()
                if seen[v_from]==0:
                    seen[v_from] = 1
                    cnt += 1
                    # 全頂点に到達した時点でOKを返して終了
                    if cnt==n: return True
                else:
                    # グラフが密になる可能性があるため移動元でもSkipを入れる
                    continue
                
                for v_to in G[v_from]:
                    if not seen[v_to]:                  
                        nx.append(v_to)

        return False

    # 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
    def bin_srch_mgr(ng, ok):
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid

        return ok

    # 二分探索の実行
    ans = bin_srch_mgr(-1, 4*(10**9))
    print(ans)


if __name__ == '__main__':
    main()