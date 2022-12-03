H, W, N, h, w = map(int, input().split())

masu = [[[0]*W for _ in range(H)] for _ in range(N+1)] # 整数ごとに、そのマスに登場するなら1, 登場しないなら0で、後から累積和をとる
setnum = set()
for i in range(H):
    a = list(map(int, input().split()))
    for j in range(W):
      masu[a[j]][i][j] = 1
      setnum.add(a[j])

for x in range(1, N+1):
  for i in range(H):
      for j in range(W-1):
          masu[x][i][j+1] += masu[x][i][j]

  for j in range(W):
      for i in range(H-1):
          masu[x][i+1][j] += masu[x][i][j]


ans = [[0]*(W-w+1) for _ in range(H-h+1)]
for x in range(1, N+1):
  for i in range(H-h+1):
    for j in range(W-w+1):
        
        # 左上
        a, b = i, j
        # 右下
        c, d = i+h-1, j+w-1

        cnt = masu[x][c][d]
        if a > 0:
            cnt -= masu[x][a-1][d] 
        if b > 0:
            cnt -= masu[x][c][b-1]
        if a > 0 and b > 0:
            cnt += masu[x][a-1][b-1]

        if masu[x][-1][-1] - cnt > 0:
          ans[i][j] += 1

for i in range(H-h+1):
  print(*ans[i])
