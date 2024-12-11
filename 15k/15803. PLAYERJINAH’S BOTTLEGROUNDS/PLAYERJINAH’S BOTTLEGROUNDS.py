x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
v1 = (x2-x1, y2-y1)
v2 = (x3-x1, y3-y1)
if (v1[0]*v2[1]) - (v1[1]*v2[0]) == 0:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")