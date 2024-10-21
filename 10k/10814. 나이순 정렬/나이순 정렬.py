import sys
input = sys.stdin.readline

A = []
t = int(input())
for _ in range(t):
    a, b = input().split()
    A.append([int(a), b])

A.sort(key=lambda x: x[0])
for a in A:
    print(a[0], a[1])