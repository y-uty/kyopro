a, b = map(int, input().split())

def make_divisors(n):
    lower_divisors , upper_divisors = set(), set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.add(i)
            if i != n // i:
                upper_divisors.add(n//i)
        i += 1
    return lower_divisors | upper_divisors

diva = set(make_divisors(a))
divb = set(make_divisors(b))
div = diva & divb

import collections
div_except = set()
div_list = sorted(list(div))
div_queue = collections.deque(div_list)
div_queue.popleft()

k = 0
while div_queue:
    d = div_queue.popleft()

    if d in div_except:
        k += 1
        continue
    for i in range(k+1, len(div_list)-1):
        if div_list[i+1]%d == 0:
            div_except.add(div_list[i+1])
    k += 1

print(len(div - div_except))