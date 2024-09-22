n, m = map(int, input().split())
A = [0] * n

for y in range(m):
    i, j, k = map(int, input().split())
    for z in range(i-1, j):
        A[z] = k
        
for a in A:
    print(a, end=" ")