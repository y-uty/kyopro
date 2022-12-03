n, k = map(int, input().split())
d = []

while n > 0:
    n, n_mod = divmod(n, k)
    d.append(n_mod)

print(len(d))
