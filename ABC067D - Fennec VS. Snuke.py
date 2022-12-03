def main():
    sys.setrecursionlimit(5*(10**5))
    N = int(input())
    T = collections.defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        T[a].append(b)
        T[b].append(a)

    # 自分の色で塗られた頂点を根とする部分木は、全て自分だけが塗ることのできる陣地として確定する
    # 自分の手番にちょうど1個必ず塗らなければならないから、
    # 全ての頂点がどちらかの陣地として確定した後の、陣地内の頂点数が、それぞれが塗れる数となる
    # これがフェネック過半数ならフェネックWin, そうでなければすぬけWinとなる

    # よって、両者は自分の手番に、より自陣を拡大するような塗り方をするのが最適
    # これは、1-Nを始点/終点とした最短パスを、互いに進んでいくことになる
    # この最短パスの長さをkとすると、フェネックが進めるのはk//2である
    # 従って、1からk//2進んだ頂点を根とする部分木のサイズがわかればよく、これをDFSで求めたのち、
    # 最短パスをBFSで求め、勝者を判定する

    subtr_size = [0]*(N+1)
    visited = [False]*(N+1)
    def dfs(v_from, cnt, l):
        visited[v_from] = True
        tmp = 1 # 部分木頂点数のカウント
        for v_to in T[v_from]:
            if not visited[v_to]:
                tmp += dfs(v_to, cnt, l) # 再帰を抜けるときに、自分より下の頂点数を足し合わせる
        subtr_size[v_from] = tmp
        return tmp

    dfs(N, 0, 0) # Nを根とした部分木のサイズをDFSで求める

    # 1 -> N へBFSして最短ステップ数ごとの部分木のサイズの最大値を求める
    visited = [-1]*(N+1)
    visited[1] = 0
    nx = collections.deque([1])
    dp = [0]*N # dp[i]:= 1からiステップでいける頂点の部分木サイズのMax
    while nx:
        v_from = nx.popleft()
        for v_to in T[v_from]:
            if visited[v_to] < 0:
                visited[v_to] = visited[v_from]+1
                dp[visited[v_to]] = max(dp[visited[v_to]], subtr_size[v_to])
                nx.append(v_to)
        if visited[N] >= 0: break # Nに到達したら打切

    # 1 -> N の最短パスを進めるだけ進んで得られる部分木のサイズが過半数なら先手の勝ち
    Fen_steps = visited[N]//2
    Fen_subtr = dp[Fen_steps]
    if Fen_subtr > N//2:
        print('Fennec')
    else:
        print('Snuke')


if __name__ == '__main__':
    import sys
    import collections
    import itertools
    import bisect
    import heapq
    import math
    import copy

    main()