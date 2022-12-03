N = int(input())
import collections
A = collections.defaultdict(int)
B = collections.defaultdict(int)
for i in range(50):
    A[i+1] = 3**(i+1)
for i in range(30):
    B[i+1] = 5**(i+1)

for a, v in A.items():
    for b, w in B.items():
        if v+w== N:
            print(str(a) + ' ' + str(b))
            exit()

print(-1)