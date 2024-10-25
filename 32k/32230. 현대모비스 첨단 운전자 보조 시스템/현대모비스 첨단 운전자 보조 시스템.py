import math

def area(X, Y):
    X.append(X[0])
    Y.append(Y[0])
    xsum = 0
    ysum = 0
    for i in range(n):
        xsum += X[i] * Y[i+1]
        ysum += X[i+1] * Y[i]
    return (abs((xsum-ysum)/2))


n = int(input())
if n <= 2:
    print(0)
else:
    X = [] ; Y = []
    for i in range(n):
        a, b = map(int, input().split())
        X.append(a)
        Y.append(b)
    res = area(X, Y)
    res *= (1-(math.pi/(3*math.sqrt(3))))
    res /= 3
    print(res)