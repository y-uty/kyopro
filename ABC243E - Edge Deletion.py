import collections
N, M = map(int, input().split())

edges = collections.defaultdict(int)
INF = 10**15
dp = [[INF]*N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    edges[(A, B)] = C # A < B
    dp[A][B] = C
    dp[B][A] = C

# i-jを結ぶ辺を削除できるのは、隣接し合う(i, jを含まない)頂点集合Sに対して、
# dist(i-S-j) <= dist(i-j) となるとき(コストが同じでも消せる)

# 制約が小さいので全点対最短経路はワーシャルフロイドで簡単に求められる
# 2点間の最短経路を記録するための配列について、辺がある2点間のみそのコストを入れるが、
# 全点を更新しきるまでのどこかで一度でもそれ以下となる更新がされる
# すなわち、i-jに辺があるとして dp[i][j] >= dp[i][k] + [k][j] となるkが1つでもあれば、
# 最短路としてi-k-jを通る(同じコストで通れる)ことになるため、i-jを結ぶ辺は削除できることとなる

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][k]!=INF and dp[k][j]!=INF:

                # i-j間の最短経路更新
                if dp[i][j] >= dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    # i, jの組に対してi-jを結ぶ辺があるか1度だけ(重複せず)判定する必要があるが、
                    # 辺をi < jとして記録したのでそのまま連想配列を調べても問題ない
                    if edges[(i, j)] > 0:
                        ans += 1
                        # 処理中にi-j間を複数回更新する可能性があるので、
                        # 1度更新したら連想配列の値を0で更新しておく
                        edges[(i, j)] = 0

print(ans)