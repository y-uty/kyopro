def main():
  N = int(input())
  A = list(map(int, input().split()))

  # 累積和(Bとする)に対する制約を満たすような操作を考える問題
  # 任意のi<jについて、B[i]を更新すると、その影響はすべてのB[j]に等しく及ぶ
  # 逆に、B[j]の更新は、どのB[i]にも影響しない
  # したがって、条件を満たすようなBを作るには、前から決めていく(具体的な最適な決め方は処理内で述べる)
  # Bを +, -, +, ... にするか、 -, +, -, ... にするかの両方を考え、それらのminが答え


  # +/-どちらから始めるかで累積和数列を2つ用意しておく
  # A[0] = 0 の場合、初めから調整が必要な点に注意
  B = [A[0]]
  for i in range(1, N): B.append(B[-1]+A[i])
  C = copy.deepcopy(B)

  if B[0]==0:
    B[0] = 1
    ansB, copeB = 1, 1
    C[0] = -1
    ansC, copeC = 1, -1

  elif B[0] > 0:
    ansB, copeB = 0, 0
    diff = -1-B[0]
    C[0] = -1
    ansC, copeC = abs(diff), diff

  else:
    ansB, copeB = 0, 0
    diff = 1-B[0]
    C[0] = 1
    ansC, copeC = abs(diff), diff


  def calc_ans(B, ans, cope):

    # 任意のi<jについて、B[i]を更新すると、その影響はすべてのB[j]に等しく及ぶことから、
    # B[i]を加減した場合、その累積調整量をもっておき、B[j]に反映させてから処理に入る
    for i in range(1, N):
      B[i] += cope

      # B[i]=0のとき、B[i-1]>0 => B[i]=-1, B[i-1]<0 => B[i]=1 とするのが最適
      if B[i]==0:
        if B[i-1] < 0:
          B[i] += 1
          cope += 1
          ans += 1
        else:
          B[i] -= 1
          cope -= 1
          ans += 1
      
      # B[i]!=0のとき、B[i-1]とB[i]の符号が異なるとき調整が必要
      # これも B[i-1]>0 => B[i]=-1, B[i-1]<0 => B[i]=1 とするのが最適で、
      # 差分を計算して、操作回数と累積調整量を加算する
      else:
        if B[i-1] > 0 and B[i] > 0:
          diff = -1-B[i]
          B[i] = -1
          cope += diff
          ans += abs(diff)

        elif B[i-1] < 0 and B[i] < 0:
          diff = 1-B[i]
          B[i] = 1
          cope += diff
          ans += abs(diff)
    
    return ans

  ans1 = calc_ans(B, ansB, copeB)
  ans2 = calc_ans(C, ansC, copeC)
  ans = min(ans1, ans2)

  print(ans)



if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator
  import copy

  main()