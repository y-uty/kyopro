a,b,c,d,e,f,x = map(int, input().split())

d_taka, m_taka = divmod(x, (a+c))
if m_taka >= a:
    taka = a*b*d_taka + a*b
else:
    taka = a*b*d_taka + m_taka*b

d_aoki, m_aoki = divmod(x, (d+f))
if m_aoki >= d:
    aoki = d*e*d_aoki + d*e
else:
    aoki = d*e*d_aoki + m_aoki*e

if taka>aoki:
    print('Takahashi')
elif taka<aoki:
    print('Aoki')
else:
    print('Draw')