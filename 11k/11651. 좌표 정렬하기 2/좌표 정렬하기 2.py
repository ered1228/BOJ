n = int(input())
A = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append([a, b])

A.sort(key=lambda x: (x[1], x[0]))
for a in A:
    print(a[0], a[1])