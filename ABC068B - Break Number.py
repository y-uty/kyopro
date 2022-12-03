N = int(input())

for i in range(100):
    if 2**i > N:
        print(2**(i-1))
        break