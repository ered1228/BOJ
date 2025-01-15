import math

while True:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        v1 = (x2-x1, y2-y1)
        v2 = (x3-x1, y3-y1)
        v3 = (x3-x2, y3-y2)
        theta = math.acos((v1[0]*v2[0] + v1[1]*v2[1]) / (math.sqrt(v1[0]**2 + v1[1]**2) * math.sqrt(v2[0]**2 + v2[1]**2)))
        r = math.sqrt(v3[0]**2 + v3[1]**2) / (math.sin(theta)*2)
        print("{:.2f}".format(2*math.pi*r))
    except:
        break