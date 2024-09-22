X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for i in range(3):
    if X.count(X[i]) == 1:
        resultx = X[i]
    if Y.count(Y[i]) == 1:
        resulty = Y[i]
print(resultx, resulty)