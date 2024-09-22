def absolute(x):
    if x > 0:
        x = -x
    return abs(x)

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (((x1-x2)**2) + ((y1-y2)**2))**(1/2)
    if (d == 0) and (r1 == r2):
        result = -1
    else:
        if d > (r1+r2):
            result = 0
        elif d == (r1+r2):
            result = 1
        elif (d < (r1+r2)) and (d > abs(r1-r2)):
            result = 2
        elif d == abs(r1-r2):
            result = 1
        elif d < abs(r1-r2):
            result = 0
    print(result)