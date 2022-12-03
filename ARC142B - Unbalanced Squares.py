n = int(input())
ans = []

# 近傍マスが奇数の場合、どのような配置でも条件を満たす
# グリッドの周囲マスがこれに該当する
# よって、2~N-1行目(の両端以外)のことだけを考える
# 8近傍があるとき、上の行が全部小さい、下の行が全部大きいを満たすとき
# 左右が両方とも自分より小さいまたは大きければ、条件を満たす
# 従って、まず各行については1~N, N+1~2N, ..., N*(N-1)~N^2とするのがよく
# 各行の小さい方半分、大きい方半分にわけて、左から交互に使ってその行を埋めていくことで
# 左右ともに小さい、左右ともに大きい、の繰り返しを作ることができる

num = 1
for i in range(n):
    if i in (0, n-1):
        ans_row = list(range(num, num+n))
        num += n
    else:
        ans_row = []
        num_range = list(range(num, num+n))
        for j in range(n):
            if j%2==0:
                ans_row.append(num_range[j//2])
            else:
                ans_row.append(num_range[-1-(j//2)])
        num += n

    ans.append(ans_row)

for i in range(n):
    print(*ans[i])