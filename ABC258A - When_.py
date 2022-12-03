k = int(input())

if k <= 9:
    ans = '21:0'+str(k)
elif k <= 59:
    ans = '21:'+str(k)
elif k <= 69:
    ans = '22:0'+str(k-60)
else:
    ans = '22:'+str(k-60)

print(ans)
