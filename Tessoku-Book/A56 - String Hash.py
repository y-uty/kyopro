import sys
n, q = map(int, input().split())
S = input()
lenS = len(S)
MOD = 2**61-1
B = 10007

# S[1, i]のハッシュHiを前計算
HashList = [0]
for i in range(lenS):
    Hi = (B * HashList[i] + ord(S[i]))%MOD
    HashList.append(Hi)

# Bの冪乗の前計算
BaseExp = [1]
Bexp = 1
for i in range(len(S)):
    Bexp = Bexp*B%MOD
    BaseExp.append(Bexp)

# S[l, r]のハッシュを求める
def GetHash_Substr(l, r):
    return (HashList[r] - BaseExp[r-(l-1)]*HashList[l-1])%MOD

for _ in range(q):
    a, b, c, d = map(int, sys.stdin.readline().split())
    if GetHash_Substr(a, b)==GetHash_Substr(c, d):
        print('Yes')
    else:
        print('No')