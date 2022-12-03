N = int(input())
flag = 0

for i in range(9):
    for j in range(9):
        if (i+1)*(j+1) == N:
            flag = 1

print('Yes') if flag else print('No')