N = int(input())

sv = [1]*(N+1)
ans = 1
for i in range(2, N+1):
    j = i
    while j <= N:
        sv[j] += 1
        j += i

    ans += i*sv[i]
print(ans)