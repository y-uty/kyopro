x = input()

y = int(x[-3])
z = int(x[:-4])
if y >= 5:
    print(z+1)
else:
    print(z)
