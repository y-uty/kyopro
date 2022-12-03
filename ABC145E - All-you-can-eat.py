def main():
  N, T = map(int, input().split())
  dish = []
  for _ in range(N):
    A, B = map(int, input().split())
    dish.append((A, B))
  
  # ・最後の注文以外は、どのような順番で注文してもよい
  # ・最後の注文は、注文する中で最も時間がかかる(Aiが最大)のものにするのがよい
  # 　-> 選ぶ注文の中でAi最大のものを選んだときに、食べ終わる時刻がT以降になるようにナップサックできればよい
  # これは、料理を予めAiの昇順でソートしておくことで、「料理iを選んで時刻j+Aiに遷移してT以上になる」とき、
  # k=1~i-1について必ずAk <= Aiとなるため実現できる
  # (DPの遷移の中で、dp[i][j]となるk=1~i-1の選び方はわからなくなっているが、どれを選んでもAk<=Aiが保証されている
  #  言い換えると、(Aiの昇順となった)料理iまで時刻j>=Tとなった時点で、それ以上注文されることを考えなくてよい)

  dish.sort()
  
  dp = [[-1]*(T+1) for _ in range(N+1)]
  dp[0][0] = 0

  for i in range(N):
    a, b = dish[i]

    for j in range(T+1):
      if dp[i][j] >= 0:

        if j < T:
          # 時刻jに料理iを注文して食べ始める
          # 食べ終わる時刻がT以降になったら、それ以上は注文できない
          next_j = min(j+a, T)
          dp[i+1][next_j] = max(dp[i+1][next_j], dp[i][j]+b)

        # 料理iを食べない
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

  print(max(dp[N]))


if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator

  main()