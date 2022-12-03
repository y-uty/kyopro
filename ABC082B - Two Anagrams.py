s = str(input())
t = str(input())

s_sorted = ''.join(sorted(s))
t_sorted = ''.join(sorted(t, reverse=True))

if(s_sorted < t_sorted):
    print('Yes')
else:
    print('No')
