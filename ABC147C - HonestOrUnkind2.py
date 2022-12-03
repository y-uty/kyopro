import itertools
n = int(input())
t = []
for _ in range(n):
    a = int(input())
    ti = []
    for _ in range(a):
        x, y = map(int, input().split())
        ti.append((x, y))
    t.append(ti)

# N <= 15 より、正直者の人を選んだbit全探索を行う
# 正直者として選んだ人の証言が、正直者として選んだ人たちと矛盾しなければOK
# 矛盾しない選び方の正直者の人数のうち最大が答え

# bit全探索
cand = list(range(1, n+1)) # 選ぶ候補のリスト
ans = 0
for bits in itertools.product([True, False], repeat=len(cand)):
    # 1つの選び方を生成
    choice = [x for x, b in zip(cand, bits) if b]

    res = True # いまの正直者の選び方全体に対する真偽判定

    # 正直者として選んだ人の証言を1人ずつ検証する
    for c in choice:
        tc = t[c-1]

        # ある正直者(仮)の証言が、いまの正直者の選択と1つも矛盾しないかを確認
        for p, hu in tc: # hu: 0-不親切, 1-正直者
            if hu==0:
                # 人cの証言「人pが不親切である」について、
                # 今選んだ正直者のリストに人pが含まれていてはならない
                if p in choice:
                    res = False
            
            else:
                # 人cの証言「人pが正直者である」について、
                # 今選んだ正直者のリストに人pが含まれていなければならない
                if p not in choice:
                    res = False

        if not res: # 1人でも証言が矛盾すれば、ただちに全体として偽である
            break
    
    if res:
        ans = max(ans, len(choice))

print(ans)