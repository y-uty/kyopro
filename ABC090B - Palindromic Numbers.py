a, b = map(int, input().split())
flag = 0
cnt = 0

for i in range(a, b+1):
    i_str = str(i)
    for j in range(len(i_str)//2):
        if i_str[j] != i_str[len(i_str)-1-j]:
            break
    else:
        cnt += 1

print(cnt)