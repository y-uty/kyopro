from signal import siginterrupt

N = int(input())
sum_ab = []

for i in range(N-1):
    a = i+1
    b = N-a
    sum_a = sum([int(j) for j in str(a)])
    sum_b = sum([int(j) for j in str(b)])
    sum_ab.append(sum_a + sum_b)

print(min(sum_ab))