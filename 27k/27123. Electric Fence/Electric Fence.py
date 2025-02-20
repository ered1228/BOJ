def Euclidean(a, b):
    if b == 0:
        return a
    else:
        return Euclidean(b, a%b)

def pick(area, perimeter):
    return area + 1 - (perimeter/2)

n, m, p = map(int, input().split())
area = (m*p) / 2
perimeter = Euclidean(n, m) + Euclidean(abs(p-n), m) + p
print(int(pick(area, perimeter)))