a, b, w = map(int, input().split())
w *= 1000

min_ = 0
max_ = 0

for i in range(1, w+2): # max of w = 10^6
    if w / i <= b:
        if w / i >= a:
            if min_ == 0:
                min_ = i
        else:
            if min_ == 0:
                print('UNSATISFIABLE')
                exit()

            if max_ == 0:
                max_ = i-1
    
    if min_ * max_ > 0:
        break

print(min_, max_)