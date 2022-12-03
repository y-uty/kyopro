p = []
for _ in range(4):
    p.append(list(map(int, input().split())))

def cross_product(v1, v2, vo=(0, 0)):
    v1x, v1y = v1
    v2x, v2y = v2
    vox, voy = vo
    v1x, v2x = v1x-vox, v2x-vox
    v1y, v2y = v1y-voy, v2y-voy
    cross_prod = v1x*v2y - v1y*v2x
    # >0: ccw, <0: cw, =0:colinear
    return cross_prod
   
for i in range(4):
    # A -> B -> Cの順でみていく
    pa = p[i]
    pb = p[(i+1)%4]
    pc = p[(i+2)%4]

    # vBC × vBA が反時計回り
    if cross_product(pc, pa, pb) < 0:
        print('No')
        exit()
    
print('Yes')