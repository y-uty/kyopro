N, X = map(int, input().split())

M = [int(input()) for i in range(N)]

restX = X - sum(M)
add_d = restX // min(M)

print(N + add_d)