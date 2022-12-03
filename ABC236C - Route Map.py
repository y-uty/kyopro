S_cnt, T_cnt = map(int, input().split())
S = [str(i) for i in input().split()]
T = [str(j) for j in input().split()]

s_num = 0
t_num = 0

for _ in range(len(S)):
    if S[s_num] == T[t_num]:
        print('Yes')
        s_num += 1
        t_num += 1
    else:
        print('No')
        s_num += 1
