n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    if b in set(A):
        pass
    else:
        print('No')
        exit()
    
    A.remove(b)

print('Yes')
