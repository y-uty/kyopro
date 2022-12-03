s = str(input())
a, b = map(int, input().split())

s_list = list(s)

s_a = s_list[a-1]
s_b = s_list[b-1]

s_list[a-1] = s_a
s_list[b-1] = s_b

s =  "".join(s_list)

print(s)