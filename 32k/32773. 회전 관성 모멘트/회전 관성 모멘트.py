import sys
input = sys.stdin.readline

n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(float, input().split())
    X.append(x)
    Y.append(y)

X.append(X[0])
Y.append(Y[0])

I = 0
for i in range(n):
    qx = (X[i]*Y[i+1] - X[i+1]*Y[i])*(Y[i]**2 + Y[i]*Y[i+1] + Y[i+1]**2)
    qy = (X[i]*Y[i+1] - X[i+1]*Y[i])*(X[i]**2 + X[i]*X[i+1] + X[i+1]**2)
    I += qx + qy

print("{:.1f}".format(abs(I)/12))