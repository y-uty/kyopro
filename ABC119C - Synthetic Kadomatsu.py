import itertools
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = 10**9

# 最適な魔法の使い方がわかっているとき、それらを使う順番は関係無い
# 合成魔法の使い方が難しいので、どう合成するかは決めうちして全探索できないかを考える
# ⇒各竹について、A, B, Cに使う, 使わないの4択があり、これを全探索する
#   最大で 4^8 = 65536

# ビット全探索の要領で各竹をどう使うかの組み合わせを得る
cand = range(N)
for K in itertools.product([0,1,2,3], repeat=len(cand)):

  # A, B, Cに何本使うか、合成魔法だけを使った時点での長さはいくつかを求める
  init_len = [0]*4
  use_count = [0]*4
  for i in range(N):
    init_len[K[i]] += L[i]
    use_count[K[i]] += 1
  
  a, b, c = init_len[0], init_len[1], init_len[2]
  # A, B, Cいずれかに少なくとも1つ竹が使われている場合のみ
  if a > 0 and b > 0 and c > 0:
    tmp_a = abs(A-a) + (use_count[0]-1)*10
    tmp_b = abs(B-b) + (use_count[1]-1)*10
    tmp_c = abs(C-c) + (use_count[2]-1)*10
    ans = min(ans, tmp_a+tmp_b+tmp_c)

print(ans)