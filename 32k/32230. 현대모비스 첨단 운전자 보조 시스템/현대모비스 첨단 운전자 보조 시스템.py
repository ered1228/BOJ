import cmath
import math

def steiner_inellipse(x1, y1, x2, y2, x3, y3):
    z1 = complex(x1, y1)
    z2 = complex(x2, y2)
    z3 = complex(x3, y3)
    # f(z)
    fa = z1 + z2 + z3
    fb = z1*z2 + z2*z3 + z3*z1
    fc = z1 * z2 * z3 
    # f'(z)
    a = 3
    b = -2*fa
    c = fb
    # Marden's Theorem
    delta = b**2 - 4*a*c
    sol1 = (-b + cmath.sqrt(delta)) / (2*a)
    sol2 = (-b - cmath.sqrt(delta)) / (2*a)
    f1 = (sol1.real, sol1.imag)
    f2 = (sol2.real, sol2.imag)
    # area of enellipse
    d = math.dist(f1, f2)
    p1 = ((x1+x2)/2, (y1+y2)/2)
    rl = math.sqrt((f1[0] - p1[0])**2 + (f1[1] - p1[1])**2) + math.sqrt((f2[0] - p1[0])**2 + (f2[1] - p1[1])**2)
    long = rl / 2
    short = math.sqrt(long**2 - (d/2)**2)
    return math.pi * long * short

def tri_area(x1, y1, x2, y2, x3, y3):
    X = [x1, x2, x3, x1]
    Y = [y1, y2, y3, y1]
    xsum = 0
    ysum = 0
    for i in range(3):
        xsum += X[i] * Y[i+1]
        ysum += X[i+1] * Y[i]
    return (abs((xsum-ysum)/2))

def COM(P):
    X = [p[0] for p in P]
    Y = [p[1] for p in P]
    xcom = sum(X) / n
    ycom = sum(Y) / n
    return xcom, ycom

n = int(input())
if n <= 2:
    print(0)
else:
    P = []
    res = 0
    for i in range(n):
        a, b = map(int, input().split())
        P.append([a, b])
    xcom, ycom = COM(P)
    P.append(P[0])
    for j in range(n):
        area = tri_area(xcom, ycom, P[j][0], P[j][1], P[j+1][0], P[j+1][1])
        area -= steiner_inellipse(xcom, ycom, P[j][0], P[j][1], P[j+1][0], P[j+1][1])
        area /= 3
        res += area
    print(res)