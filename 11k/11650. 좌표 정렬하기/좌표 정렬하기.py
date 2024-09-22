n = int(input())
A = []
for _ in range(n):
    [x, y] = map(int, input().split())
    A.append([x, y])
A.sort()
for i in range(n):
    print(A[i][0], A[i][1])