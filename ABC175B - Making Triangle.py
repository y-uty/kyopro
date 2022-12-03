N = int(input())
L = list(map(int, input().split()))

cnt = 0

# 三角形の成立条件 abs(b-c) < a < b+c
for a in L:
    for b in L:
        for c in L:
            if (a < b < c) and (abs(b-c) < a < b+c) and ( len(set([a,b,c])) == 3):
                cnt += 1

print(cnt)