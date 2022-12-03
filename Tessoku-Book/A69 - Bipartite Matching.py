def main():
    N = int(input())

    # 「生徒(頂点1~N)」と「席(頂点N+1~2N)」の二部マッチングで解く
    # 入力を残余グラフを構築するためのedgesに変換
    edges = []
    for i in range(N):
        C = input()
        for j in range(N):
            if C[j]=='#':
                edges.append((i+1, j+N+1, 1))
    
    # s(頂点2N+1) -> 生徒, 席 -> t(頂点2N+2) への辺を張る
    for i in range(N):
        edges.append((2*N+1, i+1, 1))
        edges.append((i+N+1, 2*N+2, 1))


    # 答えを求めて出力
    ans = maxflow(2*N+2, 2*N+1, 2*N+2, edges) # 頂点数, 頂点s, 頂点t, edges
    print(ans)


# 最大フロー用の辺の構造体
class maxflow_edge:
	def __init__(self, to, cap, rev):
		self.to = to # 辺が向かう頂点
		self.cap = cap # 辺の容量
		self.rev = rev # 逆辺が頂点toの隣接リストの何番目にいるかのindex

# 深さ優先探索
def dfs(pos, goal, F, G, used):
	if pos == goal:
		return F # ゴールに到着：このフローを流せる
	# 探索する
	used[pos] = True
	for e in G[pos]:
		# 容量が 1 以上でかつ、まだ訪問していない頂点にのみ行く
		if e.cap > 0 and not used[e.to]:
			flow = dfs(e.to, goal, min(F, e.cap), G, used)
			# フローを流せる場合、残余グラフの容量を flow だけ増減させる
			if flow >= 1:
				e.cap -= flow 
                # 辺eのv_toの隣接リストのe.rev番目に、逆辺(元の辺のfromをe.toとするクラス)がいる
				G[e.to][e.rev].cap += flow
				return flow
	# すべての辺を探索しても見つからなかった
	return 0

#  頂点 s から頂点 t までの最大フローの総流量を返す（頂点数 N、辺のリスト edges）
def maxflow(N, s, t, edges):
	# 初期状態の残余グラフを構築
	G = [list() for i in range(N + 1)]
	for a, b, c in edges:
        # 逆辺が、相手側の隣接リストの何番目にいるかをe.revに持つ
		G[a].append(maxflow_edge(b, c, len(G[b])))
		G[b].append(maxflow_edge(a, 0, len(G[a])-1))
	INF = 10 ** 10
	total_flow = 0
	while True:
		used = [False] * (N+1)
		F = dfs(s, t, INF, G, used)
		if F > 0:
			total_flow += F
		else:
			break # フローを流せなくなったら、探索全体を終了してMaxFlowを返す
	return total_flow


if __name__=='__main__':
    main()
