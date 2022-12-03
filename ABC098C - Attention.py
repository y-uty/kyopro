n = int(input())
s = str(input())

e_cnt = [0]*n
w_cnt = [0]*n

tmp = 0
for i in range(n):
    # W --> E 向き合ってる人数の累積和
    if s[i]=='W': tmp += 1
    e_cnt[i] = tmp

tmp = 0
for i in range(n):
    # W <-- E 向き合ってる人数の累積和
    if s[-1*i-1]=='E': tmp += 1
    w_cnt[-1*i-1] = tmp

ans = n

# 前方からの「同じ向きの人数」累積和 + 後方からの「逆向きの人数」の累積和
# 累積和を予め逆向きにとっているので、リーダ候補がどちら向きでも見るべき値は同じ
for i in range(n):
    if i==0:
        tmp = w_cnt[i+1] + 0
    elif i==n-1:
        tmp = 0 + e_cnt[i-1]
    else:
        tmp = w_cnt[i+1] + e_cnt[i-1]
    if tmp < ans:
        ans = tmp

print(ans)