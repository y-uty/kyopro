N = int(input())
A = list(map(int, input().split()))
maxA = max(A)

sv = [0]*(maxA+1)
for i in range(N): sv[A[i]] += 1

# 小さいAiから順に、Aiの倍数のカウンタを上げていく
# これの結果一度もカウンタが上がらなかったものが、
# 自身以外のAiで割り切れない数である
for i in range(1, maxA+1):
    if sv[i] >= 1:
        j = i+i
        while j <= maxA:
            sv[j] += 1
            j += i

ans = 0
for i in range(N):
    if sv[A[i]]==1:
        ans += 1

print(ans)