A = list(map(int, input().split()))
B = [1, 1, 2, 2, 2, 8]
C = []
for i in range(6):
    C.append(B[i]-A[i])
for c in C:
    print(c, end=" ")