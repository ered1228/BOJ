x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

cross1 = ((x2 - x1)*(y4 - y1)) - ((y2 - y1)*(x4 - x1))
cross2 = ((x2 - x1)*(y3 - y1)) - ((y2 - y1)*(x3 - x1))
cross3 = ((x4 - x3)*(y2 - y3)) - ((y4 - y3)*(x2 - x3))
cross4 = ((x4 - x3)*(y1 - y3)) - ((y4 - y3)*(x1 - x3))

if cross1*cross2 < 0 and cross3*cross4 < 0:
    print(1)
elif cross1*cross2 == 0 and cross3*cross4 < 0:
    print(1)
elif cross1*cross2 < 0 and cross3*cross4 == 0:
    print(1)
elif cross1*cross2 == 0 and cross3*cross4 == 0:
    if max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2):
        print(1)
    else:
        print(0)
else:
    print(0)