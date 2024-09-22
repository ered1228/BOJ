import cmath
import math

def steiner_inellipse(x1, y1, x2, y2, x3, y3):
    z1 = complex(x1, y1)
    z2 = complex(x2, y2)
    z3 = complex(x3, y3)
    
    # f(z) = (z-a)(z-b)(z-c)
    fa = z1 + z2 + z3
    fb = z1*z2 + z2*z3 + z3*z1
    fc = z1 * z2 * z3
    
    #도함수 계수
    a = 3
    b = -2*fa
    c = fb
    
    # Marden's Theorem
    delta = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    focus1 = (x1.real, x1.imag)
    focus2 = (x2.real, x2.imag)
    return focus1, focus2

def find_rl(f1, f2):
    d = math.sqrt((f1[0] - f2[0])**2 + (f1[1] - f2[1])**2)
    p1 = ((x1+x2)/2, (y1+y2)/2)
    rl = math.sqrt((f1[0] - p1[0])**2 + (f1[1] - p1[1])**2) + math.sqrt((f2[0] - p1[0])**2 + (f2[1] - p1[1])**2)
    return rl

t = int(input())

for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    focus1, focus2 = steiner_inellipse(x1, y1, x2, y2, x3, y3)
    if (focus1[0] > focus2[0]) or (focus1[0] == focus2[0] and focus1[1] > focus2[1]):
        focus1, focus2 = focus2, focus1
    rl = find_rl(focus1, focus2)
    print(f"{focus1[0]:.2f} {focus1[1]:.2f} {focus2[0]:.2f} {focus2[1]:.2f} {rl:.2f}")