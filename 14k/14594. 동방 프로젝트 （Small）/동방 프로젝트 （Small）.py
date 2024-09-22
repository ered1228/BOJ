n = int(input())
m = int(input())
R = [0]*n

for i in range(m):
    x, y = map(int, input().split())
    for j in range(x, y):
        R[j] = 1

print(R.count(0))