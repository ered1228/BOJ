import math

def factor(l):
    F = []
    for i in range(1, int(math.sqrt(l))+1):
        if l % i == 0:
            F.append(i)
            if i != l//i:
                F.append(l//i)
    return sorted(F, reverse=True)

a, b, l = map(int, input().split())
if l < max(a, b):
    print(-1)
elif l == max(a, b):
    print(1)
elif l % math.lcm(a, b) != 0:
    print(-1)
else:
    F = factor(l)
    c = float('inf')
    for f in F:
        temp = math.lcm(a, b, f)
        if temp == l:
            c = min(c, f)
    if c == float('inf'):
        print(-1)
    else:
        print(c)