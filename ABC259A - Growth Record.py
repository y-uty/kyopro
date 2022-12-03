n,m,x,t,d = map(int, input().split())

y = max([x-m, 0])
gr = y*d

print(t-gr)