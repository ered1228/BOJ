R = []

n = int(input())

for i in range(2000):
    for j in range(2000):
        tmp = 3*i + 5*j
        if tmp == n:
            R.append(i+j)

if len(R) == 0:
    print(-1)
else:
    print(min(R))