n = int(input())

p = set()

for _ in range(n):
    num = set([int(input())])
    p ^= num # XOR:あるなら消す、ないなら入れる

print(len(p))