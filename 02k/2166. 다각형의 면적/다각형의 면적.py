import sys
input = sys.stdin.readline
X = []
Y = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.append(X[0])
Y.append(Y[0])
a = 0
b = 0

for i in range(n):
    a += X[i] * Y[i+1]
    b += X[i+1] * Y[i]
print(abs((a-b)/2))