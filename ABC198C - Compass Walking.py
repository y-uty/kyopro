R, X, Y = map(int, input().split())
import math
dist = math.sqrt(X**2 + Y**2)

if R > dist:
    print(2)
else:
    print(math.ceil(dist / R))