x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

v0 = (x2-x1, y2-y1)
v1 = (x3-x1, y3-y1)
v2 = (x4-x1, y4-y1)
ccw1 = (v0[0] * v1[1]) - (v0[1] * v1[0])
ccw2 = (v0[0] * v2[1]) - (v0[1] * v2[0])

if ccw1 * ccw2 < 0:
    print(1)
else:
    print(0)