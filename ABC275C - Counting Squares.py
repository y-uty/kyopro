import itertools
import collections
masu = []
for _ in range(9):
    s = list(input())
    masu.append(s)

ans = 0
p = []
# 81C4をすべてためす
for i in range(9):
    for j in range(9):
        if masu[i][j]=='#':
            p.append((i, j))

# 座標ベクトルを与えて外積を得る. 引数3は始点座標が原点でないとき用
def cross_product(v1, v2, vo=(0, 0)):
    v1x, v1y = v1
    v2x, v2y = v2
    vox, voy = vo
    v1x, v2x = v1x-vox, v2x-vox
    v1y, v2y = v1y-voy, v2y-voy
    cross_prod = v1x*v2y - v1y*v2x
    # >0: ccw, <0: cw, =0:colinear
    return cross_prod

points4 = itertools.combinations(p, 4)
# どの3つも同一直線上になく、4つの距離がすべて同じであれば正方形
for p4 in points4:
    a,b,c,d = p4

    cp_a_bc = cross_product(b, c, a)
    cp_c_ad = cross_product(a, d, c)
    cp_d_cb = cross_product(c, b, d)
    cp_b_ad = cross_product(a, d, b)
    if cp_a_bc==0: continue
    if cp_c_ad==0: continue
    if cp_d_cb==0: continue
    if cp_b_ad==0: continue

    ar, ac = a
    br, bc = b
    cr, cc = c
    dr, dc = d

    d_ab = (ar-br)**2 + (ac-bc)**2
    d_ac = (ar-cr)**2 + (ac-cc)**2
    d_ad = (ar-dr)**2 + (ac-dc)**2

    d_bc = (br-cr)**2 + (bc-cc)**2
    d_bd = (br-dr)**2 + (bc-dc)**2

    d_cd = (cr-dr)**2 + (cc-dc)**2

    d_cnt = collections.defaultdict(int)
    d_cnt[d_ab] += 1
    d_cnt[d_ac] += 1
    d_cnt[d_ad] += 1
    d_cnt[d_bc] += 1
    d_cnt[d_bd] += 1
    d_cnt[d_cd] += 1

    p4, p2 = False, False
    for k, v in d_cnt.items():
        if v==4:
            p4 = True
        if v==2:
            p2 = True

    if p4 and p2: ans += 1

print(ans)
