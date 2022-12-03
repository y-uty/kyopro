N = int(input())
flag = 0

for i in range(N//4 + 1):
    for j in range(N//7 + 1):
        if 4*i + 7*j == N:
            flag = 1

print('Yes') if flag else print('No')
