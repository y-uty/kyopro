n, m = map(int, input().split())

st = []
for _ in range(n):
    ab = list(map(int, input().split()))
    st.append(ab)

cp = []
for _ in range(m):
    cd = list(map(int, input().split()))
    cp.append(cd)

ans_list = []
for i in range(n):
    tmp = 10**9
    ans = 0
    for j in range(m):
        d = abs(st[i][0] - cp[j][0]) +abs(st[i][1] - cp[j][1])
        if d < tmp:
            tmp = d
            ans = j+1

    ans_list.append(ans)

print(*ans_list, sep='\n')