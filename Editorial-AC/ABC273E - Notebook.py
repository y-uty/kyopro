import sys
import collections
# AをTrie木で表現し、ADD/DELETEで子を増やして移動する/親に戻ることで
# Aの末尾は現在地の頂点に書かれた整数となる

# 頂点iに書かれた数字を管理するlist[i]
Anode = [-1]

# 頂点iの親頂点の番号を管理するdict[i]
parents = collections.defaultdict(int)

# SAVE/LOAD用: そのページに記録したAの末尾、つまり記録したときにいた頂点の番号(から整数をlist[i]で調べる)
pages = collections.defaultdict(int)

ans, pos = [], 0

q = int(input())
for _ in range(q):
    qry = list(map(str, sys.stdin.readline().split()))
    t = qry[0]

    if t=='ADD': # 子を増やしつつそこへ移動
        x = int(qry[1])
        parents[len(Anode)] = pos
        Anode.append(x)
        pos = len(Anode)-1

    elif t=='DELETE': # 親へ移動(-1にいるときは何もしない)
        if pos>0: pos = parents[pos]
    
    elif t=='SAVE': # ページyに現在地の頂点番号を記録
        y = int(qry[1])
        pages[y] = pos

    else: # 'LOAD': # ページzに記録された頂点番号へ移動
        z = int(qry[1])
        pos = pages[z] # ページzが空でも0を返して-1に戻るのでOK
    
    ans.append(Anode[pos]) # 現在地の整数がAの末尾

print(*ans)

