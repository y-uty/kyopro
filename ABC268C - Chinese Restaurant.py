import collections


n = int(input())
p = list(map(int, input().split()))
p_to_idx = collections.defaultdict(int)
opcnt_to_num = collections.defaultdict(int)
for i in range(n):
    p_to_idx[p[i]] = i

for i in range(n):
    idx = p_to_idx[i] # 料理iがはじめどの人の前にあるか
    # print(i, idx)

    # (i-1)%N = i
    x = (i-1)%n
    opcnt_to_num[(x-idx+n)%n] += 1

    # i%N = i
    y = i%n
    opcnt_to_num[(y-idx+n)%n] += 1

    # (i+1)%N = i
    z = (i+1)%n
    opcnt_to_num[(z-idx+n)%n] += 1

print(max(opcnt_to_num.values()))