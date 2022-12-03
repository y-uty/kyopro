import itertools
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
m = int(input())
# たすきの受け渡しができないa,bをreput[a][b]=Falseと表現する2次元配列を作る
# これにより、のちの受け渡し可否判定が1ペアあたりO(1)となる
reput = [[False]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    reput[x-1][y-1] = True
    reput[y-1][x-1] = True

# N!<=3628800通りを全探索 全体計算量はO(N!*N)
runners = list(itertools.permutations(range(1, n+1)))
ans = 10**9
for r in runners:
    tmp = 0
    # i, i+1人目がたすきを受け渡せない場合、この順列はNG
    for i in range(n-1):
        if reput[r[i]-1][r[i+1]-1]:
            break   
        tmp += a[r[i]-1][i]  
    else:
        # 全員受け渡し可能なら、最後の1人を加算し忘れないように
        tmp += a[r[-1]-1][-1]
        if tmp < ans: ans = tmp

if ans < 10**9:
    print(ans)
else:
    print(-1)
