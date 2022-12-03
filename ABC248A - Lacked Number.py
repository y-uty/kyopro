s = str(input())

s = set(list(s))
num = set(list('0123456789'))

print(list(num - s)[0])