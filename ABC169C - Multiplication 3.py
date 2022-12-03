a, b = map(str, input().split())

a = int(a)
b = int(b[:len(b)-3] + b[-2:])

print(a * b // 100)