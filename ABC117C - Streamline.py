n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

if n > m: n=m
diff_x = [abs(x[i+1]-x[i]) for i in range(m-1)]
diff_x.sort()

print(sum(diff_x[:len(diff_x)-(n-1)]))