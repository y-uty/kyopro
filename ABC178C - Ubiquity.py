n = int(input())
MOD = 10**9 + 7

ans = 10**n - (9**n * 2 - 8**n)

print(ans%MOD)