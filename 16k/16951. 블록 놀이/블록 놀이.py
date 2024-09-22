import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = []
D = []

for i in range(1000):
    B = [i + 1 + (j * k) for j in range(n)]    
    C = [A[j] - B[j] for j in range(n)]
    D.append(C.count(0))
    
print(n-max(D))