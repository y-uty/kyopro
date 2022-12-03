n, x, m = map(int, input().split())

# mod Mでは 0<=Ai<M であるから、A_M+1までに必ず同じ値となる(鳩の巣原理)
# 同じ値を取ったあとは、その周期を繰り返す
# 従って、登場済みのAiの値と、それが何項めかを記録していき、
# 繰り返しを検出したら、残りの個数を周期で割った商をp, 余りをqとしたとき
# p*周期内総和 + 周期のはじめから余りからq項までの和　を求めることでO(M)となる

remainders = [-1]*m
anslist = []
cnt = 0
ans = x

while True:
    x *= x
    x %= m
    if remainders[x]>=0:
        # 繰り返しを検出した
        ans += sum(anslist)
        break
    else:
        # N<=Mの場合、繰り返すことなく終わる可能性がある
        remainders[x] = cnt
        anslist.append(x)
        cnt += 1    
        if cnt==n-1:
            ans += sum(anslist)
            print(ans)
            exit()

# 繰り返し検出後の処理
# 1サイクルの配列と長さ
cycle_list = anslist[remainders[x]:]
cycle_len = len(cycle_list)
# 残項数を周期で割った商pと余りq
cnt_rest = n-1-cnt
p, q = divmod(cnt_rest, cycle_len)
# p*周期内総和 + 周期のはじめから余りからq項までの和 を答えに加算
ans += p*sum(cycle_list)
ans += sum(cycle_list[:q])

print(ans)
