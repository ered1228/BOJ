import sys
input = sys.stdin.readline

def Euclidean(x, y):
    while y != 0:
        [x, y] = [y, x%y]
    return x

n = int(input())
start = int(input())
A = [start, 0]
B = [0]*(n-1)

for i in range(n-1):
    A[1] = int(input())
    B[i] = A[1] - A[0]
    A[0] = A[1]

gcd = Euclidean(B[0], B[1])
for j in range(len(B)-2):
    gcd = Euclidean(gcd, B[j+2])

print(((A[1] + gcd - start)//gcd) - n)