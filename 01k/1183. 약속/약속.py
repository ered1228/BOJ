import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a-b)

if n % 2 == 1:
    print(1)
else:
    A.sort()
    m = (len(A)//2) - 1
    print((A[m+1]-A[m])+1)