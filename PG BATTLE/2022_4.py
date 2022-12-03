import itertools
import collections
N = int(input())
MOD = 998244353
ashi = []
miso = []

# 美味しさの合計
sum_ashi = 0
sum_miso = 0
for _ in range(N):
    a, b = map(int, input().split())
    a_tmp = []
    for i in range(11):       
        a_tmp.append(a*i)
    ashi.append(a_tmp)
    sum_ashi += a*10
    miso.append(b)
    sum_miso += b

sum_all = sum_ashi+sum_miso

if sum_all%2==1:
    print(0)
    exit()

# if sum_all==0:
#     tmp = 2**N
#     tmp2 = 1
#     for _ in range(10*N):
#         tmp2 *= 2
#         tmp2 %= MOD
#     ans = tmp*tmp2
#     print(ans%MOD)
#     exit()

ashiF = ashi[:N//2]
ashiL = ashi[N//2:]

print(ashiF, ashiL)

cnt_ashiF = collections.defaultdict(int)
cnt_ashiL = collections.defaultdict(int)

aF = itertools.product(*ashiF)
aL = itertools.product(*ashiL)

for f in aF:
    cnt_ashiF[sum(f)] += 1
for l in aL:
    cnt_ashiL[sum(l)] += 1


print(cnt_ashiF)
print(cnt_ashiL)

ans = 0
cnt = 0
# かにみそbit全探索(高橋君に分けるかにみそ)
for bits in itertools.product([True, False], repeat=len(miso)):
    # かにみその1つの選び方を生成
    cnt += 1
    choice = [x for x, b in zip(miso, bits) if b]
    print(choice, sum(choice))

    taka_oishisa = sum_all//2
    aoki_oishisa = sum_all//2

    taka_miso = sum(choice)
    aoki_miso = sum_miso - taka_miso
    # print(taka_miso, aoki_miso)

    # 高橋君に分ける合計の脚のおいしさはいくつか
    taka_ashi = sum_all//2 - taka_miso
    aoki_ashi = sum_all//2 - aoki_miso
    # print(taka_ashi, aoki_ashi)

    # 通り数
    for k, v in cnt_ashiF.items():
        tmp = taka_ashi-k
        ans += cnt_ashiL[tmp]*v
        ans %= MOD

print(ans, cnt)