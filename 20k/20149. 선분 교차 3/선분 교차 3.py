x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

cross1 = ((x2 - x1)*(y4 - y1)) - ((y2 - y1)*(x4 - x1))
cross2 = ((x2 - x1)*(y3 - y1)) - ((y2 - y1)*(x3 - x1))
cross3 = ((x4 - x3)*(y2 - y3)) - ((y4 - y3)*(x2 - x3))
cross4 = ((x4 - x3)*(y1 - y3)) - ((y4 - y3)*(x1 - x3))

if cross1*cross2 == 0 and cross3*cross4 == 0:
    if cross1 == 0 and cross2 == 0: #일직선
        if x1 == x2: # 일직선, 기울기 없음
            if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
                print(0)
            elif y1 < y2 and y2 == y3 and y3 < y4:
                print(1)
                print(x2, y2)
            elif y4 < y3 and y3 == y2 and y2 < y1:
                print(1)
                print(x2, y2)
            elif y2 < y1 and y1 == y3 and y3 < y4:
                print(1)
                print(x1, y1)
            elif y2 < y1 and y1 == y4 and y4 < y3:
                print(1)
                print(x1, y1)
            elif y1 < y2 and y2 == y4 and y4 < y3:
                print(1)
                print(x2, y2)
            elif y4 < y3 and y3 == y1 and y1 < y2:
                print(1)
                print(x1, y1)
            elif y3 < y4 and y4 == y1 and y1 < y2:
                print(1)
                print(x1, y1)
            elif y3 < y4 and y4 == y2 and y2 < y1:
                print(1)
                print(x2, y2)
            else:
                print(1)
        else: #일직선, 기울기 있음
            if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
                print(0)
            elif x1 < x2 and x2 == x3 and x3 < x4:
                print(1)
                print(x2, y2)
            elif x4 < x3 and x3 == x2 and x2 < x1:
                print(1)
                print(x2, y2)
            elif x2 < x1 and x1 == x3 and x3 < x4:
                print(1)
                print(x1, y1)
            elif x2 < x1 and x1 == x4 and x4 < x3:
                print(1)
                print(x1, y1)
            elif x1 < x2 and x2 == x4 and x4 < x3:
                print(1)
                print(x2, y2)
            elif x4 < x3 and x3 == x1 and x1 < x2:
                print(1)
                print(x1, y1)
            elif x3 < x4 and x4 == x1 and x1 < x2:
                print(1)
                print(x1, y1)
            elif x3 < x4 and x4 == x2 and x2 < x1:
                print(1)
                print(x2, y2)
            else:
                print(1)
    else: #일직선이 아니고 외적곱이 모두 0인 경우
        if x1 == x2:
            rx = x1
            m2 = (y4 - y3)/(x4 - x3)
            n2 = y3 - (m2*x3)
            ry = (m2*rx) + n2
            print(1)
            print(rx, ry)
        elif x3 == x4:
            rx = x3
            m1 = (y2 - y1)/(x2 - x1)
            n1 = y1 - (m1*x1)
            ry = (m1*rx) + n1
            print(1)
            print(rx, ry)
        else:
            m1 = (y2 - y1)/(x2 - x1)
            m2 = (y4 - y3)/(x4 - x3)
            n1 = y1 - (m1*x1)
            n2 = y3 - (m2*x3)
            rx = (n2 - n1)/(m1 - m2)
            ry = (m1*rx) + n1
            print(1)
            print(rx, ry)
elif cross1*cross2 <= 0 and cross3*cross4 <= 0:
    if x1 == x2:
        rx = x1
        m2 = (y4 - y3)/(x4 - x3)
        n2 = y3 - (m2*x3)
        ry = (m2*rx) + n2
        print(1)
        print(rx, ry)
    elif x3 == x4:
        rx = x3
        m1 = (y2 - y1)/(x2 - x1)
        n1 = y1 - (m1*x1)
        ry = (m1*rx) + n1
        print(1)
        print(rx, ry)
    else:
        m1 = (y2 - y1)/(x2 - x1)
        m2 = (y4 - y3)/(x4 - x3)
        n1 = y1 - (m1*x1)
        n2 = y3 - (m2*x3)
        rx = (n2 - n1)/(m1 - m2)
        ry = (m1*rx) + n1
        print(1)
        print(rx, ry)
else:
    print(0)