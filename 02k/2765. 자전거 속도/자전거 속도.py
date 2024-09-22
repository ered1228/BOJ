import math
i = 0

while True:
    r, c, t = map(float, input().split())
    if c == 0:
        break
    else:
        i += 1
        temp = 1 / 63360
        r /= 2
        r *= temp
        l = 2*math.pi*r
        dist = l*c
        hour = 3600 / t
        mph = hour * dist
        print(f"Trip #{i}: {dist:.2f} {mph:.2f}")