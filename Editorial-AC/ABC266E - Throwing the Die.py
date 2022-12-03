n = int(input())

# ゲームを続行するべきか終了するべきかの判断は、
# これまでどのような出目を出してきたかか関係無く、
# 直近の出目と、それに対して「この先に振れる回数と、その回数で期待できる出目」で決まる

# 従って、逆(N回目)から考えるのがよい
# 1回だけ振れるときの期待値は3.5なので、
# もし残りのターン数が1のとき、振り直すときの出目の期待値は3.5である
# ということは、直近の出目が3以下なら振り直した方がスコア更新を期待できるし、
# 4以上なら、振り直さない方がよいことが期待できる

# こうすると、あと2回だけ振れるときの期待値が求まる
# なぜなら、あと2回中1回目に振った出目が、先のシチュエーションで言う「直近の出目」であり、
# その出目に応じて最適な判断をした際の期待値が求まっているからである
# この流れで、あとN-1回だけ振れる時の期待値が求められる
# またその値は、1/6 * max(直近の出目,　あとi回振れるときの出目の期待値)となる


# 1回振るときの期待値
e = 3.5

# 残りi~N-1回振ることができるときの期待値を順に求めていく
for i in range(n-1):
    e_tmp = 0
    for j in range(1, 7):
        e_tmp += max(j, e)
    e_tmp /= 6
    
    e = e_tmp

print(e)
