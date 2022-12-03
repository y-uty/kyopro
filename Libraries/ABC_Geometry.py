# 座標ベクトルを与えて外積を得る. 引数3は始点座標が原点でないとき用
def cross_product(v1, v2, vo=(0, 0)):
    v1x, v1y = v1
    v2x, v2y = v2
    vox, voy = vo
    v1x, v2x = v1x-vox, v2x-vox
    v1y, v2y = v1y-voy, v2y-voy
    cross_prod = v1x*v2y - v1y*v2x
    # >0: ccw, <0: cw, =0:colinear
    return cross_prod

# 2次元平面座標をθ(ラジアン)回転
import math
def coordinate_rotate(vrot, theta, vo=(0, 0), mode='r'):
    if mode=='d': theta = math.radians(theta)
    px, py = vrot
    ox, oy = vo
    px, py = px-ox, py-oy
    # 中心となる座標周りにp0を回転
    rotated_x = math.cos(theta)*px - math.sin(theta)*py
    rotated_y = math.sin(theta)*px + math.cos(theta)*py
    return rotated_x, rotated_y

