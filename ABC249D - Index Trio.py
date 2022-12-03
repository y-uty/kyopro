import collections
n = int(input())
a = list(map(int, input().split()))

# Aiの値と個数を辞書にしておき、重複排除した値を昇順ソートしておく
# Ai, Ajの二重ループでAiAj=Akとなるかを辞書に問い合わせてチェック
# パッと見でO(N^2)だが、AiAjがmax(A)を超えたら次のAiへ移る
# 最悪ケースでもN/1+N/2+...+N/N = NlogN回なので、間に合う

acnt = collections.Counter(a)
aset = sorted(list(acnt.keys()))
amax = aset[-1]
alen = len(aset)
ans = 0

for i in range(alen):
    ai = aset[i]

    for j in range(i, alen):
        aj = aset[j]
        ak = ai*aj
        if ak > amax:
            break # max(A)を超えたらありえない
        tmp = acnt[ak] # 仮のAk=AiAjがAに存在するか確認
        if tmp > 0:
            # AiとAjが同じ値かどうかで数え上げ方が異なるので注意
            if ai==aj: # (aiの個数)^2
                anstmp = (acnt[ai]**2)*tmp
            else: # (aiの個数)*(ajの個数)だが、i, jの入替もあるので*2
                anstmp = 2*(acnt[ai]*acnt[aj])*tmp
            ans += anstmp

print(ans)