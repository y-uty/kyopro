def main():
    H, W = map(int, input().split())
    masu = []
    Teleport_pair = collections.defaultdict(list)
    for i in range(H):
        a = list(sys.stdin.readline().replace('\n', ''))
        masu.append(a)

    for i in range(H):
        for j in range(W):
            m = masu[i][j]
            if m=='S':
                Sr, Sc = i, j
            elif m=='G':
                Gr, Gc = i,j
            elif ord(m)>=97 and ord(m)<=122:
                Teleport_pair[m].append((i, j))

    # 全てがテレポート地点の場合、単純にBFSすると(HW)^2本程度の辺になってしまう
    # 2回以上同じテレポート地点を使って得することはないので、
    # 1回テレポートしたテレポート地点は、全て通常のマスに変える
    nx = collections.deque()
    nx.append((Sr, Sc))
    INF = H*W
    cost = [[INF]*W for _ in range(H)]
    cost[Sr][Sc] = 0
    vr = [0, 1, 0, -1]
    vc = [1, 0, -1, 0]

    while nx:
        r_from, c_from = nx.popleft()
        cost_from = cost[r_from][c_from]

        # テレポート
        if len(Teleport_pair[masu[r_from][c_from]]) > 0:
            for r_tele, c_tele in Teleport_pair[masu[r_from][c_from]]:
                masu[r_tele][c_tele] = '.'
                if r_tele==r_from and c_tele==c_from: continue
                if cost[r_tele][c_tele] > cost_from+1:
                    cost[r_tele][c_tele] = cost_from+1
                    nx.append((r_tele, c_tele))        

        # 隣のマスへ移動
        for i in range(4):
            dr, dc = vr[i], vc[i]
            r_to = r_from+dr
            c_to = c_from+dc
            if r_to>=0 and r_to<H and c_to>=0 and c_to<W:
                if masu[r_to][c_to]!='#':
                    if cost[r_to][c_to] > cost_from+1:
                        cost[r_to][c_to] = cost_from+1
                        nx.append((r_to, c_to))

    ans = cost[Gr][Gc]
    if ans==INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    import sys
    import collections

    main()