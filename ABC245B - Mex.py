N = int(input())
A = list(map(int, input().split()))

for i in range(2001):
    if i in set(A):
        pass
    else:
        print(i)
        exit()
