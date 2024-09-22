n, m = map(int, input().split())
A = []
B = []
result = []

for _ in range(n):
    r1 = list(map(int, input().split()))
    A.append(r1)
    
for _ in range(n):
    r2 = list(map(int, input().split()))
    B.append(r2)
    
for i in range(n):
    for j in range(m):
        result = A[i][j] + B[i][j]
        print(result, end=' ')
    print()