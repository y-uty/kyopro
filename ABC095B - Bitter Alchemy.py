N = int(input())
X = int(input())
M = [int(input()) for i in range(N)]

restX = X - sum(M)
add_d = restX // min(X)

print(N + add_d)