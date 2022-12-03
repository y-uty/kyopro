import collections
n = int(input())

# n以下の自然数を、平方数で割った数を求める
# 割り切れない場合はそのまま
# 結果が同じである数字2つを選ぶと平方数が作れる

# 同じ数を複数の平方数で更新するので、参照用と格納用は別にする
num = [i for i in range(n+1)]
sv = [i for i in range(n+1)]

i = 2
while i*i <=n: # n以下の平方数について
    j = i*i
    while j <= n: # 平方数の倍数を順にみていく
        d, m = divmod(num[j], i*i)
        if m==0: # 割り切れるときだけ商を記録する
            sv[j] = d
        j += i*i # 次の倍数へ
    i += 1 # 次の平方数へ

# 結果が同じものから2つ選ぶので、それぞれの数の2乗の和が答え
cnt = collections.Counter(sv[1:]).values()
ans = 0
for c in cnt: ans += c**2
print(ans)
