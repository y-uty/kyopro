import sys
n = int(input())

# |Ai-x|の総和を最小にするようなxは、Aiの中央値
# マンハッタン距離はx,y座標を独立に考えてよいことを考えると、
# |Xi-px|の総和を最小にするようなpx, |Yi-py|の総和を最小にするようなpyを
# それぞれ独立に考えればよく、これは前述の通り中央値を求めれば良い

px = []
py = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    px.append(x)
    py.append(y)

px.sort()
py.sort()
x_med = px[n//2]
y_med = py[n//2]

ans = 0
for i in range(n):
    ans += abs(px[i]-x_med)
    ans += abs(py[i]-y_med)

print(ans)