x, y, a, b, c = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)[:x] # 美味しい順の赤いりんごx個
q = sorted(list(map(int, input().split())), reverse=True)[:y] # 美味しい順の緑のりんごy個
rg = sorted(p+q)
tp = sorted(list(map(int, input().split())), reverse=True)

num = x+y
ans = sum(rg)
rg_tmp = ans
tp_tmp = 0
# 透明なりんごを、美味しい順にi個食べるとき、
# 残りのx+y-i個は、美味しい順x個の赤りんごとy個の緑りんごから貪欲に選ぶ
for i in range(min(num, c)): 
    rg_tmp -= rg[i]
    tp_tmp += tp[i]

    if rg_tmp+tp_tmp > ans:
        ans = rg_tmp+tp_tmp

print(ans)