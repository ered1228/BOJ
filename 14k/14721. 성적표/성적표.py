X = []
Y = []
R = float('inf')

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

resulta = 0    
resultb = 0

for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for i in range(len(X)):
            rss += (Y[i] - (a*X[i] + b))**2
        if R > rss:
            R = rss
            resulta = a
            resultb = b

print(resulta, resultb)