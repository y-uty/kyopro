def main():
  N = int(input())
  Ax, Ay = map(int, input().split())
  Ax -= 1
  Ay -= 1
  Bx, By = map(int, input().split())
  Bx -= 1
  By -= 1
  masu = [list(sys.stdin.readline().replace('\n', '')) for _ in range(N)]

  # 右下、右上、左上、左下
  vx = [1, -1, -1, 1]
  vy = [1, 1, -1, -1]

  # 01-BFS 0:同じ方向に進む 1:それ以外
  nx = collections.deque()
  nx.append((Ax, Ay, -1))
  INF = 10**9
  # (x座標, y座標, 直前に進んだ方向)
  cost = [[[INF]*N for _ in range(N)] for _ in range(4)]
  for i in range(4): cost[i][Ax][Ay] = 0
  fixed = [[[False]*N for _ in range(N)] for _ in range(4)]

  # 要領はDijkstraと同じ. コスト0が先, 1が後でdequeを使う
  while nx:
    x_from, y_from, dir_from = nx.popleft()

    if dir_from==-1: # 初手だけ注意
      for i in range(4): fixed[i][x_from][y_from] = True
    elif fixed[dir_from][x_from][y_from]:
      continue

    fixed[dir_from][x_from][y_from] = True
    c_from = cost[dir_from][x_from][y_from]

    # 4方向へ
    for dir_to in range(4):
      dx, dy = vx[dir_to], vy[dir_to]
      x_to = x_from + dx
      y_to = y_from + dy

      if x_to < 0 or x_to >= N or y_to < 0 or y_to >= N or masu[x_to][y_to]=='#':
        continue

      if dir_from==dir_to: # 同じ方向にはコスト0で進む
        if cost[dir_to][x_to][y_to] > c_from:
          cost[dir_to][x_to][y_to] = c_from
          nx.appendleft((x_to, y_to, dir_to)) # 先
      else: # 異なる方向にはコスト1で進む
        if cost[dir_to][x_to][y_to] > c_from + 1:
          cost[dir_to][x_to][y_to] = c_from + 1
          nx.append((x_to, y_to, dir_to)) # 後


  ans = INF
  for i in range(4): ans = min(ans, cost[i][Bx][By])
  if ans==INF:
    print(-1)
  else:
    print(ans)


if __name__=='__main__':
  import sys
  import collections

  main()