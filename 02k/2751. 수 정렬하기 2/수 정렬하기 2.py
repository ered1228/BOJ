import sys

A = []
n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    A.append(x)
    
A.sort()

for a in A:
    print(a)