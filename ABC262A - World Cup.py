y = int(input())

if y%4==2:
    print(y)
elif y%4==0:
    print(y+2)
elif y%4==1:
    print(y+1)
else:
    print(y+3)