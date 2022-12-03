n, k = map(int, input().split())

ans = 0
m = n+1
MOD = 10**9+7

# 0~nをk個選んだ総和が取りうる数は、
# sum(0,1,..,k)以上、sum(n-k+1,..,n-1,n)以下のすべての整数
for i in range(k, m+1):
    x = i-1
    min_ = x*(x+1)//2 # sum(0,1,..,k)
    max_ = (n+n-i+1)*i//2 # sum(n-k+1,..,n-1,n)
    ans += (max_ - min_ + 1) % MOD

print(ans%MOD)