N = int(input())
S = input()
T = input()
if int(S) > int(T): S, T = T, S
S = list(S)
T = list(T)

hamdist = 0
# SとTで0/1が異なる場所の個数を数える
for i in range(N):
    if S[i]!=T[i]:
        hamdist += 1

# 奇数の場合、達成不可能
if hamdist%2:
    print(-1)
    exit()

# S, Tを割り当てるのは半分ずつ
# それぞれ割り当てられる限り、0の方を優先する
numS = hamdist//2
numT = hamdist//2
ans = []
for i in range(N):
    if S[i]!=T[i]:

        if S[i]=='0':
            if numS > 0:
                ans.append(S[i]) # 0
                numS -= 1
            else:
                ans.append(T[i]) # 1
                numT -= 1

        elif T[i]=='0':
            if numT > 0:
                ans.append(T[i]) # 0
                numT -= 1
            else:
                ans.append(S[i]) # 1
                numS -= 1

    else:
        ans.append('0')

print(''.join(ans))