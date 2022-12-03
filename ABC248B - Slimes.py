a, b, k = map(int ,input().split())

cnt = 0

while a<b:
    cnt += 1
    a = a * k

print(cnt)