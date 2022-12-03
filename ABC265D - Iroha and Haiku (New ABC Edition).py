import itertools
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
csum = [0] + list(itertools.accumulate(a))

left_ = 0
right_ = 1
x = False
while left_ < n and right_ <= n:
    tmp = csum[right_] - csum[left_]
    if tmp==p:
        x = True
        break
    elif tmp < p:
        right_ += 1
    else:
        left_ += 1

if not x:
    print('No')
    exit()

left_ = right_
right_ += 1
y = False
while left_ < n and right_ <= n:
    tmp = csum[right_] - csum[left_]
    if tmp==q:
        y = True
        break
    elif tmp < q:
        right_ += 1
    else:
        left_ += 1

if not y:
    print('No')
    exit()

left_ = right_
right_ += 1
z = False
while left_ < n and right_ <= n:
    tmp = csum[right_] - csum[left_]
    if tmp==r:
        z = True
        break
    elif tmp < r:
        right_ += 1
    else:
        left_ += 1

if not z:
    print('No')
else:
    print('Yes')