n = int(input())
A = list(map(int, input().split()))

B = sorted(list(set(A)))

C = {}
for i in range(len(B)):
    C[B[i]] = i

for j in A:
    print(C[j], end=" ")