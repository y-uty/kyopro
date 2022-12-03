n = int(input())
sets = set()
sets_1 = set()

for i in range(n):
    s = str(input())
    sets.add(s)
    sets_1.add('!' + s)

sets_its = sets & sets_1

if len(sets_its) > 0:
    print(sets_its.pop().replace('!', ''))
else:
    print('satisfiable')
