N = int(input())
A = [int(a) for a in input().split()]

A.sort()

print(abs(A[0] - A[-1]))