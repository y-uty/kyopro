N = int(input())

oflow = 2**31

if (N >= oflow * (-1)) and (N < oflow):
    print('Yes')
else:
    print('No')