import math
a, b, k = map(int, input().split())
ans = ''

for i in range(a+b):
    # i文字目にaを置いたとき、残りのa,bで何通りの文字列が作れるか？
    comb_when_chosen_a = math.comb(a-1+b, b)

    # k以上のとき、aを置いた文字列の中にk番目があるので、aを置く.
    if comb_when_chosen_a >= k:
        ans += 'a'
        a -= 1
    # k未満のとき、aを置いた文字列の中にk番目はない.
    # 従って、aを置けないならbを置く. 
    else:
        ans += 'b'
        b -= 1
        # aを置いて作れる数ぶんを飛ばしたので、比較に使うkもその分減算することに注意.
        k -= comb_when_chosen_a

print(ans)