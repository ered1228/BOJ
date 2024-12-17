def Euclidean(a, b):
    if b == 0:
        return a
    return Euclidean(b, a%b)

a, b = map(int, input().split())
print('1'*Euclidean(a, b))