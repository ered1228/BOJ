n = int(input())
X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

p = Y.index(min(Y))
print(X[p], end=' ')
print(Y[p], end=' ')