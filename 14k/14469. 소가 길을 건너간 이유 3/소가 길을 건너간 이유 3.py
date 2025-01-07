n = int(input())
cows = []
for _ in range(n):
    a, b = map(int, input().split())
    cows.append((a, b))

cows.sort(key=lambda x: (x[0], x[1]))
t = cows[0][0] ; end = t + cows[0][1]
for i in range(n):
    if end > cows[i][0]:
        stay = 0
    else:
        stay = cows[i][0] - end
    t += stay
    t += cows[i][1]
    end = t

print(t)