import collections
N = int(input())

cnt = collections.defaultdict(int)

if N==0:
    print(1)
    exit()

A, B = N//2, N//3
cnt[A] += 1
cnt[B] += 1
while True:
    kv = cnt.items()

    if len(kv)==1:
        break

    cnt = collections.defaultdict(int)
    for k, v in kv:
        if k==0:
            cnt[0] += v
        else:
            cnt[k//2] += v
            cnt[k//3] += v

print(cnt[0])


# memorized recursive method. (Python3 only)
# from functools import lru_cache
# N = int(input())
# @lru_cache
# def f(k):
#     if k==0:
#         return 1
#     else:
#         return f(k//2) + f(k//3)
# print(f(N))