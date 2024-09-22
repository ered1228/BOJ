import math

# 0 <= a, b, s <= 10^18
# ax + by = s
def extended_Euclidean(r1, r2, s1, s2, t1, t2):
    while r2 != 0:
        q = r1 // r2
        r = r1 - (q * r2)
        s = s1 - (q * s2)
        t = t1 - (q * t2)
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
    return [r1, s1, t1]

a, b, s = map(int, input().split())

def solution(a, b, s):
    if a == 0 and b == 0:
        if s == 0:
            return True
        else:
            return False
    elif a == 0 and b != 0:
        if s % b == 0:
            return True
        else:
            return False
    elif a != 0 and b == 0:
        if s % a == 0:
            return True
        else:
            return False
    elif a == s or b == s:
        return True
    elif a + b > s:
        return False
    elif a + b == s:
        return True
    else:
        EEA = extended_Euclidean(a, b, 1, 0, 0, 1)
        g = EEA[0]
        x0 = EEA[1]
        y0 = EEA[2]
        if s % g != 0:
            return False
        else:
            x0 *= s // g
            y0 *= s // g
            for k in range((-g*x0//b)+1, (g*y0//a)+1):
                if math.gcd(x0 + k*b//g, y0 - k*a//g) == 1:
                    return True
            return False

if solution(a, b, s):
    print("YES")
else:
    print("NO")