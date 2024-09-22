import sys
input=sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    g = float(input())
    A.append(g)
A.sort()
for j in range(0, 7):
    print("{:.3f}".format(A[j]))